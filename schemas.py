from pydantic import BaseModel

# Base class for User schema
class UserBase(BaseModel):
    username: str

# Schema for creating a user (inherits from UserBase and adds a password field)
class UserCreate(UserBase):
    password: str

# Schema for returning a user (inherits from UserBase and adds an ID field)
class User(UserBase):
    id: int

    class Config:
        orm_mode = True

# Base class for Item schema
class ItemBase(BaseModel):
    title: str
    description: str

# Schema for creating an item (inherits from ItemBase)
class ItemCreate(ItemBase):
    pass

# Schema for returning an item (inherits from ItemBase and adds an ID field)
class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True

# Schema for the token response
class Token(BaseModel):
    access_token: str
    token_type: str
