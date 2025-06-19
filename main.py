from operator import truediv

from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

API_KEY = 'd11caa373e4345afb76143753251906'

async def verified_api(api_key: str = Header()):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail='Invalid API_KEY')
    return True

@app.get('/verified_api')
async def verified_api_get():
    await verified_api()