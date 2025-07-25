from sqlalchemy.orm import Session
from models.document import Document
from .base_dao import BaseDAO
from models.object import Object
from sqlalchemy import select


class DocumentDAO(BaseDAO):
    def __init__(self, session):
        super().__init__(session, Document)

    def get_by_object(self, obj_id: int) -> Object:
        query = select(Document).where(Document.object_id == obj_id)
        docs = self.session.execute(query)

        return docs.scalars().all()
