from typing import Union

from pydantic import BaseModel, Field, confloat, conint, constr


class Event(BaseModel):
    user_id: constr(min_length=1, max_length=500)
    item_id: Union[constr(min_length=1, max_length=500), None]
    timestamp: confloat(ge=1_648_871_097.0, le=2_147_483_647.0)
    event_type: constr(min_length=1, max_length=500)
    event_value: constr(min_length=1, max_length=500)
    from_: Union[constr(min_length=1, max_length=500), None] = Field(alias="from")
    is_zai_recommendation: bool
    time_to_live: Union[conint(ge=0), None] = None

    class Config:
        allow_population_by_field_name = True

        schema_extra = {
            "example": {
                "user_id": "123456",
                "item_id": "ABCDEF",
                "timestamp": 1_648_871_097.0,
                "event_type": "product_detail_view",
                "event_value": "1",
                "from": "home",
                "is_zai_recommendation": True,
                "time_to_live": 60 * 60 * 24,
            }
        }
