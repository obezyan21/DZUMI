from sqlalchemy import String, ForeignKey, Text, Integer, Boolean, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

from .base import Base

if TYPE_CHECKING:
    from .object import Object
    from .user import User
    from .document import Document
    from .order_items import OrderItem


class Order(Base):

    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    object_id: Mapped[int] = mapped_column(ForeignKey('objects.id', ondelete="CASCADE"))
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id', ondelete="CASCADE"))
    system_type: Mapped[str] = mapped_column(String(70))  # enum
    order_status: Mapped[str] = mapped_column(String(50))  # enum
    total_price: Mapped[float] = mapped_column(Numeric(10, 2))
    agreed: Mapped[str] = mapped_column(String(50))
    priority: Mapped[str] = mapped_column(String(50))  # enum
    description: Mapped[str] = mapped_column(Text)
    comment: Mapped[str] = mapped_column(Text)
    decline_reason: Mapped[str] = mapped_column(String(255))

    # связи
    document: Mapped[list["Document"]] = relationship(back_populates="order")
    object: Mapped["Object"] = relationship(back_populates="order")
    user: Mapped["User"] = relationship(back_populates="order")
    order_item: Mapped[list["OrderItem"]] = relationship(back_populates="order")
