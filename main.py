import json
import time

from flask import Flask, render_template, url_for, redirect
from flask_cors import CORS

import connexion

# Create the application instance
app = connexion.FlaskApp(__name__, specification_dir='./')

CORS(app.app)
app.app.config.update({
    'SECRET_KEY': 'SomethingNotEntirelySecret',
    'OIDC_CLIENT_SECRETS': '../client_secrets.json',
    'OIDC_ID_TOKEN_COOKIE_SECURE': False,
    'OIDC_SCOPES': ["openid", "profile", "email"],
    'OIDC_CALLBACK_ROUTE': '/authorization-code/callback'
})
# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
