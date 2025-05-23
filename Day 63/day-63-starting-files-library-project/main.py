from flask import Flask, render_template, request, redirect, url_for
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)

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
    all_books = db.session.query(Book).all()
    return render_template('index.html', books=all_books)


    
@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST': 
        title = request.form['name'] 
        author = request.form['author'] 
        review = request.form['rating'] 
        
        new_book = Book(title=title, author=author, review=review)
        with app.app_context():
            db.session.add(new_book)
            db.session.commit()
            
        return redirect(url_for('home'))
    return render_template('add.html') 

@app.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id): 
    all_books = db.session.query(Book).all()
    
    if request.method == 'POST':
        change_review = request.form['review'] 
        
        book_to_update = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
        book_to_update.review = change_review
        db.session.commit()
        return redirect(url_for('home'))
        
    return render_template('rating.html', id=id, books=all_books)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
    
    if book_to_delete:
        db.session.delete(book_to_delete)
        db.session.commit()
        
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)


# NOTE
# read the document rather than stack over flow or chatgpt, try to read for few minutes before going deep
# i have to breakdown and practice some specifics
