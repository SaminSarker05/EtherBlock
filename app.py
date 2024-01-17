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

  response = {'message': f'new block {block.index} forged'}
  return response


@app.route('/chain', methods=['GET'])
def seeChain():
  etherChain.chain.printList()
  return "Hi"


@app.route('/new', methods=['POST'])
def transaction():
  data = request.get_json()
  required = ['sender', 'recipient', 'amount']
  for i in data:
    if i not in required:
      print("missing values")
      return 'Missing Values', 400
  
  index = etherChain.new_transaction(data['sender'], data['recipient'], data['amount'])
  response = {'message': f'transaction will be added to ether block {index}'}
  return response




if __name__ == '__main__':
    app.run(debug = True)