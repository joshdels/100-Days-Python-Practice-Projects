from flask import Flask, render_template, request, redirect, url_for
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)

all_books = []

class Base(DeclarativeBase):
    pass

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collect.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key =True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    review: Mapped[float] = mapped_column(Float, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST': 
        name = request.form['name'] 
        author = request.form['author'] 
        rating = request.form['rating'] 
        all_books.append({"title":name, "author":author, "rating":rating})
        
        new_book = Book(title=s)
        with app.app_context():
            db.session.add()
        return redirect(url_for('home'))
   
    return render_template('add.html') 


if __name__ == "__main__":
    app.run(debug=True)


# NOTE
# read the document rather than stack over flow or chatgpt, try to read for few minutes before going deep

