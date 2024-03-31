from flask import Flask, render_template
from API.v1.views import app_views
from models import storage
from models.properties import Property

app = Flask(__name__)
app.register_blueprint(app_views)

# Define routes
@app.route('/')
def index():
    properties = storage.all(Property).values()
    return render_template('index.html', properties=properties)

if __name__ == "__main__":
    app.run(debug=True)
