
import sqlite3
import os
from bottle import post, get, template, request, redirect


#are we executing at Pythonanywhere?
ON_PYTHONANYWHERE = "PYTHONANYWHERE_DOMAIN" in os.environ

assert ON_PYTHONANYWHERE == False


if ON_PYTHONANYWHERE: 
    pass
else:
    #on the development environment, import the development server
    from bottle import run, debug

@get('/')
def get_show_list():
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("select * from todo")
    result = cursor.fetchall()
    cursor.close()
    # return str(result)
    return template ("show_list",rows=result)


@get("/status/<id:int>/<value:int>")
def get_status(id, value):
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("update todo set status = ? where id = ?", (value, id))
    connection.commit()
    cursor.close()
    redirect("/")


@get('/new_item')
def get_new_item():
    return template ("new_item")


@post('/new_item')
def post_new_item():
    new_item = request.forms.get("new_item").strip()
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("insert into todo (task, status) values (?,?)", (new_item, 1))
    connection.commit()
    cursor.close()
    # return str(result)
    # return "the new item is: ["+ new_item +"]..."
    redirect("/")

@get('/delete_item/<id:int>')
def get_delete_item(id):
    print("We want to delet ", id)    

if ON_PYTHONANYWHERE:
    pass
else:
    #on the development environment. run the development server:
    debug(True)
    run(host='localhost', port=8080)