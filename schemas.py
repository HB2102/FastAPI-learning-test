from pydantic import BaseModel
from typing import List



# article in user display
class Article(BaseModel):
    title: str
    content: str
    published: bool

    class Config:
        from_attributes = True




class UserBase(BaseModel):
    username: str
    password: str
    email: str


class UserDisplay(BaseModel):
    username: str
    email: str
    items: List[Article]

    class Config:
        from_attributes = True


class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int


# user in article display
class User(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True

class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: User

    class Config:
        from_attributes = True