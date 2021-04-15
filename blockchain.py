# Imports
import transactions
import pprint
import hashlib
import time
#Block class
class Block:
    def __init__(self, index, timestamp,nonce = 1, previhash = None):
        self.previhash = previhash
        self.index = index
        self.timestamp = timestamp
        self.nonce = nonce
        self.hash = self.calculatehash()

    # calculate the hash
    def calculatehash(self):
        d = str("{}{}{}{}".format(self.previhash, self.index, self.timestamp, self.nonce))
        #returns the sha256 hash
        return hashlib.sha256(d.encode()).hexdigest()

#blockchain
class BlockChain:
    def __init__(self, pending = [], chain = []):
        self.chain = chainn
        self.pending = pending

    #gets the previous hash    
    def getprevihash(self):
        return self.chain[-1].hash

    #adds block to our blockchain    
    def addblock(self, block):
        if len(self.chain) > 0:
            block.previhash = self.getprevihash()
            self.chain.append(block)
        else:
            block.previhash = None 
            self.chain.append(block)
        

    def mineblock(self):
        pendingblock = self.pending[-1]
        pendingblock.nonce = 1
        strhash = str(pendingblock.hash)
        if strhash[0] == "8":
            self.addblock()
        else:
            hashnot12 = True
            while hashnot12:
             pendingblock.nonce += 1
             pendingblock.hash = pendingblock.calculatehash()
             strhash = str(pendingblock.hash)
             print(pendingblock.hash, pendingblock.nonce)
             time.sleep(1)
             if strhash[0] == "8":
              self.addblock(pendingblock)
              print("block mined")
              break




    #adds block to our blockchain    
    def createblock(self, block):
        #if the blokc chain does not have a transactino then the previous hahs is none making it the genisis block
        if len(self.chain) > 0:
            block.previhash = self.getprevihash().hash
            self.pending.append(block)
        else:
            block.previhash = None 
            self.pending.append(block)


    # Makes us a nicer way of seeing our blockchain
    def printchain(self):
            for block in self.chain:
                jsonarray = {}
                jsonarray['hash'] = block.hash
                jsonarray['prevhash'] = block.previhash
                jsonarray['index'] = block.index
                jsonarray['timestamp'] = block.timestamp
                jsonarray['nonce'] = block.nonce
                # Prints out the blockchain
                pprint.pprint(jsonarray)
