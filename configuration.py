from routes.home import home_route
from routes.cliente import cliente_route
from routes.auth import auth_route
from database.database import db
from database.models.cliente import Cliente
from flask_jwt_extended import JWTManager



def configure_all(app):
    configure_routes(app)
    configure_db()
    configure_jwt(app)


def configure_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(cliente_route, url_prefix="/clientes")
    app.register_blueprint(auth_route, url_prefix="/auth")


def configure_db():
    db.connect()
    db.create_tables([Cliente])


def configure_jwt(app):
    app.jwt = JWTManager(app)
    app.config['JWT_SECRET_KEY'] = 'super-secret'