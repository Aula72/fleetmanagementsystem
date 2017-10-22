
import mysql.connector
sqp = mysql.connector.connect(host="localhost", database="people", user="root")
cursors = sqp.cursor()
#usings = cursors.execute("INSERT INTO usings (name, password)VALUES('golden', 'goals');")
sqp.commit()
def dbfunction(l, j ):
    pre = "INSERT INTO usings VALUES(%s, %s)"
    cursors.execute(pre)
def newsreport():
    print("hello")
def lop():
    pass
p = input("the first value:")
q = input("the second value: ")      
dbfunction(p, q)