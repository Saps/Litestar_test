from pydantic import BaseModel, ConfigDict
from typing import Optional


# ------------------------------------------
class UserCreate(BaseModel):
    name: str
    surname: str
    password: str
    model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    name: Optional[str] = None
    surname: Optional[str] = None
    password: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)


class UserShow(BaseModel):
    id: int
    name: str
    surname: str
    model_config = ConfigDict(from_attributes=True)
