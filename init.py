from flask import Flask, request, render_template, jsonify
import re
import hashlib
import uuid
from sqlalchemy.engine import URL
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import declarative_base
from datetime import datetime
from sqlalchemy.orm import sessionmaker, relationship, backref
import hashlib


# Set up the database
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

# Create tables in the database
Base.metadata.create_all(engine)

# Create a session maker
Session = sessionmaker(bind=engine)

app = Flask(__name__)

# Regular expression pattern for validating email addresses
EMAIL_REGEX = re.compile(r'^[\w\.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

# Function to hash the password with a unique salt
def hash_password(password, salt=None):
    if salt is None:
        salt = uuid.uuid4().hex  # Generate a random salt
    hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
    return hashed_password, salt

@app.route('/', methods=['GET'])
def hello_world():
    return 'hello world'


# Route to create a new service
@app.route('/create_service', methods=['POST'])
def create_service():
    data = request.get_json()
    name = data.get('name')

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    session = Session()
    try:
        new_service = Service(name=name)
        session.add(new_service)
        session.commit()
        return jsonify({'message': 'Service created successfully'}), 200
    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()

@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    username = data.get('username')

    if not email or not password or not username:
        return jsonify({'error': 'Email, password, and username are required'}), 400

    session = Session()
    try:
        new_user = User(email=email, password=password, username=username)
        session.add(new_user)
        session.commit()
        return jsonify({'message': 'User created successfully'}), 200
    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()

@app.route('/create_password', methods=['POST'])
def create_password():
    data = request.get_json()
    service_id = data.get('service_id')
    user_id = data.get('user_id')
    password = data.get('password')

    if not service_id or not user_id or not password:
        return jsonify({'error': 'Service ID, user ID, and password are required'}), 400

    session = Session()
    try:
        new_password = Password(service_id=service_id, user_id=user_id, password=password)
        session.add(new_password)
        session.commit()
        return jsonify({'message': 'Password created successfully'}), 200
    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()

@app.route('/retrieve_passwords', methods=['POST'])
def retrieve_passwords():
    data = request.get_json()
    user_id = data.get('user_id')
    
    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400

    session = Session()
    try:
        # Perform a SQL join to retrieve passwords along with the associated service name
        passwords = session.query(Password, Service.name).\
            filter(Password.user_id == user_id).\
            join(Service, Password.service_id == Service.id).all()

        # Extract relevant information from the joined data
        password_data = [{'service_name': service_name, 'password': password.password} 
                         for password, service_name in passwords]

        return jsonify({'passwords': password_data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()
@app.route('/get_services', methods=['GET'])
def get_services():
    session = Session()
    try:
        services = session.query(Service).all()
        service_data = [{'id': service.id, 'name': service.name} for service in services]
        return jsonify({'services': service_data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()

@app.route('/get_users', methods=['GET'])
def get_users():
    session = Session()
    try:
        # Retrieve all users from the database
        users = session.query(User).all()

        # Extract relevant information from the users
        user_data = [{'id': user.id, 'email': user.email, 'username': user.username} for user in users]

        return jsonify({'users': user_data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()
        
if __name__ == '__main__':
    app.run(debug=True)

# Whats next
    # encrypt the passwords when the enter the database and decrypt them when the user asks for them
    # add some user authentication so a user cant retrieve a different users passwords
    # update the "An ERD for your app"


### What routes do we need
    
# POST Create Service
    # name: string

# POST Create User
    # email: string
    # password: string
    # username: string

# GET Get Services
    
# POST Create Password
    # service_id: number
    # user_id: number
    # password: string

# POST Retrieve Passwords
    # user_id: string
    # > service name
    # > password



## NOTE we are not doing any user authentication with this design. 
# If we were to do user auth, we would need to have a login route
# POST Login
    # username
    # password
    # > Auth Token (expiry of 24 hours)

    

    
# If the code starts with 2 its all good
# If the code starts with 4 the user fucked up
# If the code starts with 5 the server fucked up













