from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


url = 'sqlite:///raspis.db'
Base = declarative_base()
engine = create_engine(url=url)
Session = sessionmaker(bind=engine)
session = Session()


class Raspis(Base):
    __tablename__ = 'schedule'

    id = Column(Integer, autoincrement=True, primary_key=True)
    date = Column(String)
    para = Column(String)
    lecture_time = Column(String)
    audience = Column(String)
    lesson = Column(String)
    type_lesson = Column(String)
    teacher_name = Column(String)
