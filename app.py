from flask import Flask, render_template, request, jsonify
from handler.nfts import *
import time
import json


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """index page"""
    data = {}
    return render_template('nfts.html', data=data)


# deploy Contract
@app.route('/deploy')
def deploy_nft():
    x = create_nft()
    return jsonify(x)


# mint_nft
@app.route('/mint', methods=['GET','POST'])
def _mint_nft():
    data = {}
    if request.method == 'POST':
        data = get_form_to_dict(request.form)
    id = int(time.time())
    address = data['address']
    x = json.dumps(data)
    result = mint_nft(id, address, x)
    return jsonify(result)


# transfer_nft
@app.route('/transfer', methods=['GET','POST'])
def _transfer_nft():
    data = {}
    if request.method == 'POST':
        data = get_form_to_dict(request.form)
    id = int(time.time())
    address_transfer = data['address_transfer']
    #print((address_transfer))
    address_receive = data['address_transfer']
    x = transfer_nft(id, address_transfer, address_receive)
    return jsonify(x)
    

#get nfts
@app.route('/getnfts', methods=['GET'])
def _get_nft():
    y = get_nfts()
    return jsonify(y)



# get contract
@app.route('/contract', methods=['get'])
def contract():
    x = get_contract_address()
    print(x)
    return jsonify(x)


# create invoice
@app.route('/invoice', methods=['GET','POST'])
def _create_invoice():
    data = {}
    if request.method == 'POST':
        data = get_form_to_dict(request.form)
    amount = data['amount']
    receiver = data['receiver']
    x = create_invoice(amount, receiver)
    return jsonify(x)


# get_invoice 

@app.route('/getinvoice', methods=['get'])
def _get_invoice():
    x = get_invoices()
    print(x)
    return jsonify(x)


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)

