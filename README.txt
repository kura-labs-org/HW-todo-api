The todoapp allows you to run the curl command with four different methods.

Method1 - POST
function/method that uses post: add_item()
when you call this method it will add an item to the table with the object
ex: items contains the object item

Method2 - Get
function/method that uses this method: get_all_items() and get_item(item)
when you do curl it automatically does a get but it calls the method which
will select the specified item or all of them and return them

Method3 - PUT
function/method that uses this method: update_status
will get the specified item and overwrites it if it exists

Method4 - DELETE
function/method that uses this method: delete_item(item), del_all_items() <- my added function
will basically delete the specified object within the specified columns but the function I added would delete everything and return back everything that was deleted