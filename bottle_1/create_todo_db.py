import sqlite3

connection = sqlite3.connect("todo.db")
connection.execute("Create table todo (id integer primary key, task char(100) not null, status bool not null)")
connection.execute("insert into todo (task, status) VALUES ('Read A-byte-of-Python',0)")
connection.execute("insert into todo (task, status) VALUES ('visit a python website',1)")
connection.execute("insert into todo (task, status) VALUES ('make an account on pythonanywhere',1)")
connection.execute("insert into todo (task, status) VALUES ('choose your favorite WSGI-Framework',0)")
connection.commit()
# commit takes everything I wrote and make them premd888
#required in creating,inserting,modifying, not for reading.