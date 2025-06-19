from operator import truediv
import os
from dotenv import load_dotenv
import uvicorn
import httpx
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Header, HTTPException
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

load_dotenv()

API_KEY = os.getenv('api_key')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Для разработки
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount('/static', StaticFiles(directory='static'), name='static')

@app.get('/verified_api')
async def verified_api(api_key: str):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail='Invalid API_KEY')
    return True

@app.get('/current_weather')
async def get_current_weather(city: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"
        )
        data = response.json()
        return {
            "city": city,
            "temp": data['current']['temp_c']
        }


print(API_KEY)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=3000)