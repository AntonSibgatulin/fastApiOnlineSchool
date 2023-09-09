from service.database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Double


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, autoincrement=True)
    author_id = ForeignKey(Integer, unique=False, nullable=False)
    name = Column(String(50), nullable=False)
    description = Column(String(350), nullable=False)
    blog = Column(String(350), nullable=False)
    type = Column(Integer, nullable=True)
    price = Column(Double, nullable=False)
    time = Column(Integer, nullable=False)
    likes = Column(Integer, name="likes", nullable=False, default=0)
    dislikes = Column(Integer, nullable=False, default=0)
