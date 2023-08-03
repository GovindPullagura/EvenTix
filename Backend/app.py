import os
from flask import Flask
from flask_cors import CORS
from routes.userRoutes import user_router
from routes.movieRoutes import movie_router
from routes.theatreRoutes import theatre_router
from routes.showRoutes import show_router
from routes.eventRoutes import event_router
from routes.venueRoutes import venue_router
from routes.bookingRoutes import booking_router
# Create the Flask application
app = Flask(__name__)

# Configure CORS to allow cross-origin requests
CORS(app)


@app.route("/")
def home():
    return 'Welcome to EvenTix!'


app.register_blueprint(user_router, url_prefix='/users')
app.register_blueprint(movie_router, url_prefix='/movies')
app.register_blueprint(theatre_router, url_prefix='/theatres')
app.register_blueprint(show_router, url_prefix='/shows')
app.register_blueprint(event_router, url_prefix='/events')
app.register_blueprint(venue_router, url_prefix='/venues')
app.register_blueprint(booking_router, url_prefix='/bookings')


# app.py

if __name__ == '__main__':
    app.run(debug=True)
