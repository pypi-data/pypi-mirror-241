import copy
import uuid
import hashlib
import tabulate


import os
import kraken_thing_methods as kr



from kraken_thing.kraken_class_observation.kraken_class_observation import Observation
from kraken_thing.kraken_class_thing.templates import metadata_templates as template
from kraken_thing.kraken_class_thing.helpers import things_manipulation
#from kraken_thing.kraken_class_thing.helpers import thing_json
from kraken_thing.kraken_class_thing.helpers import thing_output
from kraken_thing.kraken_class_thing.helpers import thing_comparison
from kraken_thing.kraken_class_thing_html.kraken_class_thing_html import Thing_html
from kraken_thing.kraken_class_thing_db.kraken_class_thing_db import Kraken_thing_db

class Thing:

    def __init__(self, record_type = None, record_id=None, metadata=None):
        """Thing class to store observations of a thing.
        
        Attributes
        ----------
        type: str
            The type of the thing
        id:
            The id of the thing. Defaults to uuid4
        metadata: Observation
            An object to store metadata used to create new observations.
            

        Methods
        -------
        summary():
            Returns a text representation of the thing
        get(property) :
            Returns all values for a given property
        get_best() :
            Returns the best value for a property
        set(attribute, value):
            Creates a new observation with given attribute and value, using metadata as default
        load(record):
            Load a record
        dump():
            Dump the value of thing and sub things in json record
        db_load(record):
            Load a record
        db_dump():
            Dump the value of thing and sub things in full json record with metadata

        deduplicate_things(): 
            Removes duplicates in related things
    
        Returns
        -------
        list
            a list of strings used that are the header columns
        """

        
        self._o = []            # Observations
        self._metadata = Observation()

        self._things = []        # store indented records
        
        if record_type:
            self.type = record_type
        if record_id:
            self.id = record_id
            
        self.set('@context', 'https://schema.org/')

        self.template = template

        if metadata:
            self._metadata.load_metadata(metadata)

        # Add html module
        self.html = Thing_html(self)

        # Add db module
        self.db = Kraken_thing_db(self)

    
    def __str__(self):
        return self.summary()

    def __repr__(self):
        return self.summary()

    def __eq__(self, other):
        if not isinstance(other, Thing):
            return False
        return  thing_comparison.is_equal(self, other)
                    
    def __gt__(self, other):
        """
        """
        if not isinstance(other, Thing):
            return False
        return  thing_comparison.is_gt(self, other)

    
    def __lt__(self, other):
        if not isinstance(other, Thing):
            return False
        return  thing_comparison.is_lt(self, other)

    
    def __add__(self, other):
        """
        """
        if not isinstance(other, Thing):
            return False

        new_thing = Thing()
        for i in self._o:
            if i not in new_thing._o:
                new_thing._o.append(i)
            
        for i in other._o:
            if i not in new_thing._o:
                new_thing._o.append(i)
        return new_thing

    
    def __sub__(self, other):
        """Removes observations in other from self  
        """
        if not isinstance(other, Thing):
            return False
            
        t = Thing()
        for i in self._o:
            if i.k.startswith('@') or i not in other._o:
                t.add(i)
        return t


    def keys(self):
        """Returns all measuredProperty in ordered list
        """
        return sorted(list(set([x.measuredProperty for x in self._o])))
        
    
    def record_ref(self):
        """Return type and id in a dict
        """
        return {'@type': self.type, '@id': self.id}

    def record_refs(self):
        """Returns all possible record_ref (old data)
        """
        records = []
        types = [x.value for x in self.get('@type')]
        ids = [x.value for x in self.get('@id')]
        for type in types:
            for id in ids:
                record = {'@type': type, '@id': id}
                records.append(record)
        return records

    def record(self, in_json=False):
        """Returns thing as dict with all nested things as dict
        """

        record = self.dump(True)
        if in_json:
            return kr.json.dumps(record)
        else:
            return record
        
    
    def summary(self):
        """
        """
        return thing_output.get_summary_string(self.type, self.id, self._o)
        
    def get(self, parameter=None):
        """Retrieves all observations for a given parameter
        """

        obs = [o for o in self._o if o.k == parameter] if parameter else [o for o in self._o]
        obs.sort(reverse=True)
        return obs

    def get_best(self, parameter):
        """Returns best observation for given parameter
        """
        obs = self.get(parameter)
        return obs[0] if len(obs) > 0 else None
    
    
    def set(self, parameter, value, credibility=None, date=None):
        """Adds an observation with parameter and value.
        Uses default metadata if c and d not provided.
        """
        # Handle lists
        if isinstance(value, list):
            for i in value:
                self.set(parameter, i, credibility, date)
            return

        # Handle dict
        if isinstance(value, dict) and '@type' in value.keys():
            t = Thing()
            t.metadata.metadata = self.metadata.metadata
            t.load(value)
            self.add_related_thing(t)
            #value = t.record_ref()
            value = t

        # Handle things
        if isinstance(value, Thing):
            self.add_related_thing(value)
            #value = value.record_ref()
        
        # Convert to observation
        o = Observation(parameter, value, self.metadata.metadata)
        if credibility:
            o.c = credibility
        if date:
            o.d = date
                
        self.add(o)

        # if not valid, add valid version
        if not o.validValue:
            norm_o = o.get_normalized_observation()
            if norm_o.validValue:
                self.add(norm_o)

        
        return 

    def add(self, observation):
        """Add an observation
        """
        # Handle error
        if not observation:
            return
            
        # Handles list
        if isinstance(observation, list):
            for i in observation:
                self.add(i)
            return
        
        # If things, copies other thing observations into this one
        if isinstance(observation, Thing):
            self.add(observation.observations)
            return

        # Handles observation
        if isinstance(observation, Observation):
            if observation not in self._o:
                self._o.append(observation)
            return

        return


    
    """Related things
    """

    def add_related_thing(self, t):
        """Add a related thing to the list
        """
        if not t:
            return

        # Handles list
        if isinstance(t, list):
            for i in t:
                self.add_related_thing(i)
            return 

        # Add sub things
        for i in t.related_things():
            self.add_related_thing(i)

        # Add to itself if equal
        if t == self:
            self.add(t)

        else:
            self._things.append(t)
        
        return
        
    def related_things(self):
        """Return all nested things excluding itself
        """

        things = []
        for i in self._things:
            things += i.things()
        things = things_manipulation.deduplicate(things)
        things.sort()
        return things
        
    def things(self):
        """Return all the nested things, including itself
        """
        things = [self] + self.related_things()
        things = things_manipulation.deduplicate(things)
        things.sort()
        
        return things
    
    def deduplicate_things(self):
        """Deduplicate all related_things
        """
        # Todo: delete this method
        self._related_things = things_manipulation.deduplicate(self.related_things)
        return

    """ ID management
    """

    def harmonize_ids(self):
        """Verify all the ids for a related things
        Ensure that if a thing changed id, all references are changed as well
        """

        things_manipulation.harmonize_ids(self.things())
        return
        
        
    
    """Methods to load and dump records as dict (json)
    """

    def load(self, record):
        """Load dict (json) into thing.
        Uses values in @metadata else uses defaults 
        """

        # Deal with json
        if isinstance(record, str):
            record = kr.json.loads(record)

        # Deal with list of 1
        if isinstance(record, list):
            if len(record) == 1:
                record = record[0]
        
        for k, v in record.items():
            
            if k == '@metadata':
                self.metadata.load_metadata(v)
            else:
                self.set(k, v)
           
        return


    def dump(self, retrieve_all=True):
        """
        """

        # Harmonize ids across all things
        self.harmonize_ids()

        # Get list of attributes
        record = {}
        attr = list(set([o.k for o in self._o]))
        attr.sort()

        # Retrieve values for attributes
        for k in attr:

            if retrieve_all:
                record[k] = []
                values = [o.v for o in self.get(k)]
    
                for v in values:
                    if isinstance(v, Thing):
                        v = v.dump()
                    if v not in record[k]:
                        record[k].append(v)
            else:
                record[k] = self.get_best(k).v
                if isinstance(record[k], Thing):
                    record[k] = record[k].dump(retrieve_all)
        
        return record

    def dump_observations(self):
        """Returns observations as dict
        """
        records = []
        for i in self.observations:
            records.append(i.dump())
        return records

    
    def json(self):
        """Return a json record of thing without metadata
        """
        return kr.json.dumps(self.dump())

    def jsons(self):
        """Return a json record of all things without metadata
        """
        records = [x.dump() for x in self.things()]
        
        return kr.json.dumps(records)
    
    """Methods to load / dump records in database format
    """
    
    def _db_load(self, record):
        """Load record from database format (with metadata)
        """
        observations = record.get('observations',[])
        for i in observations:
            o = Observation()
            o.load(i)
            self.add(o)
        return
    
    def _db_dump(self, new_only=False):
        """Dump records in database format (with metadata)
        """
        # Harmonize ids across all things
        self.harmonize_ids()
        
        records = []

        # Export self
        record = {
            'type': self.type,
            'id': self.id,
            'observations': []
        }

        record['observations'] = [x.dump() for x in sorted(self._o) if x._db or not new_only]
        
        return record


    def db_json(self):
        """
        """
        return kr.json.dumps(self._db_dump())


    


    
    """Shortcuts
    """
    @property
    def metadata(self):
        return self._metadata

    @metadata.setter
    def metadata(self, value):
        self._metadata.load_metadata(value)
        return
        
    @property
    def observations(self):
        obs = []
        for i in self.keys():
            obs += self.get(i)
        return obs

    
    
    @property
    def type(self):
        o = self.get_best('@type')
        value = o.value if o else None
        if value and isinstance(value, str):
            value = value.replace('schema:', '')
        return value

    @type.setter
    def type(self, value:str):
        value = value.replace('schema:', '')
        self.set('@type', value)
        return

    @property
    def id(self):
        o = self.get_best('@id')
        if o and o.validValue:
            return o.value

        # Create new if None
        if not o or not o.value:
            o = Observation('@id', str(uuid.uuid4()))
            o.observationCredibility = 0
            self.add(o)

        # Todo: handle cases where id is invalid and needs to be replaced (add source object to uuid)
        
        return o.value if o else None


    @id.setter
    def id(self, value):
        self.set('@id', value)
        return
    
    @property
    def name(self):
        o = self.get_best('name')
        return o.value if o else None

    @name.setter
    def name(self, value):
        self.set('name', value)
        return

    @property
    def url(self):
        o = self.get_best('url')
        return o.value if o else None

    @url.setter
    def url(self, value):
        self.set('url', value)
        return

    @property
    def sameAs(self):
        values = [o.value for o in self.get('sameAs')]
        return values
        
    @sameAs.setter
    def sameAs(self, value):
        self.set('sameAs', value)




    @property
    def street(self):
        values = [o.value for o in self.get('streetAddress')]
        return values
        
    @street.setter
    def street(self, value):
        self.set('streetAddress', value)


    @property
    def city(self):
        values = [o.value for o in self.get('addressLocality')]
        return values
        
    @city.setter
    def city(self, value):
        self.set('addressLocality', value)

    @property
    def state(self):
        values = [o.value for o in self.get('addressRegion')]
        return values
        
    @state.setter
    def state(self, value):
        self.set('addressRegion', value)

    @property
    def country(self):
        values = [o.value for o in self.get('addressCountry')]
        return values
        
    @country.setter
    def country(self, value):
        self.set('addressCountry', value)

    @property
    def postal_code(self):
        values = [o.value for o in self.get('postalCode')]
        return values
        
    @postal_code.setter
    def postal_code(self, value):
        self.set('postalCode', value)

    

    
    def get_thumbnail(self):
        # Returns url of thumbnail
        url = None

        # Get thumbnail
        if not url:
            thumbnail = self.get_best('thumbnailUrl')
            if thumbnail:
                url = thumbnail.value
                
        # Get image
        if not url:
            image = self.get_best('image')
            if image: 
                print(image.value)
                url = image.value.get_image()

        # Get content
        if not url:
            content = self.get_best('contentUrl')
            if content:
                url = content.value

        

        return url

    def get_image(self):
        # Return url of image

        url = None

        # Get image
        image = self.get_best('image')
        if image: 
            url = image.value.get_image()

        # Get content
        if not url:
            content = self.get_best('contentUrl')
            if content:
                url = content.value

        # Get thumbnail
        if not url:
            thumbnail = self.get_best('thumbnailUrl')
            if thumbnail:
                url = thumbnail.value

        return url

    def get_name(self):
        # Returns Name
        name = None

        # Get from name
        name_obs = self.get_best('name')
        if name_obs:
            name = name_obs.value

        
        if self.type =='person':
            fname = self.get_best('givenName')
            lname = self.get_best('familyName')
            name = getattr(fname, 'value', '') + '' + getattr(lname, 'value', '') if fname and lname else None

        if not name:
            name = self.url if self.url else None

        if not name:
            name = self.id
        
        return name

    def record_type_id(self):

        return f'/{self.type}/{self.id}'