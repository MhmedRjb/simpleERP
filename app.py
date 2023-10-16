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



if __name__ == '__main__':
    app.run()
