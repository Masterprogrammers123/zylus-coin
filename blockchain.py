# Imports

import pprint
import hashlib
# Extremely basic setup of the blockchain

class Block:
    def __init__(self, index, timestamp, previhash = None):
        self.previhash = previhash
        self.index = index
        self.timestamp = timestamp
        self.hash = self.calculatehash()
      
    def calculatehash(self):
        d = str("{}{}{}".format(self.previhash, self.index, self.timestamp))
        return hashlib.sha256(d.encode()).hexdigest()


class BlockChain:
    def __init__(self, chain = []):
        self.chain = chain

    def getprevihash(self):
        return self.chain[-1]

    def addblock(self, block):
        if len(self.chain) > 0:
            block.previhash = self.getprevihash().hash
            self.chain.append(block)
        else:
            block.previhash = None 
            self.chain.append(block)

    def printchain(self):
            for block in self.chain:
                jsonarray = {}

                jsonarray['hash'] = block.hash
                jsonarray['prevhash'] = block.previhash
                jsonarray['index'] = block.index
                jsonarray['timestamp'] = block.timestamp

                pprint.pprint(jsonarray)

