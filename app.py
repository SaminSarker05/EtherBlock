from EtherChain import *

from flask import Flask, request

app = Flask(__name__)

@app.route('/mine', methods=['GET'])
def mineEther():
  return "mining..."

@app.route('/chain', methods=['GET'])
def seeChain():
  return "chain..."

@app.route('/new', methods=['POST'])
def transaction():
  data = request.get_json()
  return data


if __name__ == '__main__':
    app.run(debug = True)