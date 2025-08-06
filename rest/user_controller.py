from fastapi import FastAPI, HTTPException, Depends, Query
from pydantic import BaseModel
from services.user_service import UserService
from dependencies import get_user_service
from typing import List, Optional

app = FastAPI()

class UserDto(BaseModel):
    last_name = [str]
    first_name = [str]
    middle_name = [str]
    email = [str]
    phone_number = [str]
    role_id = [str]

@app.post('')
async def create_new_user(user_dto: UserDto,
                          user_service: UserService = Depends(get_user_service)
):
    user_service.create_user(user_dto)
