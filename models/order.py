from sqlalchemy import String, ForeignKey, Text, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

from .base import Base

if TYPE_CHECKING:
    from .object import Object


class Order(Base):

    __tablename__ = "orders"

    object_id: Mapped[int] = mapped_column(ForeignKey('objects.id', ondelet="CASCADE"))

    # связи
    object: Mapped[list["Object"]] = relationship(back_populates="orders")
