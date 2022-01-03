from flask import Flask,render_template,request
import sqlite3
import _sqlite3

application = app = Flask(__name__,static_folder='./static')


# conn = sqlite3.connect('todo.db')
# print("Opened database successfully")

# conn.execute('CREATE TABLE todos ("item" TEXT NOT NULL,"status" TEXT NOT NULL,PRIMARY KEY("item"))')
# print("Table created successfully")
# conn.close()



todolist = []


@app.route('/')
def todo_app():
    return render_template('index.html')

@app.route('/addtodo',methods = ['POST', 'GET'])
def addtodo():
    if request.method == 'POST':
        try:
            con = sqlite3.connect("todo.db")
            item = request.form['item']
            todolist.append(item)
            print(item)
            cur = con.cursor()
            cur.execute('INSERT INTO todos (item,status) VALUES(?,?)',(item,"uncomplete"))

        # We commit to save the change
            con.commit()

            #msg = "item successfully added"
        except:
            con.rollback()
            #msg = "error in insert operation"
      
        finally:
            return render_template("index.html",number_of_items=len(todolist),todolist=[item for item in todolist])
            con.close()
    else:
        con = sqlite3.connect("todo.db")
        cur = con.cursor()
        cur.execute('SELECT * FROM todos')
# @app.route('/reset')
# def resetitems():
#     todolist = []
#     if request.method == 'POST':
#         try:
#             pass
#         except:
#             con.rollback()
#             #msg = "error in insert operation"
#         finally:
#             return render_template("index.html",todolist=[item for item in todolist])
#             con.close()

    
