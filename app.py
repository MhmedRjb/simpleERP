from flask import Flask, request, render_template, jsonify , Blueprint
from blueprint.item import item
from blueprint.transaction import transaction
from blueprint.main.clients import clients
import mysql.connector
from Config import dbConfig
from flaskext.mysql import MySQL
import os
from services.connections.database import mysql, init_app,check_database_connection

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config.from_object(dbConfig)
# Initialize the MySQL extension
init_app(app)
app.register_blueprint(item)
app.register_blueprint(transaction)
app.register_blueprint(clients)


@app.route('/')
def index():
    #print helow world
    return 'Hello World!'

@app.route('/health', methods=['GET'])
def health_check():
    # Check database connection
    db_status = check_database_connection()

    if db_status is True:
        return jsonify({'status': 'OK', 'database': 'Healthy'}), 200
    else:
        return jsonify({'status': 'Database connection error', 'error': db_status}), 500





if __name__ == '__main__':
    app.config['EXPLAIN_TEMPLATE_LOADING'] = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.config['JSON_SORT_KEYS'] = False
    app.run(host='0.0.0.0', port=8080, debug=True)
