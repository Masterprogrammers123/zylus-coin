import blockchain
import time

indexer = 1
#timestamp
ts = time.time()
# make a block

block1 = blockchain.Block(indexer, ts)

blockchai = blockchain.BlockChain()

blockchai.addblock(block1)

block2 = blockchain.Block(2, ts)

blockchai.addblock(block2)

blockchai.printchain()