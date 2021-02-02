# Imports

import pprint

# Extremely basic setup of the blockchain

class Block:
    def __init__(self, hash, prevhash, index, timestamp):
        self.hash = hash
        self.prevhash = prevhash
        self.index = index
        self.timestamp = timestamp
        
    
class BlockChain:
    def __init__(self, chain):
        self.chain = []

    def addblock(self, block):
        self.chain.append(block)

    def printchain(self):
            for block in self.chain:
                jsonarray = {}
                jsonarray['hash'] = block.hash
                jsonarray['prevhash'] = block.prevhash
                jsonarray['index'] = block.index
                jsonarray['timestamp'] = block.timestamp

                pprint.pprint(jsonarray)
