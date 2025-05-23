from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)

# Create Database
class Base(DeclarativeBase):
  pass

# Initialize the database
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///new-books-collection.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

## Create Table of Database
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    review: Mapped[float] = mapped_column(Float, nullable=False)
    
# Creates the schema? what is schema
with app.app_context():
  db.create_all()

# # Writes the record data of the database (CRUD)
#CREATE
with app.app_context():
  new_book = Book(title="Life of Josh", author="Joshua De Leon", review=9.3)
  new_book2 = Book(title="Josh is Josh", author="Joshua De Leon", review=5.3)
  db.session.add_all([new_book, new_book2])
  db.session.commit()
  
# # #READ
# with app.app_context():
#   book = db.session.execute(db.select(Book).where(Book.title))
#   all_books = book.scalar()

  # book = db.session.execute(db.select(Book).where(Book.title == "Joshua De Leon")).scalar()
  
# #UPDATE
# with app.app_context():
#   booK_to_update = db.session.execute(db.select(Book).where(Book.id ==1)).scalar()
#   booK_to_update.title = "Josh goes Hard"
#   db.session.commit()

# #DELETE
# with app.app_context():
#   booK_to_delete = db.session.execute(db.select(Book).where(Book.id ==1)).scalar()
#   db.session.delete(booK_to_delete)
#   db.session.commit()
  
@app.route("/")
def home():
    return "<h1> Hi</h1>"


if __name__ == "__main__":
    app.run(debug=True)