from sqlalchemy.orm import Session
from models.trusted_suppliier import TrustedSupplier
from .base_dao import BaseDAO


class TrustedSupplierDAO(BaseDAO):
    def __init__(self, session):
        super().__init__(session, TrustedSupplier)
