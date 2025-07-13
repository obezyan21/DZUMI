from sqlalchemy.orm import Session
from models.object import Object
from .base_dao import BaseDAO


class ObjectDAO(BaseDAO):
    def __init__(self, session):
        super().__init__(session, Object)
