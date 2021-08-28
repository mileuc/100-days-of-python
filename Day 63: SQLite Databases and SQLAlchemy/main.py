###################################### SQLite Databases ###############################################
# 1. import the sqlite3 module
import sqlite3

# 2. create a connection to a new database (if the database does not exist then it will be created)
# 3. run main.py and you should see a new file appear in PyCharm called books-collection.db
# db = sqlite3.connect("books-collection.db")

# 4. create a cursor which will control and modify our SQLite database
# cursor = db.cursor()
# 5. create a table called books in our database
# 10. comment out the previous line of code where you are created the table called books to avoid an error
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY,"
#                " title varchar(250) NOT NULL UNIQUE,"
#                " author varchar(250) NOT NULL,"
#                " rating FLOAT NOT NULL)")

# 6/7/8. run code. to view database, download DB Browser and use it to open the database

# 9. create a new entry in our books table and commit the changes to our database
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

# 11. close down the database in DB Browser by clicking Close Database
# 12. run the code in main.py and re-open the database in DB Browser to see the updated books table

###################################### SQLACADEMY ###############################################
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
# will silence the deprecation warning in the console
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# baseclass for all your models is called db.Model. it’s stored on the SQLAlchemy instance you have to create
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=False, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f"<Book {self.title}>'"


db.create_all()  # creates all tables

# create record
new_book = Book(id=1, title="Harry Potter", author="J.K. Rowling", rating=9.3)
db.session.add(new_book)
db.session.commit()
