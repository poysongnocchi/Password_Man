from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker
import hashlib



url = URL.create(
    drivername="postgresql",
    username="jabujabu",
    host="localhost",
    database="password_manager"
)

engine = create_engine(url)

connection = engine.connect()

Base = declarative_base()



class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    username = Column(String(100), nullable=False, unique=True)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    content = Column(Text)
   

class Service(Base):
    __tablename__ = "services"

    id = Column(Integer(), primary_key=True)
    name = Column(String(100), nullable=False, unique=True)

class Password(Base):
    __tablename__ = 'passwords'

    id = Column(Integer(), primary_key=True)
    joined = Column(DateTime(), default=datetime.now)
    user_id = Column(Integer(), ForeignKey('users.id'))
    service_id = Column(Integer(), ForeignKey('services.id'))
    password = Column(String(128), nullable=False) 

    # user = relationship('User', backref='services')



# Drop existing tables if any
Base.metadata.drop_all(engine)

Base.metadata.create_all(engine)





ahmed = User(
    username="Ahmedd",
    password="Mohammed",
    email="ahmed_email@gmail.com"
)


ezekiel = User(
    username="ezekiel",
    password="Mohammed",
    email="ahmed_email@gmail.com"
)

facebook = Service(
    name="facebook"
)



Session = sessionmaker(bind=engine)
session = Session()
session.add(ahmed)
session.add(ezekiel)
session.add(facebook)
session.commit()


ahmed_facebook = Password(
    user_id=ahmed.id,
    service_id=facebook.id,
    password="bananas"
)

ezekiel_facebook = Password(
    user_id=ezekiel.id,
    service_id=facebook.id,
    password="ezekiel12345"
)


session.add(ahmed_facebook)
session.add(ezekiel_facebook)
session.commit()



print(ahmed.id)







# SELECT * 
# FROM user_service us
# JOIN users u ON u.id = us.user_id;
