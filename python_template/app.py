from fastapi import FastAPI
from env2 import env2 as env


app = FastAPI(debug=bool(env('APP_LEVEL', False, False)))


@app.get('/')
async def index():
    return "Hello, world"
