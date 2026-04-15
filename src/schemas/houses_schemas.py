from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class HouseBase(BaseModel):
    id: UUID
    user_id: UUID
    color: str

    class Config:
        """Configure Pydantic to allow population from ORM objects and provide an example."""
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "user_id": "123e4567-e89b-12d3-a456-426614174000",
                "color": "blue"
            }
        }


class HousePost(BaseModel):
    user_id: UUID
    color: str

    class Config:
        """Configure Pydantic to allow population from ORM objects and provide an example."""
        from_attributes = True
        json_schema_extra = {
            "example": {
                "user_id": "123e4567-e89b-12d3-a456-426614174000",
                "color": "blue"
            }
        }


class HouseUpdate(BaseModel):
    user_id: Optional[UUID]
    color: Optional[str]

    class Config:
        """Configure Pydantic to allow population from ORM objects and provide an example."""
        from_attributes = True
        json_schema_extra = {
            "example": {
                "user_id": "123e4567-e89b-12d3-a456-426614174000",
                "color": "blue"
            }
        }
