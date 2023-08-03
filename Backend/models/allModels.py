from configs.db import dbConnection

userCollection = dbConnection['users']
movieCollection = dbConnection['movies']
showCollection = dbConnection['shows']
theatreCollection = dbConnection['theatres']
eventCollection = dbConnection['events']
venueCollection = dbConnection['venues']
bookingCollection = dbConnection['bookings']

user_schema = {'name': str, 'age': int, 'email': str, 'password': str,
               'membership': str, 'bio': str, 'date_of_birth': str}

movie_schema = {"title": str,
                "description": str,
                "director": str,
                "image": str,
                "cast": [str],
                "run_time": int,
                "genre": str,
                "release_date": str,
                "languages": [str],
                "versions": [str]
                }

show_schema = {'movie_id': str,
               'theatre_id': str,
               'start_time': str,
               'date': str,
               'screen': int}

theatre_schema = {'name': str,
                  'price': int,
                  'location': str,
                  'city': str}

event_schema = {"name": str,
                "image": str,
                "description": str,
                "category": str,
                "date": str,
                "language": str,
                "start_time": str,
                "end-time": str,
                "price": int,
                "venue_id": str}

venue_schema = {"name": str,
                "location": str,
                "city": str,
                "capacity": int
                }
booking_schema = {"user_id": str,
                  "show_id": str,
                  "event_id": str,
                  "tickets_qty": int,
                  "amount": int
                  }


def validate_data(data, schema):
    for key, value_type in schema.items():
        if key not in data or not isinstance(data[key], value_type):
            return False
    return True
