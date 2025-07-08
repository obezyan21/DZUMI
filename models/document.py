from sqlalchemy import String, ForeignKey, Text, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

from .base import Base

if TYPE_CHECKING:
    from .order import Order
    from .object import Object


class Document(Base):

    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("order.id", ondelete="CASCADE"))
    object_id: Mapped[int] = mapped_column(ForeignKey("object.id", ondelete="CASCADE"))
    file_name: Mapped[str] = mapped_column(String(255))
    base_path: Mapped[str] = mapped_column(String(255))
    file_path: Mapped[str] = mapped_column(Text)
    document_type: Mapped[str] = mapped_column(String(255))

    order: Mapped[list["Order"]] = relationship(back_populates="documents")
    object: Mapped[list["Object"]] = relationship(back_populates="documents")
