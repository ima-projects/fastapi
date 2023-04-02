from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional

# the funtionality of these will be added in each of the functions under routers files

#Client Post Request
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

#User Response. This needs to be pur above post Response in order to return UserOut in Post class (schema)
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode=True

#Response 
    #also logic from our (get post) route will grab the owner_id from the token (id of logged in user) and use that as our (owner_id) field. Therefore, no need for client/user to provide  owner_id in body
class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut #returning a pydantic schema/model

    class Config:
        orm_mode=True

class PostOut(BaseModel):
    # make sure Post is capitalised here bc our (database) query returns it with a capital P. So small instance where Pydantic is case sensitive
    # value references class Post just above this class. All of the class Post fields will be under the one field as Post
    Post: Post
    votes: int

    class Config:
        orm_mode=True



#User Request
class UserCreate(BaseModel):
    email: EmailStr
    password: str



# Authentication (Login by user)

class UserLogin (BaseModel):
    email: EmailStr
    password: str


#Token provided back by user (client)
class Token(BaseModel):
    access_token: str
    token_type: str

#Actual data within the access token
class TokenData(BaseModel):
    id: Optional[str] = None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)