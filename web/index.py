from flask import Flask, render_template
from API.v1.views import app_views
from API.v1.views.config import Config
from models import storage
from models.amenity import Amenity
from models.properties import Property
from models.state import State
from flask_mail import Mail  # Import Mail class from flask_mail

app = Flask(__name__)
app.register_blueprint(app_views)
app.config.from_object(Config)

mail = Mail(app)

# Define routes
@app.route('/')
def index():
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    properties = storage.all(Property).values()
    properties = sorted(properties, key=lambda k: k.name)

    return render_template('index.html',
                           states=st_ct,
                           amenities=amenities,
                           properties=properties)

if __name__ == "__main__":
    app.run(debug=True)
