from sqlalchemy.orm import Session
from models.user import User
from .base_dao import BaseDAO


class UserDAO(BaseDAO):
    def __init__(self, session):
        super().__init__(session, User)
