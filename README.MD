# R1

The problem being addressed by building this particular app is the challenge of managing and remembering passwords for various online services. In today's digital age, people often have accounts on multiple platforms, each requiring a unique password for security purposes. However, remembering all these passwords can be cumbersome and prone to forgetting or using weak passwords.

The app aims to solve this problem by providing a secure platform where users can store their service credentials (such as usernames or emails) along with the associated passwords. This way, users can easily access their passwords when needed without having to remember them all or resorting to unsafe practices like using the same password for multiple accounts.

Key aspects of the problem being addressed include:

**Password Management:** Many users struggle with managing and remembering passwords for various online services. This app provides a centralized solution for storing and accessing passwords securely.

**Security:** Using unique and strong passwords for each service is crucial for online security. By storing passwords in a secure app, users can avoid using weak or easily guessable passwords.

**Convenience:** Having quick access to stored passwords makes it convenient for users to log in to their accounts without the hassle of searching for or resetting passwords.

**Data Integrity:** Ensuring that stored passwords are encrypted and protected from unauthorized access is essential for maintaining data integrity and user privacy.

Overall, the app aims to simplify password management, enhance security, and provide a user-friendly experience for managing online service credentials.


# R2

The need for a password management app arises from several factors that make it a significant problem that needs solving:

**Security Concerns:** With the increasing number of online accounts and services that people use daily, maintaining strong and unique passwords for each service is critical for cybersecurity. Weak or reused passwords are a significant risk factor for unauthorized access and data breaches.

**Human Memory Limitations:** Remembering multiple complex passwords can be challenging for most people. As passwords become more complex (as recommended for security), the difficulty of remembering them also increases.

**Avoiding Password Reuse:** Many users resort to using the same password across multiple accounts due to the difficulty of remembering multiple passwords. This practice is highly insecure because if one account is compromised, all other accounts with the same password become vulnerable.

**Efficiency:** A password management app provides a convenient and efficient way to store, organize, and access passwords across different devices. It eliminates the need to memorize or write down passwords, reducing the risk of losing or forgetting them.

**Encouraging Strong Password Practices:** By providing a secure platform for storing passwords, password management apps can encourage users to create and use strong, unique passwords for each service, thereby enhancing overall cybersecurity.

Overall, the need for a password management app stems from the complexity of modern digital life, the importance of cybersecurity, and the limitations of human memory in managing multiple strong passwords effectively.


# R3

The choice of using a relational database system like PostgreSQL for the password management API can be attributed to several reasons:

**Data Structure:** Relational databases are well-suited for structured data with clear relationships between entities, such as storing user credentials (username, password) and associating them with specific services. This structured approach simplifies data management and querying.

**ACID Compliance:** Relational databases like PostgreSQL ensure ACID (Atomicity, Consistency, Isolation, Durability) properties, providing transactional consistency and data integrity. This is crucial for handling sensitive data like passwords securely.

**Query Flexibility:** SQL (Structured Query Language) provides a powerful and standardized way to query relational databases. It allows complex operations like joins, filtering, sorting, and aggregation, which are essential for retrieving and managing data in a password management system.

**Data Integrity:** Relational databases support constraints (e.g., primary keys, foreign keys, unique constraints) and data validation rules, ensuring data integrity and preventing inconsistencies.

**Scalability:** While relational databases may have traditionally been associated with vertical scalability (adding more resources to a single server), modern RDBMS like PostgreSQL also support horizontal scalability through techniques like sharding, replication, and clustering.

However, relational databases also have some drawbacks compared to other database systems:

**Schema Rigidity:** Relational databases require a predefined schema, which can be rigid and less flexible compared to NoSQL databases that offer schemaless or flexible schemas. This can make it challenging to adapt to changing data requirements.

**Performance:** In certain use cases, especially when dealing with large-scale data or high-throughput applications, NoSQL databases or specialized databases (e.g., time-series databases, graph databases) may offer better performance and scalability than traditional relational databases.

**Complexity:** Managing complex relationships and joins in relational databases can sometimes lead to complex SQL queries and performance bottlenecks, especially for applications with highly interconnected data.

