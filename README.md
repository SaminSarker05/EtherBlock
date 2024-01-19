# EtherChain - The Best Blockchain

A lightweight blockchain implementation. Users can interact with the blockchain through API endpoints, mine new blocks, and participate in the consensus process. The project uses Flask for API development and the SHA-256 hash function. Multiple users can connect to the network and the consensus algorithm ensures the EtherChain's validity. Users can pass transactions to the public ledger and miners are awarded with EtherBlock.

## Features

- `API endpoints`: register (POST), mine (GET), chain (GET), new (POST), resolve (GET)
- `Proof of Work`: Miners compete to generate a new hash with 5 leading zeros using previous block's proof
- `Consensus Algorithm`: Ensures the same valid EtherChain is shared amongst all nodes in the network
- `Peer-to-peer Connection`: Allows decentralization of EtherChain and sharing of ledger amongst user nodes
- `Transaction Data`: Etherblock stores transaction data between users

## Technologies Used

- `Flask`: API building
- `Python`: Backend language for functions
- `Postman`: Testing API endpoints

## API Endpoints

- `register`: POST - allows registration of nodes in network
- `mine`: GET - mines a new block and adds to local chain
- `new`: POST - new transaction data to be saved on next block
- `chain`: GET - returns current chain and blocks with data
- `resolve`: GET - uses consensus algo to check for changes

## Getting Started

1. Clone the repository:
   ```bash
   git clone git@github.com:SaminSarker05/EtherBlock.git
   ```
2. Change into Project Directory:
   ```bash
   cd EtherBlock
   ```
3. Install Project Dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the Flask Application:
   ```bash
   python3 app.py
   ```

## Examples on Postman

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")







blockchain Notes:

public ledger - record of financial transactions

each block has data, hash, hash of previous block
bitcoin blockchain stores data of transactions

each hash is unique
hash of previous block allows chaining

first block called genesis block -> has no previous block

proof of work --> mechanism to create new block
takes a long time to do proof of work

P2P network allows anyone to join

ledger shared with everyone

one way hash of signature 

inverse is infeasible

crearting block - mining by block creator

public database where transactions stored in an immutable chain

digital money can be easily duplicated --> requires 3rd party authentication

proof of work process makes adding new block of transiactions by miners difficult --> relies on computational difficulty

bitcoin wallet contains private and public key
private to send
public to receive

1. make transaction
2. broadcast transaction
3. miner will validate and add to block
4. broadcast blockchain change to all miners

sign transaction using private key

transactions stored in blocks
new block added every few minutes

senders need to provide transaction fee to incentivize miners to include their transaction into the block
mining process = proof of work

hash funcion maps an arbitrary size to fixed size

SHA-256 hash function used in bitcoin

miners compete to find a new valid block

to reslive conflicts follow longest chain

