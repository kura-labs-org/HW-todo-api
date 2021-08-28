# HW-todo-api
Allows user to track the items they would like to accomplish on a website. The app functions as a digital planner.



# Base App
 
 [StackAbuse](https://stackabuse.com/building-a-todo-app-with-flask-in-python/)

# App

***Return Json***
- [x] List items

**Endpoint:** ``/items``

**Request Method:** ``GET``
- [x] Add item

**Endpoint:** ``/items/new/<name>``

**DataType:** ``json`` 

**Request method:** ``Post``

- [x] Search Item status

**Endpoint:** ``/items/<name>``

**DataType:** ``str`` 

**Request method:** ``GET``
- [x] Update item

**Endpoint** ``/items/update/<Name>/<newstatus>``

**DataType:** ``str``

**Request Method:** ``PUT``
- [x] Delete item

**Endpoint:** ``/items/remove/<name>``

**DataType:** ``str``

**Request Method:**``DELETE``

# Changes

* Split items into classes and added params so a user can query items quicker