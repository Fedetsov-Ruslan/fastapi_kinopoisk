from pydantic import BaseModel,  ConfigDict



class UserSchema(BaseModel):
    model_config = ConfigDict(strict=True)
    
    username: str
    password: bytes
