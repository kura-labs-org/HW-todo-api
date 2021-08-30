import sqlite3

DB_PATH = './todo.db'
NOTSTARTED = 'Not Started'
INPROGRESS = 'In Progress'
COMPLETED = 'Completed'

def add_to_list(item):
    try:
        connection = sqlite3.connect(DB_PATH)
        
        #Establish connection and use the cursor method to execute queries
        c = connection.cursor()
        
        #Keep the initial status as Not Started
        c.execute('Insert into items(item, status) values(?, ?)', (item, NOTSTARTED))

        #We commit to save the change
        connection.commit()
        return {"item": item, "status": NOTSTARTED}
    finally:
        pass
    

def get_all_items():
    try:
        connection = sqlite3.connect(DB_PATH)
        c = connection.cursor()
        c.execute('select * from items')
        rows = c.fetchall()
        return { "count": len(rows), "items": rows }
    except Exception as e:
        print('Error: ', e)
        return None


# def get_item(item):
#     try:
#         connection = sqlite3.connect(DB_PATH)
#         c = connection.cursor()
#         c.execute("select status from items where item='%s'" % item)
#         status = c.fetchone()[0]
#         return status
#     except Exception as e:
#         print('Error: ', e)
#         return None


def get_item(item):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("select status from items where item='%s'" % item)
        status = c.fetchone()[0]
        return status
    except Exception as e:
        print("Error: ", e)
        return None

def update_status(item, status):
    #Check if the passed status is a valid value
    if (status.lower().strip() == 'not started'):
        status = NOTSTARTED
    elif (status.lower().strip() == 'in progress'):
        status = INPROGRESS
    elif (status.lower().strip() == 'completed'):
        status = COMPLETED
    else:
        print(f"Invalid Status: {status}")
        return None

    try:
        connection = sqlite3.connect(DB_PATH)
        c = connection.cursor()
        c.execute('update items set status = ? where item = ?', (status, item))
        connection.commit()
        return {item: status}
    except Exception as e:
        print('Error: ', e)
        return None

def delete_item(item):
    try:
        connection = sqlite3.connect(DB_PATH)
        c = connection.cursor()
        c.execute('delete from items where item = ?', (item,))
        connection.commit()
        return {'item': item}
    except Exception as e:
        print('Error: ', e)
        return None