**Scaling Challenges:** While modern RDBMS like PostgreSQL support horizontal scaling techniques, scaling relational databases across multiple nodes in a distributed environment can be more challenging compared to some NoSQL databases designed for distributed architectures from the ground up.

Overall, the choice of using a relational database system like PostgreSQL for the password management API depends on factors such as data structure, transactional requirements, query flexibility, and the specific use case of the application.



# R4

Object-Relational Mapping (ORM) offers several key functionalities and benefits that simplify database interactions and enhance application development. Here are the key functionalities and benefits of using an ORM:

**Object-Table Mapping:** Maps OOP language objects to database tables, simplifying database interactions using OOP concepts like classes and objects.

**Abstraction Layer:** Eliminates manual SQL queries by providing a high-level abstraction layer between application code and the database.

**Automatic Schema Generation:** Generates database schemas based on object models, reducing manual schema management.

**CRUD Operations:** Provides built-in methods for Create, Read, Update, and Delete operations on database entities.

**Querying:** Offers query languages or builders for writing complex database queries using language constructs.

**Transaction Management:** Handles transactions for data consistency and rollback capabilities.

**Data Validation:** Includes validation mechanisms to enforce data integrity before saving to the database.

**Relationship Mapping:** Supports defining and managing relationships between entities.

**Cross-Database Compatibility:** Works with multiple database systems seamlessly.

**Code Reusability and Maintainability:** Encapsulates database logic for modular, maintainable, and scalable codebases.

In summary, ORM simplifies database interactions, reduces development time, improves code quality, and enhances overall application scalability and maintainability by providing a high-level abstraction layer for working with databases in object-oriented applications.

# R5

## Endpoints documentation:

# 1 

~~~
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

~~~

Endpoint: /create_service
Description:
Creates a new service in the password management system.

HTTP Request Verb:
POST

Required Data:
name: string (required) - The name of the service to be created.
Expected Response Data:
Upon successful creation, the endpoint returns a success message in JSON format:

~~~
{
    "message": "Service created successfully"
}
In case of an error or missing data, the endpoint returns an error message in JSON format:
~~~

In case of an error or missing data, the endpoint returns an error message in JSON format:

~~~
{
    "error": "Error message describing the issue"
}
~~~
Authentication Method:
This endpoint does not require authentication.

# 2

~~~
@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    username = data.get('username')

    if not email or not password or not username:
        return jsonify({'error': 'email, password, and username are required'}), 400

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
~~~

Endpoint: /create_user
Description:
Creates a new user account in the password management system.

HTTP Request Verb:
POST

Required Data:
email: string (required) - The email address of the user.
password: string (required) - The password for the user account.
username: string (required) - The username for the user account.
Expected Response Data:
Upon successful creation, the endpoint returns a success message in JSON format:

~~~
{
    "message": "User created successfully"
}
~~~

In case of missing or incomplete data, the endpoint returns an error message in JSON format:

~~~
{
    "error": "email, password, and username are required"
}
~~~
Authentication Method:
This endpoint does not require authentication.

# 3

~~~
@app.route('/create_password', methods=['POST'])
def create_password():
    data = request.get_json()
    service_id = data.get('service_id')
    user_id = data.get('user_id')
    password = data.get('password')

    if not service_id or not user_id or not password:
        return jsonify({'error': 'service_id, user_id, and password are required'}), 400

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

~~~

Endpoint: /create_password
Description:
Creates a new password entry for a user and service in the password management system.

HTTP Request Verb:
POST

Required Data:
service_id: number (required) - The ID of the service associated with the password.
user_id: number (required) - The ID of the user for whom the password is being created.
password: string (required) - The password to be stored.
Expected Response Data:
Upon successful creation, the endpoint returns a success message in JSON format:

~~~
{
    "message": "Password created successfully"
}
~~~
In case of missing or incomplete data, the endpoint returns an error message in JSON format:

~~~
{
    "error": "service_id, user_id, and password are required"
}
~~~
Authentication Method:
This endpoint does not require authentication.

