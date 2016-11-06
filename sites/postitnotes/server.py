from flask import Flask, render_template, request, redirect, jsonify, session # jsonify lets us send JSON back!
# Import MySQLConnector class from mysqlconnection.py
from mysqlconnection import MySQLConnector
app = Flask(__name__)
'''
Set variable 'mysql' to be an instance of the MySQLConnector class,
taking our entire application as the first argument and the database
name as the second argument.
'''
mysql = MySQLConnector(app, 'ajaxnotes2')
app.secret_key='EBCDIC'


@app.route('/',methods=["GET"])
def index():
    return render_template('index.html')


@app.route('/notes/',methods=["GET"])
def notes():
    print "index()"

    if not 'first' in session:
        session['first']=0

    first = session['first']

    query = "SELECT * FROM notes ORDER BY updated_at DESC LIMIT :first,8"
    qdict = {'first':first}
    result = mysql.query_db(query,qdict)
    # print "R:",result
    return jsonify(notes=result)


@app.route('/notes/<arg>',methods=["GET"])
def notes_page(arg):
    print "notes_page()"

    if not 'first' in session:
        session['first']=0

    if session['first'] > 0 and arg == 'left':
        session['first'] -= 8
        if session['first'] < 0:
            session['first'] = 0
    if arg=='right':
        session['first'] += 8

    first = session['first']

    query = "SELECT * FROM notes ORDER BY updated_at DESC LIMIT :first,8"
    qdict = {'first':first}
    result = mysql.query_db(query,qdict)

    if len(result)==0:
        session['first'] -= 8
        first = session['first']
        query = "SELECT * FROM notes ORDER BY updated_at DESC LIMIT :first,8"
        qdict = {'first':first}
        result = mysql.query_db(query,qdict)


    return jsonify(notes=result)

@app.route('/notes//search',methods=["GET"])
def catch1():
    return redirect('/notes')

    
@app.route('/notes/<arg>/search',methods=["GET"])
def notes_search(arg):
    print "notes_search()"

    session['first']=0
    first = session['first']

    x = arg
    print x
    filters = x.split(',')
    print filters
    where="WHERE ("
    for i in range(0,len(filters)):
        if i > 0:
            where +=" OR"
        f = filters[i].strip(u' ')
        where += " subject LIKE '%"+f+"%'"
    where +=" ) "
    print where
    query = "SELECT * FROM notes " + where + "ORDER BY updated_at DESC LIMIT :first,8"
    qdict = {'first':first}
    result = mysql.query_db(query,qdict)

    return jsonify(notes=result)


@app.route('/notes/create', methods = ["POST"])
def create():
    subject = request.form['subject']
    subject.strip()
    if subject != None and subject != "":
        query = "INSERT INTO notes (subject, created_at, updated_at) VALUES (:subject , NOW(), NOW())"
        qdict = { "subject": subject}
        row = mysql.query_db(query,qdict)
    return jsonify(row)


@app.route('/notes/<id>/delete', methods = ['GET'])
def delete(id):
    id.strip()
    if int(id) != 0:
        query = "DELETE FROM notes where notes.id=:id"
        qdict = {"id": int(id)}
        result = mysql.query_db(query,qdict)
        # print "Result:",result
    return jsonify(result)


@app.route('/notes/<id>/edit', methods = ['GET'])
def edit_show(id):
    id.strip()
    if int(id) != 0:
        query = "SELECT * FROM notes where notes.id=:id"
        qdict = {"id": int(id)}
        result = mysql.query_db(query,qdict)
    return render_template('edit.html', note=result[0])


@app.route('/notes/<id>/edit', methods = ['POST'])
def edit_update(id):
    id.strip()
    if int(id) != 0:
        note = request.form['note']
        subject = request.form['subject']
        query = "UPDATE notes SET subject=:subject, note=:note, updated_at=NOW() WHERE notes.id=:id"
        qdict = { "id": int(id), "subject":subject, "note":note }
        result = mysql.query_db(query,qdict)
    return redirect('/')
    # return render_template('update.html', note=result[0])
app.run(debug=True)
