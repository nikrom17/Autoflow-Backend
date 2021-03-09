from flask import Blueprint, jsonify, abort

# from auth import AuthError, requires_auth
from .models import Lead, Opportunity, FunnelStep, OpportunityInfo, Todo
from .utils import default_response

api = Blueprint('api', __name__)

# ROUTES
@api.route('/opportunities', methods=['GET'])
def get_opportunities():
    try:
        query_result = Opportunity.query.all()
        opportunities = [opportunity.format() for opportunity in query_result]
        return default_response(opportunities, 'opportunities')
    except Exception as e:
        abort(500)

@api.route('/opportunity-info', methods=['GET'])
def get_opportunity_info():
    try:
        query_result = OpportunityInfo.query.all()
        opportunities_info = [opportunity_info.format() for opportunity_info in query_result]
        return default_response(opportunities_info, 'opportunities')
    except Exception as e:
        print(e)
        abort(500)

@api.route('/funnel-steps', methods=['GET'])
def get_funnel_steps():
    try:
        query_result = FunnelStep.query.all()
        funnel_steps = [funnel_step.format() for funnel_step in query_result]
        return default_response(funnel_steps, 'funnelSteps')
    except Exception as e:
        abort(500)

@api.route('/leads', methods=['GET'])
def get_leads():
    try:
        query_result = Lead.query.all()
        leads = [lead.format() for lead in query_result]
        return default_response(leads, 'leads')
    except Exception as e:
        abort(500)

@api.route('/todos', methods=['GET'])
def get_todos():
    try:
        query_result = Todo.query.all()
        todos = [todo.format() for todo in query_result]
        return default_response(todos, 'todos')
    except Exception as e:
        print(e)
        abort(500)
        
# @api.route('/clients/<int:client_id>', methods=['GET'])
# # @requires_auth('')
# def get_client(client_id):
#     try:
#         client = Opportunity.query.get(client_id)
#         if not client:
#             abort(404)
#         return default_response([client.format()], 'clients')
#     except Exception as e:
#         abort(500, e)

# @api.route('/locations', methods=['GET'])
# # @requires_auth('')
# def get_locations():
#     try:
#         query_result = Lead.query.all()
#         locations = [location.format() for location in query_result]
#         return default_response(locations, 'locations')
#     except Exception as e:
#         abort(500, e)

# @api.route('/locations/client/<int:client_id>', methods=['GET'])
# # @requires_auth('')
# def get_client_locations(client_id):
#     try:
#         if not Opportunity.query.get(client_id):
#             abort(404)
#         query_result = Lead.query.join(Client).filter(Lead.client_id==client_id).all()
#         locations = [location.format() for location in query_result]
#         return default_response(locations, 'locations')
#     except Exception as e:
#         abort(500, e)

# @api.route('/locations/<int:location_id>', methods=['GET'])
# # @requires_auth('')
# def get_location(location_id):
#     try:
#         location = FunnelStep.query.get(location_id)
#         if not location:
#             abort(404)
#         return default_response([location.format()], 'locations')
#     except Exception as e:
#         abort(500, e)

# @api.route('/deliveries', methods=['GET'])
# # @requires_auth('')
# def get_deliveries():
#     try:
#         query_result = FunnelStep.query.all()
#         deliveries = [delivery.format() for delivery in query_result]
#         return default_response(deliveries, 'deliveries')
#     except Exception as e:
#         abort(500, e)

# @api.route('/deliveries/client/<int:client_id>', methods=['GET'])
# # @requires_auth('')
# def get_client_deliveries(client_id):
#     try:
#         if not Opportunity.query.get(client_id):
#             abort(404)
#         query_result = FunnelStep.query.join(Client).filter(Delivery.client_id==client_id).all()
#         deliveries = [delivery.format() for delivery in query_result]
#         return default_response(deliveries, 'deliveries')
#     except Exception as e:
#         abort(500)

# @api.route('/deliveries/<int:delivery_id>', methods=['GET'])
# # @requires_auth('')
# def get_delivery(delivery_id):
#     try:
#         delivery = FunnelStep.query.get(delivery_id)
#         if not delivery:
#             abort(404)
#         return default_response([delivery.format()], 'deliveries')
#     except Exception as e:
#         abort(500, e)

@api.errorhandler(500)
def not_found(error):
    return jsonify({
        "message": "Server Error",
        "code": 500,
        "description": str(error),
        "success": False,
    }), 500
    
    
@api.errorhandler(404)
def not_found(error):
    return jsonify({
        "message": "Not Found",
        "code": 404,
        "description": "We couldn't find what you were looking for",
        "success": False,
    }), 404


@api.errorhandler(403)
def forbidden(error):
    return jsonify({
        "message": "Forbiden",
        "code": 403,
        "description": "You are not authorized to access the resource",
        "success": False,
    }), 403


@api.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "code": 400,
        "description": error.message
    }), 400


@api.errorhandler(401)
def unauthorized(error):
    return jsonify({
        "message": "Unauthorized",
        "code": 401,
        "description": "Please login",
        "success": False,
    }), 401
