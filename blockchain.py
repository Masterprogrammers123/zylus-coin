# Extremely basic setup of the blockchain

class Block:
    def __init__(self, data, hash, previous_hash, genesis : bool=False):
        self.data = data
        self.hash = hash
        self.previous_hash = previous_hash
        self.genesis_block = genesis
        if self.genesis_block == True:
            print("Genesis block created.")
        else:
            print("Block Created.")
    
class BlockChain:
    def __init__(self, n):
        self.number_of_blocks = n
        self.genesis_block = Block(" ", " ", " ", True)
        self.blockchain = [self.genesis_block]

        for x in range(self.number_of_blocks-1):
            x = Block(" ", " ", " ")
            self.blockchain.append(x)
        
        print(self.blockchain)
    
b = BlockChain(5)
