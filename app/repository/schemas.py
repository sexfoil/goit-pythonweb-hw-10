from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional


class ContactBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    birthday: Optional[date]


class ContactCreate(ContactBase):
    pass


class ContactUpdate(ContactBase):
    pass


class ContactOut(ContactBase):
    id: int

    class Config:
        orm_mode = True

# from pydantic import BaseModel, EmailStr
# from typing import Optional

# class UserCreate(BaseModel):
#     email: EmailStr
#     password: str

# class UserOut(BaseModel):
#     id: int
#     email: EmailStr
#     is_active: bool
#     is_verified: bool

#     class Config:
#         orm_mode = True

# class Token(BaseModel):
#     access_token: str
#     token_type: str

# class TokenData(BaseModel):
#     email: Optional[str] = None