from blockchain import Block, BlockChain
from transactions import Transactions
from pprint import pprint

trans = Transactions(999)
pprint(trans.generate_public_key())
pprint(trans.generate_private_key())

block = Block("LOA", None, 1, 10000)

chain = BlockChain([])

chain.addblock(block)

chain.printchain()
