from flask import Blueprint, render_template, request, jsonify
from app import db

item = Blueprint('item', __name__)

# Route to display the form for adding an item
@item.route('/add_item', methods=['GET'])
def get_item():
    return render_template('add_item.html')

# Route to record a new item
@item.route('/add_item', methods=['POST'])
def record_item():
    data = request.json
    print("Received data from the form:", data)

    response = {'message': 'Item recorded successfully'}

    return jsonify(response), 200

# Route to remove an item


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Item(id={self.id}, name='{self.name}', price={self.price})"

# Route to remove an item
@item.route('/remove_item/<int:item_id>', methods=['DELETE'])
def remove_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()

    response = {'message': f'Item with ID {item_id} removed successfully'}
    return jsonify(response), 200

# Route to see all items
@item.route('/view_items', methods=['GET'])
def view_all_items():
    # Code to retrieve all items from the database
    items = [{'id': 1, 'name': 'Item 1', 'price': 10.0}, {'id': 2, 'name': 'Item 2', 'price': 20.0}]
    return jsonify(items), 200

# Route to edit an item
@item.route('/edit_item/<int:item_id>', methods=['PUT'])
def edit_item(item_id):
    data = request.json
    # Code to update the item with the given ID in the database with the new data
    response = {'message': f'Item with ID {item_id} updated successfully'}
    return jsonify(response), 200

# Route to search for an item
@item.route('/search_item', methods=['GET'])
def search_item():
    # Code to search for an item in the database
    item_name = request.args.get('name')
    item = {'id': 1, 'name': item_name, 'price': 10.0}
    return jsonify(item), 200


