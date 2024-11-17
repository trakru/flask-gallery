from flask import Flask
from app.auth import auth
from app.routes import main as main_blueprint

def create_app():
    app = Flask(__name__)
    
    # Init auth
    # auth.init_app(app)
    
    # Register blueprint
    app.register_blueprint(main_blueprint)
    
    return app