from flask import Flask, request, render_template, jsonify , Blueprint
from blueprint.item import item
import mysql.connector



config = {
  'user': 'he',
  'password': 'AVNS_YbysylwEM8xq2ycbVfl',
  'host': 'db-mysql-nyc3-08709-do-user-14592966-0.b.db.ondigitalocean.com',
  'port': '25060',
  'database': 'defaultdb',
  'ssl_disabled': 'True',
}

# Connect to the database
db = mysql.connector.connect(**config)



# Don't forget to close the connection


# Check if the connection was successful
if db.is_connected():
    print("Connected to the database")
    cursor = db.cursor()
    cursor.execute("SHOW TABLES")

    tables = cursor.fetchall()

    for table in tables:
        print(table[0])


# Check if the connection was successful
if db.is_connected():
    print("Connected to the database")


# from blueprint.transaction import transaction
app = Flask(__name__, template_folder='templates', static_folder='static')

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





# @app.route('/my_table')
# def view_my_table():    
#     cursor.execute("SELECT * FROM my_table")
#     result = cursor.fetchall()

#     return render_template('my_table.html', data=result)




if __name__ == '__main__':
    app.config['EXPLAIN_TEMPLATE_LOADING'] = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.config['JSON_SORT_KEYS'] = False
    
    
    app.run(host='0.0.0.0', port=8080, debug=True)
