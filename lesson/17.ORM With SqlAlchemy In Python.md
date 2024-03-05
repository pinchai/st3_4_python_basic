# Flask SQLAlchemy

Using raw SQL in the Flask Web application to perform CRUD operations on the database can be cumbersome.

Instead, SQLAlchemy, the Python Toolkit is a powerful OR Mapper, which provides application developers with the full
functionality and flexibility of SQL.

Flask-SQLAlchemy is a Flask extension that adds support for SQLAlchemy to the Flask application.


**What is ORM?**

ORM is short for Object Relation Mapping (sometimes Object Relationship Mapping).

Most programming language platforms are object-oriented.
the data in the RDBMS server is stored in tables.
Object-relational mapping is a technique that maps object parameters to the structure of a layer RDBMS table. The ORM API provides a way to perform CRUD operations without writing raw SQL statements.


**_Setup_**

In this section, we will study the ORM technology of Flask-SQLAlchemy and build a small web application.

**Step 1 -** Install the Flask-SQLAlchemy extension.

``pip install flask-sqlalchemy``

**_Step 2 -_** You need to import the SQLAlchemy class from this module.

``from flask_sqlalchemy import SQLAlchemy``

**_Step 3_ - ** Now create a Flask application object and set the URI for the database to use.

````
#SQLite
app = Flask (__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
````

````
#SQLite
app = Flask (__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://user:password@host/database'
````


**_Step 4_** - then use the application object as a parameter to create an object of class SQLAlchemy.The object contains an auxiliary function for the ORM operation.It also provides a parent Model class that uses it to declare a user-defined model.In the code snippet below, the studients model is created.

````
db = SQLAlchemy(app)
class students(db.Model):
   id = db.Column('student_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))  
   addr = db.Column(db.String(200))
   pin = db.Column(db.String(10))

def __init__(self, name, city, addr,pin):
   self.name = name
   self.city = city
   self.addr = addr
   self.pin = pin
````


**_Step 5_** - To create/use the database mentioned in the URI, run the create_all() method.

````
with app.app_context():
    # db.drop_all()
    db.create_all()
    db.session.commit()

if __name__ == '__main__':
    app.run()
````


##❇️ CRUD
SQLAlchemy’s Session object manages all persistence operations for ORM objects.

The following session method performs CRUD operations:


**1. Read or Retrieve**

````
students = students.query.all()
````

**2. Create**

````
student = students(request.form['name'], request.form['city'],
    request.form['addr'], request.form['pin'])
 
 db.session.add(student)
 db.session.commit()
````

**3. Update**

````
student = students.query.get(id)
student.email = 'my_new_email@example.com'
db.session.commit()

OR

student = students.query.filter_by(username='admin').first()
student.email = 'my_new_email@example.com'
db.session.commit()
````

**4. Delete**

````
student = students.query.get(id)
db.session.delete(data)
db.session.commit()
````

