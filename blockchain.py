# Imports

import pprint
import hashlib
#Block class
class Block:
    def __init__(self, index, timestamp, previhash = None):
        self.previhash = previhash
        self.index = index
        self.timestamp = timestamp
        self.hash = self.calculatehash()
    # calculate the hash
    def calculatehash(self):
        d = str("{}{}{}".format(self.previhash, self.index, self.timestamp))
        #returns the sha256 hash
        return hashlib.sha256(d.encode()).hexdigest()

#blockchain
class BlockChain:
    def __init__(self, chain = []):
        self.chain = chain

    #gets the previous hash    
    def getprevihash(self):
        return self.chain[-1].hash

    #adds block to our blockchain    
    def addblock(self, block):
        #if the blokc chain does not have a transactino then the previous hahs is none making it the genisis block
        if len(self.chain) > 0:
            block.previhash = self.getprevihash()
            self.chain.append(block)
        else:
            block.previhash = None 
            self.chain.append(block)

    # Makes us a nicer way of seeing our blockchain
    def printchain(self):
            for block in self.chain:
                jsonarray = {}
                jsonarray['hash'] = block.hash
                jsonarray['prevhash'] = block.previhash
                jsonarray['index'] = block.index
                jsonarray['timestamp'] = block.timestamp
                # Prints out the blockchain
                pprint.pprint(jsonarray)
