import asyncio
import aiohttp
import os



API_URL = os.getenv('API_URL')





async def get(self, record_type, record_id):
    #
    headers = {'content-type': "application/json"}
    params = {}

    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(API_URL, params=params) as response:
                content = await response.text()
    except Exception as e:
        print('Error kraken_api - get ', e)
        return False

    if response.status == 200:
        return content
    else:
        return False



    def search(self, record_type, record_id):
        #

        return

    def post(self, records):
        #Post to api returns new records

        return

    