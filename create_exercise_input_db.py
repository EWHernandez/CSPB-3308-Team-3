import sqlite3

def create_workouts():
    # Create the database and establish a connection
    conn = sqlite3.connect('workouts.db')
    cursor = conn.cursor()

    # Create the "workouts" table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS workouts (
            id INTEGER PRIMARY KEY,
            -- FOREIGN KEY (user_id) REFERENCES users (id),
            date DATETIME,
            exercise_name VARCHAR,
            date DATETIME,
            duration TIME,
            workout_type INT,
            notes VARCHAR,
            FOREIGN KEY (user_id) REFERENCES user(id)
        )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Function to add a workout entry
#modify to have user Id
def add_workout(date, exercise_name, duration, workout_type, notes):
    conn = sqlite3.connect('workouts.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO workouts (date, exercise_name, duration, workout_type, notes)
        VALUES (?, ?, ?, ?, ?)
    ''', (date, exercise_name, duration, workout_type, notes))
    conn.commit()
    conn.close()

# Function to add a workout entry 'get_workouts(user_ID)'
def get_workouts():
    conn = sqlite3.connect('workouts.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT date, exercise_name, workout_type, duration,  notes
        FROM workouts;
    ''')
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return rows

# Function to delete a user entry by id
def delete_entry(exercise_name):
    conn = sqlite3.connect('workouts.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM workouts WHERE exercise_name=?', (exercise_name))
    conn.commit()
    conn.close()

def recreateTable():
    conn = sqlite3.connect('workouts.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE workouts;')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS workouts (
        id INTEGER PRIMARY KEY,
        -- FOREIGN KEY (user_id) REFERENCES users (id),
        date DATETIME,
        exercise_name VARCHAR,
        duration TIME,
        workout_type INT,
        notes VARCHAR
    )''')
    conn.commit()
    conn.close()


# Example usage:
# add_workout('Bench Press', '12/1/23', '15', 'strength', '3 sets of 12 reps')
# delete_entry(Bench Press)
