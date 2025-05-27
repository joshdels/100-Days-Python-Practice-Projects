from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests



app = Flask(__name__)
Bootstrap5(app)

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Movie.db"

class EditForm(FlaskForm):
    rating = FloatField('Rating', validators=[DataRequired()])
    review = StringField('Review', validators=[DataRequired()])
    submit = SubmitField('Done') 
    
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class = Base)
db.init_app(app)


# CREATE DB
class Movies(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True)
    year: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String(250))
    rating: Mapped[float] = mapped_column(Float)
    ranking: Mapped[int] = mapped_column(Integer)
    review: Mapped[str] = mapped_column(String(250))
    img_url: Mapped[str] = mapped_column(String(250), nullable=True)

# CREATE TABLE
with app.app_context():
    db.create_all()

# # ADD Data for test
#     second_movie = Movies(
#         title="China Wars",
#         year=1950,
#         description="War on china is devastitating",
#         rating=5.3,
#         ranking=3,
#         review="Hmmm mid tier.",
#         img_url="https://i0.wp.com/asiatimes.com/wp-content/uploads/2020/05/China-War-Propaganda-Poster.jpg?fit=1400%2C900"
#     )
    
#     db.session.add(second_movie)
#     db.session.commit()
    
@app.route("/")
def home():
    # all_movies = db.session.query(Movies).all() --> tinapulan, pero same gihapon 
    result = db.session.execute(db.select(Movies))
    all_movies = result.scalars().all()
    
    return render_template("index.html", movies = all_movies)

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    form = EditForm()
    movie = db.session.execute(db.select(Movies).where(Movies.id == id)).scalar()
    if form.validate_on_submit():
        movie.review = form.review.data
        movie.rating = form.rating.data
        db.session.commit()
        return redirect(url_for('home'))
    
    return render_template("edit.html", form=form)

@app.route("/delete/<int:id>")
def delete(id):
    movie = db.session.execute(db.select(Movies).where(Movies.id == id)).scalar()
    db.session.delete(movie)
    db.session.commit()
    
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
    
## Going edit table na josh! yeye hahha update
