from LinkedList import LinkedList
from time import time
from uuid import uuid4
import hashlib

class EtherBlock:
  def __init__(self, index, transactions, proof, previous_hash):
    self.index = index
    self.timestamp = time()
    self.transactions = transactions
    self.proof = proof
    self.previous_hash = previous_hash


class EtherChain:
  def __init__(self):
    self.chain = LinkedList()
    self.transactions = LinkedList()

  def new_transaction(self, sender, recipient, amount):
    data = {
      'sender': sender,
      'recipient': recipient,
      'amount': amount
    }
    self.transactions.append(data)
    return self.last_block['index'] + 1

  def new_block(self, proof, previous_hash = None):
    block = EtherBlock(len(self.chain) + 1, self.transactions, proof, previous_hash)
    self.transactions = LinkedList()
    self.chain.append(block)
    return block

  def last_block(self):
    return self.chain.last()

  def hash(EtherBlock):
    pass
  
  def poW(self, last_proof):
    proof = 0
    while self.poW_validate(last_proof, proof) is False:
      proof += 1
    
    return proof
  
  def poW_validate(self, last_proof, proof):
    test = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:4] == "0000"

test = EtherChain()