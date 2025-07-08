from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, TYPE_CHECKING

from .base import Base

if TYPE_CHECKING:
    from .document import Document

class DocumentAttributes(Base):
    
    __tablename__ = "document_attributes"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    document_id: Mapped[int] = mapped_column(ForeignKey("documents.id", ondelete="CASCADE"))
    attribute_name: Mapped[str] = mapped_column(String(100))
    attribute_value: Mapped[Optional[str]] = mapped_column(Text())
    data_type: Mapped[Optional[str]] = mapped_column(String(50))
    file_type: Mapped[Optional[str]] = mapped_column(String(50))

    # Связи
    document: Mapped["Document"] = relationship(back_populates="attributes")
