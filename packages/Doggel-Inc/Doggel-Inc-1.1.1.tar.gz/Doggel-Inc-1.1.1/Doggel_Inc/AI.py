import aiohttp

apikey = None

def setup(key):
    global apikey
    apikey = key

async def request(ctxx, message):
    if message == "":
        message = ctxx.content
    global apikey
    request_headers = {'Authorization': apikey}
    async with aiohttp.ClientSession() as session:                                     
        api_url = 'http://us3.techstar.host:55565/request'
        request_data = {'message': message,'message-author-id': ctxx.author.id,'message-author-user': ctxx.author.name,'function': "ai"}
        async with session.post(api_url, json=request_data, headers=request_headers) as response:
            api_response = await response.json()
            return api_response
