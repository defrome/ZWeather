from operator import truediv
import os
import uvicorn
from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

API_KEY = 'd11caa373e4345afb76143753251906'

@app.get('/verified_api')
async def verified_api(api_key: str):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail='Invalid API_KEY')
    return True

print(API_KEY)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=3000)