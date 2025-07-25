from fastapi import Depends
from services.orders_service import OrderService
from dao.orders_dao import OrderDAO
from dao.users_dao import UserDAO

# тут мы пишем функции для Depends чтобы не явно/не строго передавать зависимости
# упрощает тесты

def get_order_dao():
    return OrderDAO()

def get_user_dao():
    return UserDAO()

def get_order_service(
    order_dao: OrderDAO = Depends(get_order_dao),
    user_dao: UserDAO = Depends(get_user_dao)
):
    return OrderService(order_dao, user_dao)