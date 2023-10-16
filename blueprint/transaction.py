# from flask import Blueprint, render_template, request, jsonify

# transaction = Blueprint('transaction', __name__)

# @transaction.route('/record_transaction', methods=['GET'])
# def get_transaction():
#     # Handle the GET request here
#     return render_template('add_transaction.html')

# @transaction.route('/record_transaction', methods=['POST'])
# def record_transaction():
#     # Handle the transaction data here
#     data = request.json  # Get the data from the request
#     print("Received data from the form:", data)  # Print the data to the console for testing

#     # Respond with a JSON message (for testing)
#     response = {'message': 'Transaction recorded successfully'}

#     return jsonify(response), 200


