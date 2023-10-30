import strawberry
from fastapi import HTTPException
from strawberry.types import Info


@strawberry.type
class Customer:
    id: int
    first_name: str
    last_name: str


def add_new_customer(first_name: str, last_name: str, info: Info):
    c = info.context['customers'].add_customer(first_name, last_name)
    return Customer(id=c.id, first_name=first_name, last_name=last_name)


def get_customer_by_id(_id: int, info: Info):
    customer = info.context['customers'].get_by_id(_id)
    if customer is None:
        raise Exception('Not found')
    return Customer(id=customer.id, first_name=customer.first_name, last_name=customer.last_name)


def get_all_customers(info: Info):
    customer_models = info.context['customers'].get_all()
    return [Customer(id=c.id, first_name=c.first_name, last_name=c.last_name) for c in customer_models]
