from sqlalchemy.orm import Session
from models.document_attribute import DocumentAttribute
from .base_dao import BaseDAO


class DocumentAttribute(BaseDAO):
    def __init__(self, session):
        super().__init__(session, DocumentAttribute)
