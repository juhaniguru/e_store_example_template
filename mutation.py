import strawberry

from graphql_types.customer import Customer, add_new_customer


@strawberry.type
class Mutation:
    add_customer: Customer = strawberry.mutation(resolver=add_new_customer)