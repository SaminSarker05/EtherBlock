# EtherChain - The Best Blockchain

Users can interact with the Ether blockchain through API endpoints, mine new blocks, and participate in the consensus process. The project uses Flask for API development and the SHA-256 hash function. Multiple users can connect to the network and the consensus algorithm ensures the EtherChain's validity. Users can pass transactions to the public ledger and miners are awarded with EtherBlock.

## Features

- `API endpoints`: register (POST), mine (GET), chain (GET), new (POST), resolve (GET)
- `Proof of Work`: Miners compete to generate a new hash with 5 leading zeros using previous block's proof
- `Consensus Algorithm`: Ensures the same valid EtherChain is shared amongst all nodes in the network
- `Peer-to-peer Connection`: Allows decentralization of EtherChain and sharing of ledger amongst user nodes
- `Transaction Data`: Etherblock stores transaction data between users

## Technologies Used

- `Flask`: Python framework used for API building
- `Python`: Backend language for functions and logic
- `Postman`: API platform for endpoint testing
- `SHA-256`: Hash function for cryptographic hashes

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

- View entire blockchain with transactions
<img src="https://github.com/SaminSarker05/EtherBlock/blob/main/images/chain.png" width=80%>

- Mine a new block and add transactions
<img src="https://github.com/SaminSarker05/EtherBlock/blob/main/images/mine.png" width=80%>

- Register another node/user in network
<img src="https://github.com/SaminSarker05/EtherBlock/blob/main/images/register.png" width=80%>

- Write a new transaction to be added to next block
<img src="https://github.com/SaminSarker05/EtherBlock/blob/main/images/new.png" width=80%>

- Call consensus algorithm to validate EtherChain
<img src="https://github.com/SaminSarker05/EtherBlock/blob/main/images/resolve.png" width=80%>

## Remarks

- Default port is 5000. To change port append different number as such `python3 app.py NEW_PORT`
- 4 leading zeroes results in a small computation time. More zeros exponentially increase mining duration


