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
  
  def __str__(self):
    return f"Index: {self.index}, Timestamp: {self.timestamp}, Transactions: {self.transactions}, Proof: {self.proof}, Previous Hash: {self.previous_hash}"


class EtherChain:
  def __init__(self):
    self.chain = LinkedList()
    self.transactions = LinkedList()

    self.new_block(proof = 100, previous_hash = 1)

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
    return hashlib.sha256(str(block)).hexdigest()
  
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