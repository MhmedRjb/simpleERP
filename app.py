from flask import Flask, request, render_template, jsonify , Blueprint
from blueprint.item import item
# from blueprint.transaction import transaction
app = Flask(__name__, template_folder='templates', static_folder='static')

app.register_blueprint(item)
@app.route('/record_transaction', methods=['GET'])
def get_transaction():
    # Handle the GET request here
    return render_template('add_transaction.html')

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


if __name__ == '__main__':
    app.config['EXPLAIN_TEMPLATE_LOADING'] = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    
    app.run(host='0.0.0.0', port=8080, debug=True)
