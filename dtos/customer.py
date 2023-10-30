import typing

from pydantic import BaseModel


class Customer(BaseModel):
    id: int
    first_name: str
    last_name: str


class Customers(BaseModel):
    customers: typing.Optional[typing.List[Customer]] = []


class AddCustomerReq(BaseModel):
    first_name: str
    last_name: str
