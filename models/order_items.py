from sqlalchemy import Integer, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

from .base import Base

if TYPE_CHECKING:
    from .order import Order
    from .item import Item
    from .trusted_supplier import TrustedSupplier

class OrderItem(Base):
    
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))
    item_id: Mapped[int] = mapped_column(ForeignKey("items.id"))
    quantity: Mapped[int] = mapped_column(Integer)
    remained_quantity: Mapped[int] = mapped_column(Integer)
    invoice_price: Mapped[float] = mapped_column(Numeric(10, 2))
    supplier_id: Mapped[int] = mapped_column(ForeignKey("trusted_supplier.id"))

    # Связи
    order: Mapped["Order"] = relationship(back_populates="order_items")
    item: Mapped["Item"] = relationship(back_populates="order_items")
    supplier: Mapped["TrustedSupplier"] = relationship(back_populates="order_items")
