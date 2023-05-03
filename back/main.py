from fastapi import FastAPI
from db import models
from db.database import engine
from routers import user, item, cart
from fastapi.staticfiles import StaticFiles
from auth import authentication
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()
app.include_router(user.router)
app.include_router(cart.router)
app.include_router(authentication.router)

app.include_router(item.router)

@app.get('/')
def root():
    return 'Hello world!'


origins = [
    'http://localhost:8080'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


models.Base.metadata.create_all(engine)


app.mount('/images', StaticFiles(directory='images'), name='images')


if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)