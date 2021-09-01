import helper 
from flask import Flask, request, Response
import json

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/item/new',methods=['POST'])
def add_item():
	#Get item from the POST body
    req_data = request.get_json()
    item =req_data['item']

	#Add item to the list
    res_data = helper.add_to_list(item)

    #Return error if item not added 
    if res_data is None:
        response = Response("{'error': 'Item not added - " + item 
"'}, status=400 ,mimetype='application/json')
	return response
    # Return response
    response= Response(json.dumps(res_data), mimetype='application
/json')

return response 
