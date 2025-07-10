from sqlalchemy.orm import Session
from models.order_item import OrderItem
from .base_dao import BaseDAO


class OrderItem(BaseDAO):
    def __init__(self, session):
        super().__init__(session, OrderItem)
