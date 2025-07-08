from sqlalchemy import String, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

from .base import Base

if TYPE_CHECKING:
    from .item import Item
    from .order_items import OrderItem

class TrustedSupplier(Base):
    
    __tablename__ = "trusted_supplier"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    item_id: Mapped[int] = mapped_column(ForeignKey("items.id", ondelete="CASCADE"))
    name: Mapped[str] = mapped_column(String(255))
    price: Mapped[float] = mapped_column(Numeric(10, 2))

    # Связи
    item: Mapped["Item"] = relationship(back_populates="trusted_suppliers")
    order_items: Mapped[list["OrderItem"]] = relationship(back_populates="supplier")
