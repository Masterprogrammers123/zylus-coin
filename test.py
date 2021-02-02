from blockchain import Block, BlockChain
from transactions import Transactions
from pprint import pprint
from time import time

indexer = 1
#timestamp
ts = time()
# make a block
block1 = Block(indexer, ts)

# Make a Chain
blockchai = BlockChain()

#Add block to chain
blockchai.addblock(block1)

# Make another block
block2 = Block(2, ts)

#Add it to chain
blockchai.addblock(block2)

#Print it
blockchai.printchain()

#Make Transactions object, generate keys
trans = Transactions(999)
pprint(trans.generate_public_key())
pprint(trans.generate_private_key())
