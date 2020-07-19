from flask import jsonify

def default_response(data, identifier):
    allIds = []
    byId = {}
    for item in data:
       allIds.append(item['id'])
       byId[item['id']] = item
    return jsonify({
        'success': True,
        'code': 200,
        identifier: {
            "allIds": allIds,
            "byId": byId,
        },
    })