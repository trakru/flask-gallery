# app/auth.py

import os
import logging
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

logging.basicConfig(filename='access.log', level=logging.INFO)

auth = HTTPBasicAuth()

# creds
ADMIN_USERNAME = os.getenv('ADMIN_USERNAME')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')

# creds check
if not ADMIN_USERNAME or not ADMIN_PASSWORD:
    raise ValueError("ADMIN_USERNAME and ADMIN_PASSWORD environment variables must be set")

# creds dict
users = {
    ADMIN_USERNAME: generate_password_hash(ADMIN_PASSWORD)
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        logging.info(f"Successful login by user: {username}")
        return username
    logging.warning(f"Failed login attempt with username: {username}")
    return None
