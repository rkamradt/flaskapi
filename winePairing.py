import connexion
from flask_oidc import OpenIDConnect
from flask import (
    make_response,
    abort,
    request
)
from config import (
    db,
    app
)

from models import (
    WinePairing,
    WinePairingSchema,
)

oidc = OpenIDConnect(app)

def read_one(id):
    winePairing = WinePairing.query \
        .filter(WinePairing.id == id) \
        .one_or_none()
    if winePairing is not None:
        winePairing_schema = WinePairingSchema()
        return winePairing_schema.dump(winePairing)
    else:
        abort(404, 'WinePairing not found for Id: {id}'.format(id=id))

def read_all():
    winePairing = WinePairing.query \
        .order_by(WinePairing.id) \
        .all()
    winePairing_schema = WinePairingSchema(many=True)
    return winePairing_schema.dump(winePairing)

@oidc.accept_token(True)
def create():
        schema = WinePairingSchema()
        newWinePairing = schema.load(request.json, session=db.session)
        db.session.add(newWinePairing)
        db.session.commit()
        return schema.dump(newWinePairing), 201

@oidc.accept_token(True)
def update(id):
    updateWinePairing = WinePairing.query.filter(
        WinePairing.id == id
    ).one_or_none()
    if updateWinePairing is None:
        abort(
            404,
            "WinePairing not found for Id: {id}".format(id=id),
        )
    schema = WinePairingSchema()
    update = schema.load(request.json, session=db.session)
    update.id = updateWinePairing.id
    db.session.merge(update)
    db.session.commit()
    data = schema.dump(updateWinePairing)
    return data, 200

@oidc.accept_token(True)
def delete(id):
    winePairing = WinePairing.query.filter(WinePairing.id == id).one_or_none()
    if winePairing is not None:
        db.session.delete(winePairing)
        db.session.commit()
        return make_response(
            "WinePairing {id} deleted".format(id=id), 200
        )
    else:
        abort(
            404,
            "WinePairing not found for Id: {id}".format(id=id),
        )
