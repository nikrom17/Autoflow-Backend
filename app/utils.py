from flask import jsonify

def default_response(schemas):
    response = {}
    for query_result, identifier in schemas:
        allIds = []
        byId = {}
        for item in query_result:
            allIds.append(item.id)
            byId[item.id] = item.format()
        response[identifier] = {
            "allIds": allIds,
            "byId": byId,
        }
    return jsonify({
        'success': True,
        'code': 200,
        **response
    })