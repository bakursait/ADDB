from bottle import route, run, template


@route('/hello')
@route('/hello/<my_name>')
def get_hello(my_name="Unknown Person"):
    return template("Hello {{name}}!!!", name=my_name)



@route('/goodbye')
def get_goodbye():
    return "<html>GoodBye there!!!</html>"

run(host='localhost', port=8080)