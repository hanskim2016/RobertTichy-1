from flask import Flask, redirect, render_template
# import the Connector function
# from mysqlconnection import MySQLConnector
# imports the Bcrypt module
# from flask.ext.bcrypt import Bcrypt
import os, re
app = Flask(__name__)
# bcrypt = Bcrypt(app)             # this is for encryption
# app.secret_key = os.urandom(48)  # this is for encrypting the session cookie?

# connect and store the connection in "mysql" note that you pass the database name to the function
# mysql = MySQLConnector(app, 'wall')

@app.route('/')
def index():
    poke=range(1,152)
    print poke
    return render_template( "pokeAPI.html", poke=poke)
app.run(debug=True)
