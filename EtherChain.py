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
    self.nodes = set()
    self.new_block(p=100, prev_hash=1)

  def add(self, etherBlock):
    self.chain.append(etherBlock)

  def __len__(self):
    return len(self.chain)

  # def register_node(self, address):
  #   self.nodes.add(address)

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

  # def valid_chain(self, chain):
  #   last_block = chain[0]
  #   curr = 1
  #   while curr < len(chain):
  #     testBlock = EtherBlock(index=int(last_block['index']), transactions=last_block['transactions'], proof=last_block['proof'], previous_hash=last_block['previous_hash'], time=last_block['timestamp'])
  #     if chain[curr]['previous_hash'] != self.hash(testBlock):
  #       return False
  #     last_block = chain[curr]
  #     curr += 1
  #   return True

  # def resolve(self):
  #   neighbors = self.nodes
  #   found = None
    
  #   for node in neighbors:
  #     response = requests.get(f'{node}/chain')
  #     if response.status_code == 200:
  #       length = response.json()['length']
  #       chain = response.json()['chain']

  #       if length > len(self) and self.valid_chain(chain):
  #         found = LinkedList()
  #         for block in chain:
  #           etherBlock = EtherBlock(index=int(block['index']), transactions=block['transactions'], proof=block['proof'], previous_hash=block['previous_hash'], time=block['timestamp'])
  #           found.append(etherBlock)
      
  #   if found:
  #     self.chain = found
  #     return True
    
  #   return False