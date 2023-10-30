from typing import Annotated

from fastapi import Depends

import models
from services.base import BaseService


def init_customer_service(db: models.Db):
    return CustomersSA(db)


CustomerService = Annotated[BaseService, Depends(init_customer_service)]


class CustomersSA(BaseService):
    def __init__(self, db: models.Db):
        super(CustomersSA, self).__init__(db)

    def get_all(self):
        customers = self.db.query(models.Customer).all()

        return customers

    def get_by_id(self, _id: int):
        return self.db.query(models.Customer).get(_id)

    def add_customer(self, first_name: str, last_name: str):
        c = models.Customer(first_name=first_name, last_name=last_name)
        self.add(c)
        return c

    def delete(self, _id: int):
        self.db.query(models.Customer).filter(models.Customer.id == _id).delete()
        self.commit()

        return True



