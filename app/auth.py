import os
import logging
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app

logging.basicConfig(filename='access.log', level=logging.INFO)

auth = HTTPBasicAuth()

# credentials
users = {
    os.getenv('ADMIN_USERNAME'): generate_password_hash(os.getenv('ADMIN_PASSWORD'))
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        logging.info(f"Successful login by user: {username}")
        return username
    logging.warning(f"Failed login attempt with username: {username}")
    return None