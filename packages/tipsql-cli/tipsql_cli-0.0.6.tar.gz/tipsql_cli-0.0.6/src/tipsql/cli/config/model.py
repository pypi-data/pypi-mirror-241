from pydantic import BaseModel, ConfigDict


class Model(BaseModel):
    pass


class ExtraForbidModel(Model):
    model_config = ConfigDict(extra="forbid")
