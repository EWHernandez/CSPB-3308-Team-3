import psycopg2 as pg
import database as db
import create_exercise_input_db as ceid

from flask import Flask
from flask import render_template
from flask import request, redirect, url_for, flash, jsonify

app = Flask(__name__)
app.secret_key = 'team_3_rules' 

db_args = {
    'dsn': "postgres://exercise_input_user:UJBoq6dkr6d26DEF14q4vVShnKJ4u6Xz@dpg-clqd7kae9h4c73ald8qg-a.oregon-postgres.render.com/exercise_input"
}

@app.route('/') #default
def create_workouts():
    # Create the database and establish a connection
    conn = pg.connect(**db_args)
    cursor = conn.cursor()

    # Create the "workouts" table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS workouts (
            id SERIAL PRIMARY KEY,
            -- user_id INTEGER REFERENCES users(id),
            date TIMESTAMP,
            exercise_name VARCHAR,
            duration INTERVAL,
            workout_type INTEGER,
            notes VARCHAR
        )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    return render_template('exercise_input.html')

# Function to add a workout entry
#modify to have user Id
def add_workout(date, exercise_name, duration, workout_type, notes):
    conn = pg.connect(**db_args)
    cursor = conn.cursor()

    # Add data to the "workouts" table
    cursor.execute('''
        INSERT INTO workouts (date, exercise_name, duration, workout_type, notes)
        VALUES (%s, %s, %s, %s, %s)
    ''', (date, exercise_name, duration, workout_type, notes))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Function to add a workout entry 'get_workouts(user_ID)'
def get_workouts():
    conn = pg.connect(**db_args)
    cursor = conn.cursor()

    # Retrieve data from the "workouts" table
    cursor.execute('''
        SELECT date, exercise_name, workout_type, duration, notes
        FROM workouts;
    ''')
    rows = cursor.fetchall()

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    return rows

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
def recreateTable():
    conn = pg.connect(**db_args)
    cursor = conn.cursor()

    # Recreate the "workouts" table
    cursor.execute('DROP TABLE IF EXISTS workouts;')
    cursor.execute('''
        CREATE TABLE workouts (
            id SERIAL PRIMARY KEY,
            -- user_id INTEGER REFERENCES users(id),
            date TIMESTAMP,
            exercise_name VARCHAR,
            duration INTERVAL,
            workout_type INTEGER,
            notes VARCHAR
        )
    ''')

    print("Table emptied")
    return redirect('/', code=302)