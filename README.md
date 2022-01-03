For my Todo app I created a simple database named items in SQLlite to begin with.
Then I went about creating the app. Once this was implemented, 4 methods were utilized to facilitate different changes within the table.

POST
in terms of the method that used post: add_item()
it was used to add an item to the table with the object
ex: items contains the object item

GET
in terms of the function that uses get: get_all_items() and get_item(item)
it will call the method which will then chooses the particular item or items and returns them

PUT
function that uses put: update_status
it will get a specific item and adjusts it if it does indeed exists

DELETE
functions that use delete method: delete_item(item)
when called it will delete the chosen object on specific columns 
