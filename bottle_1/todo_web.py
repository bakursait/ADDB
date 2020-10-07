from bottle import route, run, template
import sqlite3

@route('/todos')
def get_todos():
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("select * from todo")
    result = cursor.fetchall()
    # print(result)
    return str(result)



@route('/goodbye')
def get_goodbye():
    return "<html>GoodBye there!!!</html>"

run(host='localhost', port=8080)