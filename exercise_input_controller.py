###############################################################################
##
## This starter code was taken from Lab  6 Flask application and modified
## for the team 3 application
##
## The **prefix.py** code is included to allow you to develop your code within
## the **csel.io** environment.  There is a required prefix to be used when
## pages access the **csel.io** virtual machine from your local machine browser.
## 
## The prefix code will have no effect when running Flask on your local machine
## as it looks to make sure you are running on **csel.io** virtual machine.
##
## Author: Knox - Sept 2022
## Contributor: Fall 2023 Team 3 Members
##
###############################################################################


###############################################################################
## Import "prefix" code into your Flask app to make your app usable when running
## Flask either in the csel.io virtual machine or running on your local machine.
## The module will create an app for you to use

from flask import Flask, render_template, url_for, request, jsonify, redirect
import create_exercise_input_db as ceid

# create app to use in this Flask application
app = Flask(__name__, static_folder='static', template_folder='templates')


###############################################################################
##
## Begin Routes for Team 3 Exercise Food Application

@app.route('/index')
def index():
    return "HERE"

@app.route('/')
def exercise():
    ceid.create_workouts()
    return render_template('exercise_input.html')

@app.route('/testinput', methods=['POST'])
def testinput():

    #Get user iD follow syntax
    name = request.form.get('exercise_name')
    etype = request.form.get('exercise_type')
    minute = request.form.get('exercise_minute')
    note = request.form.get('exercise_notes')
    date = request.form.get('dateinput')

    #modify to include userID
    ceid.add_workout(date, name, minute, etype, note)
    
    print("made it here")
    return redirect('/', code=302)

@app.route('/populate_table', methods=['GET'])
def populate_table():
    return jsonify(ceid.get_workouts())

@app.route('/empty_table', methods=['GET'])
def recreate_table():
    ceid.recreateTable()
    print("Table emptied")
    return redirect('/', code=302)


###############################################################################
# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server using port 3308 instead of port 5000.
    app.run(host='0.0.0.0', port=3308)