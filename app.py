from flask import Flask
from config.config import DATABASE_CONNECTION_URI
from routes.Clients_routes import clients_bp
from routes.Locations_routes import locations_bp
from routes.Vehiculos_routes import vehiculos_bp
from models.db import db
from sqlalchemy.exc import OperationalError


app = Flask(__name__)

app.register_blueprint(clients_bp)
app.register_blueprint(locations_bp)
app.register_blueprint(vehiculos_bp)

app.config["SQLALCHEMY_DATABASE_URI"]        = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False



db.init_app(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

with app.app_context():
    from models.client import client
    from models.vehicle import vehicle
    from models.location import location
    # db.drop_all()
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)