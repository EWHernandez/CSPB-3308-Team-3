import psycopg2 as pg

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

# Function to delete a user entry by id
def delete_entry(exercise_name):
    conn = pg.connect(**db_args)
    cursor = conn.cursor()

    # Delete data from the "workouts" table
    cursor.execute('DELETE FROM workouts WHERE exercise_name=%s', (exercise_name,))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

def recreateTable():
    conn = pg.connect(**db_args)
    cursor = conn.cursor()

    # Recreate the "workouts" table
    cursor.execute('DROP TABLE IF EXISTS workouts;')
    cursor.execute('''
        CREATE TABLE workouts (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            date TIMESTAMP,
            exercise_name VARCHAR,
            duration INTERVAL,
            workout_type INTEGER,
            notes VARCHAR
        )
    ''')



# Example usage:
# add_workout('Bench Press', '12/1/23', '15', 'strength', '3 sets of 12 reps')
# delete_entry(Bench Press)
