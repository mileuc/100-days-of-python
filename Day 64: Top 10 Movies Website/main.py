from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange, Length
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)
app.config['SECRET_KEY'] = ''
Bootstrap(app)

load_dotenv("./.env")
TMDB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
TMDB_MOVIES_URL = "https://api.themoviedb.org/3/movie"
TMDB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
TMDB_SEARCH_PARAMS = {
    "api_key": TMDB_API_KEY,
    "query": "",
    "include_adult": "false"
}


# 4. create the RateMovieForm and use it to create a Quick Form to be rendered in edit.html.
class RateMovieForm(FlaskForm):
    new_rating = FloatField(label='Your rating out of 10 (e.g. 7.5)',
                            validators=[DataRequired(), NumberRange(min=0.0, max=10.0,
                                                                   message='Please enter a rating between %(min)s and %(max)s.')])
    new_review = StringField(label='Your review',
                             validators=[DataRequired(), Length(max=500, message='Your message is too long.')])
    submit = SubmitField(label='Submit')


# 7. render the add page with a 1-field WTF quick form when you click on the Add Movie button on the Home page
class FindMovieForm(FlaskForm):
    movie_title = StringField(label='Movie title', validators=[DataRequired()])
    add_movie = SubmitField(label='Add Movie')


# 1. create an SQLite database with SQLAlchemy. the database needs to contain a "Movie" Table
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)
db.create_all()


# 2. add a new entry to the database - comment out after initial add:
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# new_movie = Movie(title="Spider-Man 2", year=2004,
#                   description="Peter Parker is dissatisfied with life when he loses his job, the love of his life, Mary Jane, and his powers. Amid all the chaos, he must fight Doctor Octavius who threatens to destroy New York City.",
#                   rating="9.3", ranking=2, review="Probably my favourite movie I ever watched at a theater.",
#                   img_url="https://m.media-amazon.com/images/M/MV5BMzY2ODk4NmUtOTVmNi00ZTdkLTlmOWYtMmE2OWVhNTU2OTVkXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg")
# db.session.add(new_movie)
# db.session.commit()

@app.route("/")
def home():
    # 3. make the code work so that each entry in the database is displayed correctly on the home page
    # all_movies = db.session.query(Movie).all()

    # 11. sort and display the ranking of the movie according to our ratings
    all_movies = Movie.query.order_by(Movie.rating.asc()).all()
    # ascending order: highest rated movie at the bottom
    # use the .count() query on the DB to get the number of movies in the DB and use this value as the starting label
    total_num_of_movies = Movie.query.count()
    for movie in all_movies:
        movie.ranking = total_num_of_movies
        db.session.commit()
        total_num_of_movies -= 1

    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    movie_id = request.args.get("movie_id")
    form = RateMovieForm()
    movie_to_update = Movie.query.filter_by(id=movie_id).first()
    # 5. once the form is submitted and validated, add the updates to the corresponding movie entry in the database
    if form.validate_on_submit():
        movie_to_update.rating = form.new_rating.data
        movie_to_update.review = form.new_review.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", form=form)


# 6. make the delete button work and allow the movie entry to be deleted from the database.
@app.route("/delete", methods=["GET"])
def delete():
    movie_id = request.args.get("movie_id")
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


# 7. render the add page when you click on the Add Movie button on the Home page
@app.route("/add", methods=["GET", "POST"])
def add():
    form = FindMovieForm()
    if form.validate_on_submit():
        # 8. server should receive the movie title when form is submitted
        # 8. use requests library to make a request and search The Movie Database API for all movies that match the title
        TMDB_SEARCH_PARAMS["query"] = form.movie_title.data
        response = requests.get(TMDB_SEARCH_URL, params=TMDB_SEARCH_PARAMS)
        response.raise_for_status()
        movie_results = response.json()["results"]
        return render_template('select.html', results=movie_results)

    return render_template('add.html', form=form)

# 9. use id of the selected movie to hit up another path in the Movie Database API to fetch all data on that movie
@app.route("/find")
def find():
    selected_movie_id = request.args.get("id")
    # movie id is a path param - meaning it needs to be in the URL
    response = requests.get(f"{TMDB_MOVIES_URL}/{selected_movie_id}", params={"api_key": TMDB_API_KEY})
    movie_data = response.json()

    movie_title = movie_data["title"]
    movie_poster_url = f"{TMDB_IMAGE_URL}{movie_data['poster_path']}"
    movie_year = movie_data["release_date"].split('-')[0]
    movie_description = movie_data["overview"]

    new_movie = Movie(
        title=movie_title,
        year=movie_year,
        description=movie_description,
        img_url=movie_poster_url
    )
    db.session.add(new_movie)
    db.session.commit()

    # 10. instead of redirecting to home page after finding the correct film, redirect to the edit.html page.
    return redirect(url_for('edit', movie_id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
