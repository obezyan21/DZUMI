from fastapi import Depends
from rest.orders_controller import OrderCreateDto
from dao.orders_dao import OrderDAO
from dao.users_dao import UserDAO
import dependencies

class OrderService:
    def __init__(self, order_dao: OrderDAO, user_dao: UserDAO):
        self.order_dao = order_dao
        self.user_dao = user_dao
    
    async def create_new_order(self, order_dto: OrderCreateDto):
        '''Создает заявку с проверкой пользователя'''
        user = await self.user_dao.get_by_id(order_dto.user_id)
        if not user:
            raise ValueError("Пользователь не найден")
        
        order_data = order_dto.model_dump()
        new_order = await self.order_dao.create(order_data)

        return new_order

    async def get_all_orders(self, skip: int, limit: int):  
        '''Пагинация'''
        return await self.order_dao.get_all(skip=skip, limit=limit)
    
    async def accept_order(self, ):
        pass

    async def decline_order(self, ):
        pass