from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.properties import Property
from os import environ

app = Flask(__name__)

@app.route('/')
def index():
    """ HBNB is alive! """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    places = storage.all(Property).values()
    places = sorted(places, key=lambda k: k.name)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
