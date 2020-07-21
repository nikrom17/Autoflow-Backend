import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from auth import AuthError, requires_auth
from models import setup_db, db, Location, Client, Delivery
from utils import default_response

app = Flask(__name__)
setup_db(app)
CORS(app)


# ROUTES
@app.route('/clients', methods=['GET'])
# @requires_auth('')
def get_clients():
    try:
        query_result = Client.query.all()
        clients = [client.format() for client in query_result]
        return default_response(clients, 'clients')
    except Exception as e:
        abort(500)


@app.route('/locations/<int:client_id>', methods=['GET'])
# @requires_auth('')
def get_client_locations(client_id):
    try:
        if not Client.query.get(client_id):
            abort(404)
        query_result = Location.query.join(Client).filter(Location.client_id==client_id).all()
        locations = [location.format() for location in query_result]
        return default_response(locations, 'locations')
    except Exception as e:
        abort(500)
    finally:
        raise e

@app.route('/deliveries', methods=['GET'])
# @requires_auth('')
def get_deliveries():
    try:
        query_result = Delivery.query.all()
        deliveries = [delivery.format() for delivery in query_result]
        return default_response(deliveries, 'deliveries')
    except Exception as e:
        abort(500, e)

@app.route('/deliveries/client/<int:client_id>', methods=['GET'])
# @requires_auth('')
def get_client_deliveries(client_id):
    try:
        if not Client.query.get(client_id):
            abort(404)
        query_result = Delivery.query.join(Client).filter(Delivery.client_id==client_id).all()
        deliveries = [delivery.format() for delivery in query_result]
        return default_response(deliveries, 'deliveries')
    except Exception as e:
        abort(500)

@app.route('/deliveries/<int:delivery_id>', methods=['GET'])
# @requires_auth('')
def get_delivery(delivery_id):
    try:
        delivery = Delivery.query.get(delivery_id)
        if not delivery:
            abort(404)
        return default_response([delivery.format()], 'deliveries')
    except Exception as e:
        abort(500, e)

@app.errorhandler(500)
def not_found(error):
    return jsonify({
        "message": "Server Error",
        "code": 500,
        "description": str(error),
        "success": False,
    }), 500
    
    
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "message": "Not Found",
        "code": 404,
        "description": "We couldn't find what you were looking for",
        "success": False,
    }), 404


@app.errorhandler(403)
def forbidden(error):
    return jsonify({
        "message": "Forbiden",
        "code": 403,
        "description": "You are not authorized to access the resource",
        "success": False,
    }), 403


@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "code": 400,
        "description": error.message
    }), 400


@app.errorhandler(401)
def unauthorized(error):
    return jsonify({
        "message": "Unauthorized",
        "code": 401,
        "description": "Please login",
        "success": False,
    }), 401
