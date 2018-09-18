from flask import Flask
import random
app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    # choose a movie by invoking our new function
    movie = get_random_movie()
    movie2 = get_random_movie()
    # build the response string
    content = "<h1>Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + movie + "</li>"
    content += "</ul>"

    # TODO: pick another random movie, and display it under
    # the heading "<h1>Tommorrow's Movie</h1>"
    content2 = "<h1>Tommorrow's Movie</h1>"
    content2 += "<ul>"
    content2 += "<li>" + movie2 + "</li>"
    content2 += "</ul>"

    return (content + content2)

def get_random_movie():
    # TODO: make a list with at least 5 movie titles
    movies = ['MI1', 'MI2', 'MI3', 'MI4', 'MI5']
    # TODO: randomly choose one of the movies, and return it
    movie_length = len(movies)
    choice = movies[random.randrange(0,movie_length)]
    return choice


app.run()
