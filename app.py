from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    #print helow world
    return 'Hello World!'


@app.route('/record_transaction', methods=['GET'])
def get_transaction():
    # Handle the GET request here
    return render_template('add_transaction.html')

@app.route('/record_transaction', methods=['POST'])
def record_transaction():
    # Handle the transaction data here
    # ...
    data = request.json  # Get the data from the request
    print("Received data from the form:", data)  # Print the data to the console for testing

    # Respond with a JSON message (for testing)
    response = {'message': 'Transaction recorded successfully'}
    
    # Render the transaction_form.html
    return response, 200



@app.route('/add_item', methods=['GET'])
def get_item():
    return render_template('add_item.html')

@app.route('/add_item', methods=['POST'])
def record_item():
    data = request.json
    print("Received data from the form:", data)
    
    response = {'message': 'Transaction recorded successfully'}

    return response, 200

if __name__ == '__main__':
    app.run(debug=True)
