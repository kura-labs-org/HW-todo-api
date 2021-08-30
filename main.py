import helper
from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"


@app.route('/item/new', methods=['POST'])
def add_item():
    #Get item from the POST body
    request_data = request.get_json()
    item = request_data['item']

    #Add item to the list
    response_data = helper.add_to_list(item)

    #Return error if item not added
    if response_data is None:
        response = Response("{'error': Item not added - " + item + "'}", status = 400, mimetype = 'application/json')
        return response

    #Return response
    response = Response(json.dumps(response_data), mimetype = 'application/json')

    return response


@app.route('/items/all')
def get_all_items():
    # Get items from the helper
    response_data = helper.get_all_items()

    # Return response
    response = Response(json.dumps(response_data), mimetype = 'application/json')
    return response



@app.route('/item/status', methods=['GET'])
def get_item():
    # Get parameter from the URL
    item_name = request.args.get('name')

    # Get items from the helper
    status = helper.get_item(item_name)

    # Return 404 if item not found
    if status is None:
        response = Response("{'error': 'Item Not Found - %s'}"  % item_name, status=404 , mimetype='application/json')
        return response

    # Return status
    response_data = {
        'status': status
    }

    response = Response(json.dumps(response_data), status=200, mimetype='application/json')
    return response


@app.route('/item/update', methods=['PUT'])
def update_status():
    #Get item from the POST body
    request_data = request.get_json()
    item = request_data['item']
    status = request_data['status']

    #Update item in the list
    response_data = helper.update_status(item, status)

    #Return error if the sattus could not be updated
    if response_data is None:
        response = Response("{'error': 'Error updating item - '" + item + ", " + status + "}", status = 400, mimetype = 'application/json')
        return response

    response = Response(json.dumps(response_data), mimetype = 'application/json')
    
    return response


@app.route('/item/delete', methods=['DELETE'])
def delete_item():
    #Get the item from the POST body
    request_data = request.get_json()
    item = request_data['item']

    #Delete the item from the list
    response_data = helper.delete_item(item)

    #Return error if the item could not be deleted
    if response_data is None:
        response = Response("{'error': 'Error deleting item - '" + item + "}", status = 400, mimetype = 'application/json')
        return response

    #Return response
    response = Response(json.dumps(response_data), mimetype = 'application/json')

    return Response