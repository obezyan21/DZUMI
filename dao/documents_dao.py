from sqlalchemy.orm import Session
from models.documents import Document
from .base_dao import BaseDAO


class DocumentDAO(BaseDAO):
    def __init__(self, session):
        super().__init__(session, Document)
