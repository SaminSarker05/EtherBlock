from LinkedList import LinkedList
from time import time
from uuid import uuid4
import hashlib
import json
from urllib.parse import urlparse

class EtherBlock:
  def __init__(self, index, transactions, proof, previous_hash):
    self.index = index
    self.timestamp = time()
    self.transactions = transactions
    self.proof = proof
    self.previous_hash = previous_hash

  def __str__(self):
  
    return f"Index: {self.index}, Timestamp: {self.timestamp}, Transactions: {self.transactions}, Proof: {self.proof}, Previous Hash: {self.previous_hash}"

class EtherChain:
  def __init__(self):
    self.chain = LinkedList()
    self.transactions = LinkedList()
    self.nodes = set()

    self.new_block(proof = 100, previous_hash = 1)

  def register_node(self, address):
    parsed_url = urlparse(address)
    self.nodes.add(parsed_url)


  def new_transaction(self, sender, recipient, amount):
    data = {
      'sender': sender,
      'recipient': recipient,
      'amount': amount
    }
    self.transactions.append(data)
    print(self.last_block())
    return self.last_block().data.index + 1


  def new_block(self, proof, previous_hash = None):
    block = EtherBlock(len(self.chain) + 1, self.transactions, proof, previous_hash)
    self.transactions = LinkedList()
    self.chain.append(block)
    return block


  def last_block(self,):
    return self.chain.last()

  def hash(self, block):
    data = {
      'index': str(block.index),
      'timestamp': str(block.timestamp),
      'transactions': str(block.transactions),
      'proof': str(block.proof),
      'previous_hash': str(block.previous_hash)
    }
    block_string = json.dumps(data, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()
  
  def poW(self, last_proof):
    proof = 0
    while self.poW_validate(last_proof, proof) is False:
      proof += 1
    
    return proof
  
  def poW_validate(self, last_proof, proof):
    test = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(test).hexdigest()
    return guess_hash[:4] == "0000"

test = EtherChain()