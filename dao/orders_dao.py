from sqlalchemy.orm import Session
from models.order import Order
from .base_dao import BaseDAO


class Order(BaseDAO):
    def __init__(self, session):
        super().__init__(session, Order)
