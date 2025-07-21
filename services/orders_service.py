from fastapi import Depends
from rest.orders_controller import OrderCreateDto
from dao.orders_dao import OrderDAO
from dao.users_dao import UserDAO
import dependencies

class OrderService:
    def __init__(self, order_dao: OrderDAO, user_dao: UserDAO):
        self.order_dao = order_dao
        self.user_dao = user_dao
    
    def create_new_order(self, order_dto: OrderCreateDto):
        pass