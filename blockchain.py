# Imports
import transactions
import pprint
import hashlib
import time
import transactions
#Block class
class Block:
    def __init__(self, index, transactiondata, timestamp, nonce = 1, previhash = None):
        self.previhash = previhash
        self.index = index
        self.timestamp = timestamp
        self.nonce = nonce
        self.transactiondata = transactiondata
        self.hash = self.calculatehash()
        
    # calculate the hash
    def calculatehash(self):
        d = str("{}{}{}{}{}".format(self.previhash, self.index, self.timestamp, self.nonce, self.transactiondata))
        #returns the sha256 hash
        return hashlib.sha256(d.encode()).hexdigest()

#blockchain
class BlockChain:
    def __init__(self, pending = [], chain = []):
        self.chain = chain
        self.pending = pending

    #gets the previous hash    
    def getprevihash(self):
        return self.chain[-1].hash

    # verify block
    def verifyblock(self, block):
        if block.previhash == self.chain[-1]:
            print("Same previous hash. block not allowed.")
            return False
        elif block.hash == self.getprevihash():
            print("The same hash as the previous block")
            return False
             
            block.calculatehash()  
        elif block.nonce ==  0 or None:
            print("Nonce is supposed to start at 1 or u didnt calcualte the proof of work")    
        else:
            return True    
            

    #adds block to our blockchain    
    def addblock(self, block):
        if len(self.chain) > 0:
            block.previhash = self.getprevihash()
            self.chain.append(block)
        else: 
            block.previhash = None 
            self.chain.append(block)

    def mineblock(self, acc):
        pendingblock = self.pending[-1]
        pendingblock.nonce = 1
        strhash = str(pendingblock.hash)
        if strhash[:3] == "123":
            self.addblock()
        else:
            hashnot12 = True
            while hashnot12:
             pendingblock.nonce += 1
             pendingblock.hash = pendingblock.calculatehash()
             strhash = str(pendingblock.hash)
             print(pendingblock.hash, pendingblock.nonce)
             if strhash[:3] == "123":
              self.addblock(pendingblock)
              print("block mined")
              rewards = pendingblock.transactiondata.sender.amount / 2
              
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

                tjsonarray = {}
                tjsonarray['receiver'] = block.transactiondata.receiver
                tjsonarray['amt'] = block.transactiondata.amount
                tjsonarray['sender'] = block.transactiondata.sender 
                pprint.pprint(tjsonarray)
