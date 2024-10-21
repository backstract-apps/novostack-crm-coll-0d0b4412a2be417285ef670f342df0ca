from pydantic import BaseModel

from datetime import datetime

class Persons(BaseModel):
    rollnumber: int
    fullname: str
    age: int
    profession: str


class ReadPersons(BaseModel):
    rollnumber: int
    fullname: str
    age: int
    profession: str
    class Config:
        from_attributes = True


class Addresses(BaseModel):
    id: int
    street: str
    city: str
    state: str
    country: str
    postal_code: str
    created_at: datetime
    updated_at: datetime


class ReadAddresses(BaseModel):
    id: int
    street: str
    city: str
    state: str
    country: str
    postal_code: str
    created_at: datetime
    updated_at: datetime
    class Config:
        from_attributes = True