# 4
~~~
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
~~~

Endpoint: /retrieve_passwords
Description:
Retrieves all stored passwords associated with a user in the password management system.

HTTP Request Verb:
POST

Required Data:
user_id: number (required) - The ID of the user whose passwords are to be retrieved.
Expected Response Data:
Upon successful retrieval, the endpoint returns a JSON object containing an array of password entries with their associated service names:

~~~
{
    "passwords": [
        {
            "service_name": "Facebook",
            "password": "password123"
        },
        {
            "service_name": "Google",
            "password": "securepass"
        },
        ...
    ]
}
~~~
In case of missing or incomplete data (user_id), the endpoint returns an error message in JSON format:

~~~
{
    "error": "User ID is required"
}
~~~
Authentication Method:
This endpoint does not require authentication.

# 5 
~~~
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
~~~

Endpoint: /get_services
Description:
Retrieves all available services in the password management system.

HTTP Request Verb:
GET

Required Data:
This endpoint does not require any data in the request.

Expected Response Data:
Upon successful retrieval, the endpoint returns a JSON object containing an array of service entries:

~~~
{
    "services": [
        {
            "id": 1,
            "name": "Facebook"
        },
        {
            "id": 2,
            "name": "Google"
        },
        ...
    ]
}
~~~

In case of an error during retrieval, the endpoint returns an error message in JSON format:

~~~
{
    "error": "Error message describing the issue"
}
~~~
Authentication Method:
This endpoint does not require authentication.        


# 6

~~~
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
~~~

Endpoint: /get_users
Description:
Retrieves all users registered in the password management system.

HTTP Request Verb:
GET

Required Data:
This endpoint does not require any data in the request.

Expected Response Data:
Upon successful retrieval, the endpoint returns a JSON object containing an array of user entries:

~~~
{
    "users": [
        {
            "id": 1,
            "email": "user1@example.com",
            "username": "user1"
        },
        {
            "id": 2,
            "email": "user2@example.com",
            "username": "user2"
        },
        ...
    ]
}
~~~

In case of an error during retrieval, the endpoint returns an error message in JSON format:

~~~
{
    "error": "Error message describing the issue"
}
~~~
Authentication Method:
This endpoint does not require authentication.


# R6

### Third party services that will be used for the development of the aplication:


**Flask:** A micro web framework for Python used to build web applications.
**request:** A Flask module for handling HTTP requests, accessing request data, and interacting with client requests.
**render_template:** A Flask module for rendering HTML templates, allowing dynamic generation of web pages.
**jsonify:** A Flask module for converting Python data structures into JSON format, commonly used for HTTP responses.
**re:** Python's built-in module for regular expressions, used for pattern matching and string manipulation tasks.
**hashlib:** Python's built-in module for secure hashing algorithms, often used for password hashing and data integrity checks.
**uuid:** Python's built-in module for generating universally unique identifiers (UUIDs), useful for creating unique keys or identifiers.
**SQLAlchemy:** A Python SQL toolkit and ORM for database operations, allowing interaction with databases using Python objects and queries.
**URL:** SQLAlchemy module for constructing database connection URLs, necessary for connecting to databases.
**create_engine:** SQLAlchemy function for creating database engine instances, managing database connections, and executing SQL commands.
**Column:** SQLAlchemy class for defining column properties in database tables, such as data types and constraints.
**Integer, String, DateTime, Text:** SQLAlchemy data types for defining column types in database tables, representing integers, strings, date/time values, and text.
**ForeignKey:** SQLAlchemy class for defining foreign key relationships between database tables, establishing relationships and constraints.
**declarative_base:** SQLAlchemy base class used for defining database models (classes) that represent database tables, facilitating ORM usage.
**sessionmaker:** SQLAlchemy function for creating database sessions, enabling interaction with the database and transaction management.
**relationship, backref:** SQLAlchemy functions for defining relationships between database models, such as one-to-many or many-to-many relationships, and creating back-references between related models.


# ERD needs modification

# R7


# R8


# R9


# R10