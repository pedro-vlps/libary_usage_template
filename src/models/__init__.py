from src.models.models import Users, Houses

from src.schemas.users_schemas import UserBase, UserPost, UserUpdate
from src.schemas.houses_schemas import HouseBase, HousePost, HouseUpdate

from src.configs.db_connection import get_session

routes_declaration = [
    {
        "model_class": Users,
        "standard_schema": UserBase,
        "db_session": get_session,
        "auth_callback": None,
        "request_post_schema": UserPost,
        "request_update_schema": UserUpdate,
        "response_get_schema": UserBase,
        "response_get_by_id_schema": UserBase,
        "response_post_schema": UserBase,
        "response_delete_schema": None,
        "response_patch_schema": UserBase,
        "enable_get": True,
        "enable_get_by_id": True,
        "enable_post": True,
        "enable_delete": True,
        "enable_patch": True,
        "join_parameters": None,
        "second_level_join_parameters": None,
        "route_prefix": "/users",
        "route_tags": ["Users"],
    },
    {
        "model_class": Houses,
        "standard_schema": HouseBase,
        "db_session": get_session,
        "auth_callback": None,
        "request_post_schema": HousePost,
        "request_update_schema": HouseUpdate,
        "response_get_schema": HouseBase,
        "response_get_by_id_schema": HouseBase,
        "response_post_schema": HouseBase,
        "response_delete_schema": None,
        "response_patch_schema": HouseBase,
        "enable_get": True,
        "enable_get_by_id": True,
        "enable_post": True,
        "enable_delete": True,
        "enable_patch": True,
        "join_parameters": [
            {
                "model": Users,
                "column": "user_id",
                "response_parameter": Houses.user
            }
        ],
        "second_level_join_parameters": None,
        "route_prefix": "/houses",
        "route_tags": ["Houses"],
    }
]