from blockchain import Block, BlockChain
from transactions import Transactions
from pprint import pprint
from time import time

ts = time()

bc = BlockChain()

block1 = Block(1, ts)

bc.createblock(block1)

bc.mineblock()

bc.printchain()
trans = Transactions("Phantom", "Zack", 999)
trans.generate_public_key()
trans.generate_private_key()
