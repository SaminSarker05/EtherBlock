from EtherChain import *
from flask import Flask, request, jsonify

app = Flask(__name__)
etherChain = EtherChain()


@app.route('/mine', methods=['GET'])
def mineEther():
  last_block = etherChain.last_block().data
  last_proof = last_block.proof
  new_proof = etherChain.poW(last_block)

  etherChain.new_transaction(0, "Jack", 1)
  previous_hash = etherChain.hash(last_block)

  block = etherChain.new_block(new_proof, previous_hash)

  response = {
    'message': f'new block {block.index} forged',
    'proof': str(new_proof),
    'previous_hash': str(previous_hash),
  }
  return response


@app.route('/chain', methods=['GET'])
def seeChain():

  blocks = []
  for node in etherChain.chain:
    block = node.data
    transactions = block.transactions
    ledger = []
    for _ in transactions:
      ledger.append(_.data)

    des = {
      "index": str(block.index),
      "previous_hash": str(block.previous_hash),
      "proof": str(block.proof),
      "timestamp": str(block.timestamp),
      "transactions": ledger,
    }
    blocks.append(des)

  response = {
    'chain': blocks,
    'length': len(etherChain)
  }
  return jsonify(response), 200


@app.route('/new', methods=['POST'])
def transaction():
  data = request.get_json()
  required = ['sender', 'recipient', 'amount']
  for i in data:
    if i not in required:
      print("missing values")
      return 'Missing Values', 400
  
  index = etherChain.new_transaction(data['sender'], data['recipient'], data['amount'])
  response = {
    'message': f'transaction will be added to ether block {index}'
  }
  return jsonify(response)


@app.route('/register', methods=['POST'])
def register():
  data = request.get_json()
  nodes = data.get('nodes')
  if nodes is None:
    return "Error", 400
  
  for node in nodes:
    etherChain.register_node(node)

  response = {
    'message': "new nodes added",
    'nodes': nodes
  }
  return jsonify(response)


@app.route('/resolve', methods=['GET'])
def consensus():
  change = etherChain.resolve()
  message = "not changed"
  if change:
    message = "chain was changed"
  
  response = {
    'message': message
  }

  return jsonify(response), 200
  

import sys 


if __name__ == '__main__':
  port = 5000
  if len(sys.argv) > 1:
    try:
      port = int(sys.argv[1])
    except ValueError:
      print("invalid port")

  app.run(debug = True, port = port)