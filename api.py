from fastapi import FastAPI 
import csv 

app = FastAPI()

#Endpoint 'hello world' 

@app.get("/")
def hello(): 
    return {"hello": "world"}

#Klasa movie (model danych) 

class Movie: 
    def __init__(self, movie_id, title, genres):
        self.id = movie_id
        self.title = title
        self.genres = genres
    
    def load_csv(path): 
        with open(path, encoding="utf-8") as f: 
            reader = csv.reader(f) 
            next(reader)
            return list(reader)

    #Endpoint movies 
    @app.get("/movies")
    def get_movies(): 
        rows = load_csv("data/movies.csv")
        movies = []

        for row in rows: 
            movie_id,title,genres = row
            movie = Movie(movie_id, title, genres)
            movies.append(movie.__dict__)

        return movies

class Link: 
    def __init__(self, movie_id, imdb_id, tmdb_id):
        self.movieId = movie_id
        self.imdbId = imdb_id
        self.tmdbId = tmdb_id
    
class Rating: 
    def __init__(self, user_id, movie_id, rating, timestap):
        self.userId = user_id
        self.movieId = movie_id
        self.rating = rating
        self.timestamp = timestamp

class Tag: 
    def __init__(self, user_id, movie_id, tag, timestamp):
        self.userId = user_id
        self.movieId = movie_id
        self.tag = tag
        self.timestamp = timestamp

@app.get("/links")
def get_links():
    rows = load_csv("data/links.csv")
    result = []

    for row in rows: 
        movie_id, imdb_id, tmdb_id = row
        link = Link(movie_id, imdb_id, tmdb_id)
        result.append(link.__dict__)
    return result

@app.get("/ratings")
def get_ratings():
    rows = load_csv("data/ratings.csv")
    result = [] 

    for row in rows:
        user_id,movie_id,rating,timestamp = row
        rating_obj = Rating(user_id, movie_id, rating, timestamp)
        result.append(rating_obj.__dict__)

    return result

@app.get("/tags")
def get_tags():
    rows = load_csv("data/tags.csv")
    result = [] 

    for row in rows:
        user_id, movie_id, tag, timestamp = row
        tag_obj = Tag(user_id, movie_id, tag, timestamp)
        result.append(tag_obj.__dict__)
    
    return result