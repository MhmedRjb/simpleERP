from flask import Flask, request, render_template, jsonify , Blueprint
from blueprint.item import item
from blueprint.transaction import transaction
app = Flask(__name__)

app.register_blueprint(item)
app.register_blueprint(transaction)

@app.route('/')
def index():
    #print helow world
    return 'Hello World!'

@app.route('/health', methods=['GET'])
def health_check():
    # Add any additional checks to verify the application's health.
    # You can check the database connection, external services, etc.
    return "OK", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
