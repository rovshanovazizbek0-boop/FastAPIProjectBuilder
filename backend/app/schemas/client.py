from pydantic import BaseModel, EmailStr

class ClientBase(BaseModel):
    email: EmailStr
    company_name: str
    language_preference: str = 'uz'

class ClientCreate(ClientBase):
    password: str

class ClientPublic(ClientBase):
    id: int

    class Config:
        from_attributes = True