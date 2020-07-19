import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from auth import AuthError, requires_auth
from models import setup_db, db, Location, Client, Delivery

app = Flask(__name__)
setup_db(app)
CORS(app)


# ROUTES
@app.route('/clients', methods=['GET'])
# @requires_auth('')
def get_clients():
    clients = Client.query.outerjoin(Location, Client.id == Location.client_id).outerjoin(Delivery, Client.id == Delivery.client_id).all()
    # clients2 = Client.query.all()
    for client in clients:
        print(client)
    return jsonify({
        'success': True,
        'code': 200,
        # 'clients': clients,
    })

@app.route('/locations/<int:client_id>', methods=['GET'])
# @requires_auth('')
def get_client_locations(client_id):
    query = Location.query.join(Client).filter(Location.client_id==client_id).all()
    locations = [location.format() for location in query]
    print(len(query))
    for location in locations:
        print(location)
    return jsonify({
        'success': True,
        'code': 200,
        'locations': locations,
    })


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404


@app.errorhandler(403)
def forbidden(error):
    return jsonify({
        "success": False,
        "error": 403,
        "message": "resource forbidden"
    }), 403


@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": error.description
    }), 400


@app.errorhandler(401)
def unauthorized(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": error.description
    }), 401
