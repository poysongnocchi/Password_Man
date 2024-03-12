from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker



url = URL.create(
    drivername="postgresql",
    username="jabujabu",
    host="localhost",
    database="password_manager"
)

engine = create_engine(url)

connection = engine.connect()




Base = declarative_base()

class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer(), primary_key=True)
    slug = Column(String(100), nullable=False, unique=True)
    title = Column(String(100), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    content = Column(Text)
    author_id = Column(Integer(), ForeignKey('authors.id'))



class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer(), primary_key=True)
    firstname = Column(String(100))
    lastname = Column(String(100))
    email = Column(String(255), nullable=False)
    joined = Column(DateTime(), default=datetime.now)

    articles = relationship('Article', backref='author')

Base.metadata.create_all(engine)




ezz = Author(
    firstname="Ezzeddin",
    lastname="Abdullah",
    email="ezz_email@gmail.com"
)

ahmed = Author(
    firstname="Ahmed",
    lastname="Mohammed",
    email="ahmed_email@gmail.com"
)

article1 = Article(
    slug="clean-python",
    title="How to Write Clean Python",
    content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    author=ezz
    )

Session = sessionmaker(bind=engine)
session = Session()
session.add(article1)
session.commit()



print(article1.title)





