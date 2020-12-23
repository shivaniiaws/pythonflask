# coding: utf-8
from flask import Flask
import socket
import mysql.connector
app = Flask(__name__)
import mysql.connector
import mysql.connector
@app.route('/emp')
def empdt():

        mydb = mysql.connector.connect(
        host="dev.ctjetcarduvz.ap-southeast-1.rds.amazonaws.com",
        user="root",
        password="sheshi12",
        database="web"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM emp")
        print("test db")
        myresult = mycursor.fetchall()

        p = []

        tbl = "<tr><td>ID</td><td>Name</td><td>Email</td><td>Phone</td></tr>"
        p.append(tbl)

        for row in myresult:
                a = "<tr><td>%s</td>"%row[0]
                p.append(a)
                b = "<td>%s</td>"%row[1]
                p.append(b)
                c = "<td>%s</td>"%row[2]
                p.append(c)
                d = "<td>%s</td></tr>"%row[3]
                p.append(d)


        contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
        <html>
        <head>
        <meta content="text/html; charset=ISO-8859-1"
        http-equiv="content-type">
        <title>Python Webbrowser</title>
        </head>
        <body>
        <table>
        %s
        </table>
        </body>
        </html>
        '''%(p)
        return contents
@app.route('/')
def hello_world():
   hostname = socket.gethostname()
   IPAddr = socket.gethostbyname(hostname)
   print("Your Computer Name is:" + hostname)
   print("Your Computer IP Address is:" + IPAddr)
   return "<html><body><h1>Hello World:" + IPAddr + "</h1></body></html>"
   
if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000,debug = True)

