from flask import Flask, request, render_template, jsonify , Blueprint
from blueprint.item import item
import mysql.connector
from flaskext.mysql import MySQL
import os

mysql = MySQL()


# from blueprint.transaction import transaction
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['MYSQL_DATABASE_USER'] = os.environ.get('MYSQL_DATABASE_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ.get('MYSQL_DATABASE_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = os.environ.get('MYSQL_DATABASE_DB')
app.config['MYSQL_DATABASE_HOST'] = os.environ.get('MYSQL_DATABASE_HOST')
app.config['MYSQL_DATABASE_PORT'] = os.environ.get('MYSQL_DATABASE_PORT')
mysql.init_app(app)

app.register_blueprint(item)
@app.route('/record_transaction', methods=['GET'])
def get_transaction():
    # Handle the GET request here
    return render_template('addtransaction.html')

@app.route('/record_transaction', methods=['POST'])
def record_transaction():
    # Handle the transaction data here
    data = request.json  # Get the data from the request
    print("Received data from the form:", data)  # Print the data to the console for testing

    # Respond with a JSON message (for testing)
    response = {'message': 'Transaction recorded successfully'}

    return jsonify(response), 200


@app.route('/')
def index():
    #print helow world
    return 'Hello World!'

@app.route('/health', methods=['GET'])
def health_check():
    # Add any additional checks to verify the application's health.
    # You can check the database connection, external services, etc.
    return "OK", 200





@app.route('/my_table')
def view_my_table():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM my_table")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('mytable.html', data=result)


@app.route('/insert_data', methods=['GET'])
def get_insert_data():
    return render_template('insertdata.html')

@app.route('/insert_data', methods=['POST'])
def insert_data():
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
 



if __name__ == '__main__':
    app.config['EXPLAIN_TEMPLATE_LOADING'] = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.config['JSON_SORT_KEYS'] = False
    app.run(host='0.0.0.0', port=8080, debug=True)
