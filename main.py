from types import TracebackType
import helper
from flask import Flask, request, Response
from flask_restful import Resource,Api
import json

app = Flask(__name__)
api=Api(app)
class Items(Resource):
    def get(self):
        # Get items from the helper
        res_data = helper.get_all_items()
        #Return response
        response = Response(json.dumps(res_data), mimetype='application/json')
        return response
    def post(self,name):
        #Get item from the POST body
        #Add item to the list
        res_data = helper.add_to_list(name)
        #Return error if item not added
        if res_data is None:
            response = Response("{'error': 'Item not added - '}"  + item, status=400 , mimetype='application/json')
            return response
        #Return response
        response = Response(json.dumps(res_data), mimetype='application/json')
        return response
class Item(Resource):
    def get(self,name):
        # Get items from the helper
        status = helper.get_item(name)
        
        #Return 404 if item not found
        if status is None:
            response = Response("{'error': 'Item Not Found - '}"  + item_name, status=404 , mimetype='application/json')
            return response

        #Return status
        res_data = {
            'status': status
        }

        response = Response(json.dumps(res_data), status=200, mimetype='application/json')
        return response

    def put(self,name,newstatus):
        #Update item in the list
        res_data = helper.update_status(name, newstatus)
        if res_data is None:
            response = Response("{'error': 'Error updating item - '" + item + ", " + status   +  "}", status=400 , mimetype='application/json')
            return response
        
        #Return response
        response = Response(json.dumps(res_data), mimetype='application/json')
        
        return response
    def delete(self,name):
        #Get item from the POST body
        #Delete item from the list
        res_data = helper.delete_item(name)
        if res_data is None:
            response = Response("{'error': 'Error deleting item - '" + item +  "}", status=400 , mimetype='application/json')
            return response
        #Return response
        response = Response(json.dumps(res_data), mimetype='application/json')
        return response
api.add_resource(Items,'/items','/items/new/<name>')
api.add_resource(Item,'/item/<name>','/item/update/<name>/<newstatus>','/item/remove/<name>')
if __name__ =='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)