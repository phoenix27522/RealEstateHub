from flask import Flask, render_template
from API.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
