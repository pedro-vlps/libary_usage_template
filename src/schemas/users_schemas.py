from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class UserBase(BaseModel):
    id: UUID
    name: str

    class Config:
        """Configure Pydantic to allow population from ORM objects and provide an example."""
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "name": "Pedro"
            }
        }


class UserPost(BaseModel):
    name: str

    class Config:
        """Configure Pydantic to allow population from ORM objects and provide an example."""
        from_attributes = True
        json_schema_extra = {
            "example": {
                "name": "Pedro"
            }
        }

class UserUpdate(BaseModel):
    name: Optional[str]

    class Config:
        """Configure Pydantic to allow population from ORM objects and provide an example."""
        from_attributes = True
        json_schema_extra = {
            "example": {
                "name": "Pedro"
            }
        }
