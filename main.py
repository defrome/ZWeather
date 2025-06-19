from operator import truediv
import os
import uvicorn
import httpx
from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

API_KEY = 'd11caa373e4345afb76143753251906'

@app.get('/verified_api')
async def verified_api(api_key: str):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail='Invalid API_KEY')
    return True

@app.get('/current_weather')
async def get_current_weather(city: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"http://api.weatherapi.com/v1/current.json?key=d11caa373e4345afb76143753251906&q={city}&aqi=no"
        )
        data = response.json()
        return {
            "city": city,
            "temp": data['current']['temp_c']
        }


print(API_KEY)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=3000)