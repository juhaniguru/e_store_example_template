from fastapi import APIRouter, HTTPException, Path

from dtos.customer import Customers, Customer, AddCustomerReq
from services.customers_sa import CustomerService

router = APIRouter(
    prefix='/api/v1/customers',
    tags=['customers']
)


@router.get('/', response_model=Customers)
async def get_customers(service: CustomerService):
    customers = service.get_all()
    return {'customers': customers}


@router.get('/{_id}', response_model=Customer)
async def get_customer(service: CustomerService, _id: int = Path(gt=0)):
    customer = service.get_by_id(_id)
    if customer is None:
        raise HTTPException(status_code=404, detail='Not found')
    return customer


@router.post('/', response_model=Customer)
async def add_customer(service: CustomerService, req: AddCustomerReq):
    customer = service.add_customer(req.first_name, req.last_name)
    return customer


@router.delete('/{_id}')
async def delete_customer(service: CustomerService, _id: int = Path(gt=0)):
    return service.delete(_id)
