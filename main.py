import strawberry
import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter

import controllers.customers

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(controllers.customers.router)

if __name__ == '__main__':
    uvicorn.run('main:app', port=8081)
