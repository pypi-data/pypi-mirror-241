
from kraken_thing.kraken_class_thing.kraken_class_thing import Thing
#from kraken_thing.kraken_class_things.helpers import things_json
from kraken_thing.kraken_class_thing_html.kraken_class_things_html import Things_html
from kraken_thing.kraken_class_things.helpers import things_output
from kraken_thing.kraken_class_thing_db.kraken_class_things_db import Kraken_things_db

import kraken_thing_methods as kr


class Things:

    def __init__(self, things=None):

        self._things = []
        self._related_things = []
        self.html = Things_html(self)

        self.add(things)

        # Add db module
        self.db = Kraken_things_db(self)
    
    def __add__(self, other):
        #
        if not isinstance(other, Things):
            return

        t = Things()

        for i in self._things:
            t.add(i)
        for i in other._things:
            self.add(i)
        return
        
    def __len__(self):
        return len(self._things)


    def __str__(self):
        return self.summary()
    
    def __repr__(self):
        return self.summary()

    def summary(self):
        # returns 
        return things_output.get_summary_string(self.things)
    
    def get(self, type, id):
        '''Return specific thing
        '''
        results = [x for x in self._things if x.type == type and x.id == id]
        return results[0] if len(results) > 0 else None


    def add(self, thing):
        '''Add a thing to list
        '''

        if not thing:
            return
        
        # Deal with list
        if isinstance(thing, list):
            for i in thing:
                self.add(i)
            return

        # Deal with non thing
        if not isinstance(thing, Thing):
            return self.load(thing)


        # Add thing
        if thing in self._things:
            old_thing = self.get(thing.type, thing.id)
            if old_thing:
                old_thing.add(thing)
        else:
            self._things.append(thing)
        
        # Add  related things
        for i in thing.related_things():
            # Merge if exists
            self._add_to_related(i)
            
        
    def _add_to_related(self, thing):
        """
        """
        for i in self._related_things:
            if i == thing:
                i.add(thing)
                return i
        self._related_things.append(thing)
    
    def load(self, record):
        '''Load records into things
        '''

        if not record:
            return
            
        # Deal with list
        if isinstance(record, list):
            for i in record:
                self.load(i)
            return

        # Deal with non-dict
        if not isinstance(record, dict):
            return

        # Create and add new thing
        t = Thing()
        t.load(record)
        self.add(t)
        return

    def dump(self):
        # Dumps records
        records = [x.dump() for x in self._things]
        return records

    def json(self):
        #Returns self.dump() in json format
        return kr.json.dumps(self.dump())
    
    def _db_load(self, record):
        #Load records from db
        if not record:
            return
        # Deal with list
        if isinstance(record, list):
            for i in record:
                self._db_load(i)
            return

        # Deal with non-dict
        if not isinstance(record, dict):
            return

        # Create and add new thing
        t = Thing()
        t._db_load(record)
        self.add(t)
        return

    def _db_dump(self):
        # db dump
        records = []
        for x in self._things:
            records.append(x._db_dump())
        return records

    @property
    def things(self):
        return sorted(self._things)

    @things.setter
    def things(self, values):
        self.add(values)
        return

    def to_list(self):
        #Returns a list thing with all things included in it
        
        thing_list = Thing('ItemList')
        for i in self.things:
            t = Thing('ListItem')
            t.set('item', i)
            thing_list.set('itemListElement', t)
        return thing_list
        
   