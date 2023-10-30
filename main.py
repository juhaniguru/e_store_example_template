import strawberry
import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter

import controllers.customers
import mutation
import query
from services.customers_sa import CustomerService

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def get_context(customerService: CustomerService):
    return {
        'customers': customerService
    }


schema = strawberry.Schema(query.Query, mutation=mutation.Mutation)

graphql_app = GraphQLRouter(schema, context_getter=get_context)

app.include_router(controllers.customers.router)
app.include_router(graphql_app, prefix='/graphql')

if __name__ == '__main__':
    uvicorn.run('main:app', port=5003)
