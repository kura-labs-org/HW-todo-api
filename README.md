# HW-todo-api

Submit your To-Do-API here. In your readme describe the application and any additions you made. Please link to the source of the API. If you have a git repo for this project on your own account also link to it here (as it would document the dif's between what you wrote and what was given to you)


# source 
https://stackabuse.com/building-a-todo-app-with-flask-in-python/

# description
In this task, we had to create an API or web service for the todo app. The API service had to be implemented using a REST-based architecture.

Each request to the RESTful system commonly uses these 4 HTTP verbs:

GET: Get a specific resource or a collection of resources 
get_all_items() and get_item(item)

POST: Create a new resource
add_item()

PUT: Update a specific resource
update_status

DELETE: Remove a specific resource
delete_item(item), del_all_items() <- my added function

First, we install Flask using pip: $ pip install Flask
Then we created a file main.py and typed this command: 

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

After importing Flask, we set up a route. A route is specified by a URL pattern, an HTTP method, and a function which receives and handles an HTTP request.
We run Flask app:

$ FLASK_APP=main.py flask run
Running on http://127.0.0.1:5000/
$ curl -X GET http://127.0.0.1:5000/

We greeted with the response:  
Hello World!

Then we installed the DB Browser for SQLite to easily create a database the database name is todo.db and we craeted table. 
Then we defined helper functions in a separate file helper.py
After adding all the function and items from instuction we used cURL to send a POST request and test out our app. we run command:

$ curl -X POST http://127.0.0.1:5000/item -d '{"item": "Setting up Flask"}' -H 'Content-Type: application/json'

We got response: 
{"Setting up Flask": "Not Started"}

For add one more item to the list we used this command:
$ curl -X POST http://127.0.0.1:5000/item -d '{"item": "Implement POST endpoint"}' -H 'Content-Type: application/json'

We got response: 
{"Implement POST endpoint": "Not Started"}

Then we used cURL to fetch the items and test our route:
$ curl -X GET http://127.0.0.1:5000/items/all

We got response:
json {"count": 2, "items": [["Setting up Flask", "Not Started"], [Implement POST endpoint", "Not Started"]]}

Next command:
$ curl -X GET http://127.0.0.1:5000/item/status?name=Setting+up+Flask

Responsed:
{"status": "Not Started"}

We used cURL to test this route, just as before:
$ curl -X PUT http://127.0.0.1:5000/item/update -d '{"item": "Setting up Flask", "status": "Completed"}' -H 'Content-Type: application/json'

Finely we greeted with the response:
{"Setting up Flask": "Completed"}

For delete we used this command:
$ curl -X DELETE http://127.0.0.1:5000/item/remove -d '{"item": "Setting up Flask"}' -H 'Content-Type: application/json'

we got response:
{"item": "Temporary item to be deleted"}

