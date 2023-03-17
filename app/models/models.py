from sqlalchemy.dialects.postgresql import UUID
import uuid
from ..database import Base
from sqlalchemy import TIMESTAMP, Column, String, Date
from sqlalchemy.sql.expression import  text


class Library_Book(Base):

    __tablename__ = "library_book"

    id = Column(UUID(as_uuid=True), primary_key= True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    published_date = Column(Date, nullable = True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))