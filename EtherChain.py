from time import time
from uuid import uuid4
import hashlib
import json
from urllib.parse import urlparse
import requests

# class EtherBlock:
#   def __init__(self, index, transactions, proof, previous_hash, time=time()):
#     self.index = index
#     self.timestamp = time
#     self.transactions = transactions
#     self.proof = proof
#     self.previous_hash = previous_hash

#   def __str__(self):
#     return f"Index: {self.index}, Timestamp: {self.timestamp}, Transactions: {self.transactions}, Proof: {self.proof}, Previous Hash: {self.previous_hash}"

class EtherChain:
  def __init__(self):
    self.chain = []
    self.transactions = []
    self.neighbors = set()
    self.new_block(p=100, prev_hash=1)

  def add(self, etherBlock):
    self.chain.append(etherBlock)

  def __len__(self):
    return len(self.chain)

  def new_transaction(self, src, dest, amount):
    data = {
      'sender': src,
      'recipient': dest,
      'amount': amount
    }
    self.transactions.append(data)
    return self.last_block()['index'] + 1

  def new_block(self, p, prev_hash = None):
    block = {
      'index': len(self.chain) + 1,
      'time': time(),
      'transactions': self.transactions,
      'proof': p,
      'previous_hash': prev_hash or self.hash(self.chain[-1])
    }

    self.transactions = []
    self.chain.append(block)
    return block

  def last_block(self,):
    return self.chain[-1]

  @staticmethod
  def hash(block):
    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()
  
  def poW(self, last_proof):
    proof = 0
    while not self.poW_validate(last_proof, proof):
      proof += 1
    return proof

  @staticmethod
  def poW_validate(last_proof, proof):
    output = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(output).hexdigest()
    return guess_hash[:4] == "0000"

  def register_node(self, address):
    # url_comp = urlparse(address) # returns a tuple of information
    self.neighbors.add(address)

  def valid_chain(self, chain):
    last_block = chain[0]
    ind = 1
    while ind < len(chain):
      print(f"{last_block}")
      print(f"{chain[ind]}")
      if chain[ind]['previous_hash'] != self.hash(last_block): return False
      last_block = chain[ind]
      ind += 1
    return True

  def resolve(self):
    nei = self.neighbors
    print('step1')
    new_chain = None
    print('step2')
    our_length = len(self.chain)
    print('step3')

    for node in nei:
      print(f"{node}/chain")
      res = requests.get(f"{node}/chain")
      print(res)
      if res.status_code == 200:
        length = res.json()['length']
        chain = res.json()['chain']
        if length > our_length and self.valid_chain(chain):
          new_chain = chain
          our_length = length
    print('step4')

    if new_chain != None:
      self.chain = found
      return True
    
    return False