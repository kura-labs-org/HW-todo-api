# HW-todo-api

Submit your To-Do-API here. In your readme describe the application and any additions you made. Please link to the source of the API. If you have a git repo for this project on your own account also link to it here (as it would document the dif's between what you wrote and what was given to you)

## Assignment
For this application, I have made a documentation file that includes how to complete this assignment. While doing this assignment, I faced a lot of issues with the documentation. The person who made the article from Stack Abuse had so many issues with simple typos. He would leave out some routes from the CURL request which would make the app fail. I had to spend a good amount of time debugging the issues. I tried to make the database by just creating a random file but I had to create an actual database using DB Browser for SQLite. Curl and Windows is also a weird combination. I had many issues but figured it out. This program basically has different ways of adding, recieving, updating, and deleting items from a database. Basically it follows CRUD. Create, read, update, and delete.


## My Feature

There are not many features that I can think of adding so I thought since we have a delete one row, it would be great to have a delete all rows function. In the app.py I created a new function called delete_all_items()  In this function delete_all_items() function is called from helper.py. The result is stored in res_data. The next line dumps all the items from the list on, I reused some code from the get_all_items function. 


## Upcomming

I plan to imrpove this application by adding new methods to sort the database whenever I get a chance to.
