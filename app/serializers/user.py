from pydantic import BaseModel, constr


class User(BaseModel):
    id: int
    fullname: constr(max_length=50)
    nickname: constr(max_length=20)
    password: constr(max_length=20)

    class Config:
        orm_mode = True
