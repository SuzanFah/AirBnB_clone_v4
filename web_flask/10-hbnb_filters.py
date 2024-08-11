#!/usr/bin/python3
"""
Starts a Flask web application with Flasgger for API documentation
"""

from flask import Flask, render_template
from flasgger import Swagger
from models import storage

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    Displays a HTML page like 6-index.html from static
    ---
    tags:
      - Filters
    parameters:
      - name: state_id
        in: query
        type: string
        description: The ID of the state to filter by
    responses:
      200:
        description: A page with filters
        schema:
          id: Filters
          properties:
            states:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: string
                  name:
                    type: string
            amenities:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: string
                  name:
                    type: string
    """
    states = storage.all('State').values()
    amenities = storage.all('Amenity').values()
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)

@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
