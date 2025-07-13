from sqlalchemy.orm import Session
from models.role import Role
from .base_dao import BaseDAO


class RoleDAO(BaseDAO):
    def __init__(self, session):
        super().__init__(session, Role)
