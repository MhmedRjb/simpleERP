from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('transaction_form.html')

@app.route('/record_transaction', methods=['POST'])
def record_transaction():
    # Handle the transaction data here
    # ...
    data = request.json  # Get the data from the request
    print("Received data from the form:", data)  # Print the data to the console for testing

    # Respond with a JSON message (for testing)
    response = {'message': 'Transaction recorded successfully'}
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
