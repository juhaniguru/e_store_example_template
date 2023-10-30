import typing

import strawberry
from strawberry.types import Info

import models
from graphql_types.customer import Customer, get_all_customers, get_customer_by_id
from services.customers_sa import CustomersSA


@strawberry.type
class Query:
    customers: typing.List[Customer] = strawberry.field(resolver=get_all_customers)
    customer: typing.Optional[Customer] = strawberry.field(resolver=get_customer_by_id)
    # @strawberry.field
    # def customers(self, info: Info) -> typing.List[Customer]:
    #     """ get list of customer models using service and return list of graphlql.Customers"""
    #     customer_models = info.context['customers'].get_all()
    #     return [Customer(id=c.id, first_name=c.first_name, last_name=c.last_name) for c in customer_models]
