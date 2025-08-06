from fastapi import Depends
from rest.user_controller import UserDto
from dao.users_dao import UserDAO
import dependencies

class UserService:
    def __init__(self, user_dao: UserDAO):
        self.user_dao = user_dao

    async def create_user(user_dto: UserDto, user_dao: UserDAO):
        new_user = user_dao.create(user_dto)
        return new_user
    
    async def change_first_name(user_dto: UserDto, user_dao: UserDAO):
        new_first_name = user_dao.update(user_dto.first_name)
        return new_first_name
    
    async def change_phone_number(user_dto: UserDto, user_dao: UserDAO):
        new_phone_number = user_dao.update(user_dto.phone_number)
        return new_phone_number
    
    async def change_email(user_dto: UserDto, user_dao: UserDAO):
        new_email = user_dao.update(user_dto.email)
        return new_email
    
    async def change_role(user_dto: UserDto, user_dao: UserDAO): # тут поправть условие и я чет туплю как допилить ха-ха!
        if user_dto.role_id != "Начальник":
            raise ValueError("Недостаточно прав")
        
        pass