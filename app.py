from EtherChain import *
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import sys 

app = Flask(__name__)
CORS(app)

etherChain = EtherChain()

@app.route('/', methods=['GET'])
def home():
  return render_template('home.html')


# creates and appends a new block to blockchain with transactions
@app.route('/mine', methods=['GET'])
def mineEther():
  last_block = etherChain.last_block() 
  last_proof = last_block['proof']
  new_proof = etherChain.poW(last_proof)

  etherChain.new_transaction(0, "Jack", 1)
  previous_hash = etherChain.hash(last_block)
  print("hash", previous_hash)

  block = etherChain.new_block(new_proof, previous_hash)

  response = {
    'message': f'new ether block {block["index"]} forged',
    'proof': str(new_proof),
    'previous_hash': str(previous_hash),
    'transactions': block['transactions']
  }
  return response


# endpoint returns json of entire chain and recorded transactions
@app.route('/chain', methods=['GET'])
def seeChain():
  blocks = []
  for block in etherChain.chain:
    transactions = block['transactions']
    desc = {
      "index": str(block['index']),
      "timestamp": str(block['timestamp']),
      "transactions": transactions,
      "proof": str(block['proof']),
      "previous_hash": str(block['previous_hash']),
    }
    blocks.append(desc)

  response = {
    'chain': blocks,
    'length': len(etherChain)
  }
  return jsonify(response), 200


# endpoint to add a transaction to the blockchain
@app.route('/new', methods=['POST'])
def transaction():
  data = request.get_json()
  required = ['sender', 'recipient', 'amount']
  for i in data:
    if i not in required: return 'Missing Values', 400
  
  index = etherChain.new_transaction(data['sender'], data['recipient'], data['amount'])
  response = {
    'message': f'transaction will be added to ether block {index}'
  }
  return jsonify(response)


# endpoint to allow a user to add other users to their registry
@app.route('/register', methods=['POST'])
def register():
  data = request.get_json() # parse json payload for use
  node = data.get('node')
  if node is None: return jsonify("error"), 400  
  # add neighbor/user to our registry
  etherChain.register_node(node)

  response = {
    'message': "neighbor nodes added to registry",
    'nodes': node
  }
  return jsonify(response), 200

@app.route('/test', methods=['GET'])
def test():
  return jsonify(etherChain.valid_chain(etherChain.chain)), 200


@app.route('/resolve', methods=['GET'])
def consensus():
  made_change = etherChain.resolve()
  message = "not changed"
  if made_change: message = "chain was changed"
  return jsonify(message), 200


if __name__ == '__main__':
  app.run(debug = True, port = port)
