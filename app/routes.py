from datetime import datetime
from flask import Blueprint, jsonify, abort, request

# from auth import AuthError, requires_auth
from .models import Lead, Opportunity, FunnelStep, OpportunityInfo, Todo
from .utils import default_response

api = Blueprint('api', __name__)

# ROUTES

# ---------------------------------------------------------------------------- #
# Opportunities
# ---------------------------------------------------------------------------- #

@api.route('/opportunities', methods=['GET'])
def get_opportunities():
    try:
        query_result = Opportunity.query.all()
        opportunities = [opportunity.format() for opportunity in query_result]
        return default_response(opportunities, 'opportunities')
    except Exception as e:
        abort(500)

# ---------------------------------------------------------------------------- #
# Opportunity Info
# ---------------------------------------------------------------------------- #

@api.route('/opportunity-info', methods=['GET'])
def get_opportunity_infos():
    try:
        query_result = OpportunityInfo.query.all()
        opportunities_info = [opportunity_info.format() for opportunity_info in query_result]
        return default_response(opportunities_info, 'opportunities')
    except Exception as e:
        print(e)
        abort(500)

@api.route('/opportunity-info/<int:opportunity_info_id>', methods=['GET'])
def get_opportunity_info(opportunity_info_id):
    try:
        opportunity_info = OpportunityInfo.query.get(opportunity_info_id)
        if not opportunity_info:
            abort(404)
        return default_response([opportunity_info.format()], 'opportunities')
    except Exception as e:
        abort(500, e)

# ---------------------------------------------------------------------------- #
# Funnel Steps
# ---------------------------------------------------------------------------- #

@api.route('/funnel-steps', methods=['GET'])
def get_funnel_steps():
    try:
        query_result = FunnelStep.query.all()
        funnel_steps = [funnel_step.format() for funnel_step in query_result]
        return default_response(funnel_steps, 'funnelSteps')
    except Exception:
        abort(500)

@api.route('/funnel-steps/<int:funnel_step_id>', methods=['GET'])
def get_funnel_step(funnel_step_id):
    try:
        funnel_step = FunnelStep.query.get(funnel_step_id)
        if not funnel_step:
            abort(404)
        return default_response([funnel_step.format()], 'funnelSteps')
    except Exception as e:
        abort(500, e)

# ---------------------------------------------------------------------------- #
# Leads
# ---------------------------------------------------------------------------- #

@api.route('/leads', methods=['GET'])
def get_leads():
    try:
        query_result = Lead.query.all()
        leads = [lead.format() for lead in query_result]
        return default_response(leads, 'leads')
    except Exception as e:
        abort(500, e)

@api.route('/leads/<int:lead_id>', methods=['GET'])
def get_lead(lead_id):
    try:
        lead = Lead.query.get(lead_id)
        if not lead:
            abort(404)
        return default_response([lead.format()], 'leads')
    except Exception as e:
        abort(500, e)
        

@api.route('/leads/add', methods=['POST'])
def add_lead():
    try:
        payload = request.get_json()
        lead = Lead(
            address= payload["address"],
            chanceToConvert=0.15,
            dateCreated=datetime.now(),
            email=payload["email"],
            funnelStepId=payload["funnelStepId"],
            lastContact=datetime.now(),
            name=payload["name"],
            phone=payload["phone"],
            status=payload["status"]
        )
        payload = request.get_json()
        
        if not lead:
            abort(404)
        return default_response([lead.format()], 'leads')
    except Exception as e:
        abort(500, e)
        
# ---------------------------------------------------------------------------- #
# Todos
# ---------------------------------------------------------------------------- #

@api.route('/todos', methods=['GET'])
def get_todos():
    try:
        query_result = Todo.query.all()
        todos = [todo.format() for todo in query_result]
        return default_response(todos, 'todos')
    except Exception as e:
        abort(500, e)
        
@api.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    try:
        todo = Todo.query.get(todo_id)
        if not todo:
            abort(404)
        return default_response([todo.format()], 'todos')
    except Exception as e:
        abort(500, e)


@api.errorhandler(500)
def server_error(error):
    return jsonify({
        "message": "Server Error",
        "code": 500,
        "description": str(error),
        "success": False,
    }), 500
    
    
@api.errorhandler(404)
def not_found():
    return jsonify({
        "message": "Not Found",
        "code": 404,
        "description": "We couldn't find what you were looking for",
        "success": False,
    }), 404


@api.errorhandler(403)
def forbidden():
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
def unauthorized():
    return jsonify({
        "message": "Unauthorized",
        "code": 401,
        "description": "Please login",
        "success": False,
    }), 401
