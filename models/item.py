from sqlalchemy import String, Text, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, TYPE_CHECKING

from .base import Base

if TYPE_CHECKING:
    from .trusted_supplier import TrustedSupplier
    from .order_items import OrderItem

class Item(Base):
    
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    provider_id: Mapped[Optional[int]] = mapped_column(Integer)
    article_number: Mapped[str] = mapped_column(String(100), nullable=False)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    unit_of_measurement: Mapped[Optional[str]] = mapped_column(String(50))
    description: Mapped[Optional[str]] = mapped_column(Text())

    # Связи
    trusted_suppliers: Mapped[list["TrustedSupplier"]] = relationship(back_populates="item")
    order_item: Mapped[list["OrderItem"]] = relationship(back_populates="item")
