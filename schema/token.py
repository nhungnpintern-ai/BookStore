from pydantic import BaseModel
from typing import Optional


class TokenData(BaseModel):
    email: Optional[str] = None


class token(BaseModel):
    access_token: str
    token_type: str = "bearer"
