from flask import Blueprint, render_template, request, jsonify
from services.connections.database import mysql

# Create a Blueprint
clients = Blueprint('clients', __name__)

@clients.route('/view_table/<table_name>')
def view_table(table_name):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        columns = [desc[0] for desc in cursor.description]

        return render_template('mytable.html', data=result, columns=columns)
    except Exception as e:
        error_message = str(e)
        response = {'error': 'Failed to retrieve data', 'details': error_message}
        return jsonify(response), 500

@clients.route('/insert_data', methods=['GET'])
def get_insert_data():
    return render_template('insertdata.html')

@clients.route('/insert_data', methods=['POST'])
def insert_data():
    """
    Inserts data into the 'my_table' table in the database.

    Expects a JSON object with the following keys:
    - id: The ID of the data to insert
    - name: The name of the data to insert
    """

    # Get the data from the request
    try:
        # Get the data from the request
        data = request.json
        id = data['id']
        name = data['name']

        # Connect to the database
        conn = mysql.connect()
        cursor = conn.cursor()

        # Insert the data into the table
        query = "INSERT INTO my_table (id, name) VALUES (%s, %s)"
        values = (id, name)
        cursor.execute(query, values)
        conn.commit()

        # Close the database connection
        cursor.close()
        conn.close()

        # Return a success message
        response = {'message': 'Data inserted successfully'}
        return jsonify(response), 200

    except Exception as e:
        # Handle the exception and return an error message
    # Log the error message
        print("Error:", str(e))
        
        # Handle the exception and return an error message
        error_message = str(e)
        response = {'error': 'Data insertion failed', 'details': error_message}
        return jsonify(response), 500  # Use an appropriate HTTP status code
