import requests


HEADERS = {'content-type': 'application/json'}

class Kraken_api:

    def __init__(self, thing):

        self._base_url = None
        self._thing = thing

    async def get(self, record_type, record_id):
        # Get a single record from api

        params = {'@type': record_type, '@id': record_id}
        
        r = requests.get(self._base_url, headers=HEADERS, params=params)
        records = r.json()

        self._thing._db_load(records)
        
        return

    
    async def post(self, records):
        #Post to api returns new records

        
        r = requests.post(self._base_url, headers=HEADERS, data=self._thing.db_json())

        new_records = r.json()
        
        return new_records

    