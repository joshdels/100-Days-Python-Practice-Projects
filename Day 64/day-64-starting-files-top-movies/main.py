from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests
import os

Movie_API = os.environ.get("MOVIE_API")


app = Flask(__name__)
Bootstrap5(app)

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Movie.db"

class EditForm(FlaskForm):
    rating = FloatField('Rating', validators=[DataRequired()])
    review = StringField('Review', validators=[DataRequired()])
    submit = SubmitField('Done') 
    
class AddMovie(FlaskForm):
    title = StringField('Movie Title')
    submit = SubmitField('Add Movie') 
    
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
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250))
    

# CREATE TABLE
with app.app_context():
    db.create_all()
  
@app.route("/")
def home():
    # all_movies = db.session.query(Movies).all() --> tinapulan, pero same gihapon 
    result = db.session.execute(db.select(Movies).order_by(Movies.rating))
    all_movies = result.scalars().all()

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
                 
    return render_template("index.html", movies=all_movies)

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

@app.route("/add", methods=["GET", "POST"])
def add():
    potential_movies = []
    form = AddMovie()
    
    if form.validate_on_submit():
        search = form.title.data
        
        # Get the data
        headers = {
        "accept": "application/json",
            'Authorization': f"Bearer {Movie_API}"
        }

        params = {
        "query": search
        }
        response = requests.get(
            url="https://api.themoviedb.org/3/search/movie",
            params = params,
        headers=headers
        )

        data = response.json()
        
        for row in data['results']:  
            id = row['id']
            title = row['title']
            date = row['release_date']
            
            potential_movies.append({'id': id, 'title':title, 'date':date})   
            
        print(potential_movies)
        return render_template('select.html', movies=potential_movies)
    
    return render_template("add.html", form=form)
    
@app.route("/select/<int:id>") # fix add data tomorrow
def select(id):
    # getting data of selected
    url = f"https://api.themoviedb.org/3/movie/{id}"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {Movie_API}"
    }

    response = requests.get(url, headers=headers)

    # print(response.text)
    data = response.json()

    title = data['original_title']
    img_url = f"https://image.tmdb.org/t/p/w500/{data['poster_path']}"
    year = data['release_date'].split("-")[0]
    description = data['overview']
    
    movie = Movies(
        title=title,
        year=year,
        description=description,
        img_url=img_url

    )
    
    db.session.add(movie)
    db.session.commit()
    
        
    return redirect(url_for('home'))   

if __name__ == '__main__':
    app.run(debug=True)
    
## Going edit table na josh! yeye hahha update
