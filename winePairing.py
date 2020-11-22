import connexion
from flask_oidc import OpenIDConnect

oidc = OpenIDConnect(connexion.App().app)

def read_one(id):
    print(connexion.request.headers)
    return "this is a pairing"

def read_all():
    return "this is the pairing list"

@oidc.accept_token(True)
def create():
    return "this is where we create"

@oidc.accept_token(True)
def update(id):
    return "this is where we update"

@oidc.accept_token(True)
def delete(id):
    getOidc().accept_token(True)(lambda id: "this is where we delete")
