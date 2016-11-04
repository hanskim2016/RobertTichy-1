from flask import Flask, render_template, request, redirect, jsonify, session # jsonify lets us send JSON back!
# Import MySQLConnector class from mysqlconnection.py
from mysqlconnection import MySQLConnector
app = Flask(__name__)
'''
Set variable 'mysql' to be an instance of the MySQLConnector class,
taking our entire application as the first argument and the database
name as the second argument.
'''
mysql = MySQLConnector(app, 'ajaxnotes')
app.secret_key='EBCDIC'
@app.route('/',methods=["GET"])
@app.route('/notes/',methods=["GET"])
def index():
    print "index()"

    if not 'first' in session:
        session['first']=0

    first = session['first']

    query = "SELECT * FROM notes ORDER BY updated_at DESC LIMIT :first,8"
    qdict = {'first':first}
    result = mysql.query_db(query,qdict)
    # print "R:",result
    return render_template('index.html')
@app.route('/notes/index_json',methods=["GET"])
def index_json():
    print "index_json()"

    if not 'first' in session:
        session['first']=0

    first = session['first']

    query = "SELECT * FROM notes ORDER BY updated_at DESC LIMIT :first,8"
    qdict = {'first':first}
    notes = mysql.query_db(query,qdict)
    # print "R:",result
    return jsonify(notes=notes)
@app.route('/notes/create', methods = ["POST"])
def create():
    print "create()"
    note=request.form['postit']
    print note
    note.strip()
    if note != None and note != "":
        print "Write Note:",note
        query = "INSERT INTO notes (note, created_at, updated_at) VALUES (:note , NOW(), NOW())"
        qdict = { "note": note}
        insert = mysql.query_db(query,qdict)
    return redirect('/notes')
@app.route('/notes/create_json', methods = ["POST"])
def create_json():
    print "create_json()"
    note=request.form['postit']
    print note
    note.strip()
    if note != None and note != "":
        print "Write Note:",note
        query = "INSERT INTO notes (note, created_at, updated_at) VALUES (:note , NOW(), NOW())"
        qdict = { "note": note}
        row = mysql.query_db(query,qdict)
    return jsonify(row)
app.run(debug=True)
