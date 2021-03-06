from blockchain import Block, BlockChain
from transactions import Transactions
from account import Account
from pprint import pprint
from time import time

acout = Account()
ac2 = Account()

bc = BlockChain()

acout.generate_public_key()

acout.generate_zylus_key()

acout.generate_private_key()

ac2.generate_public_key()

ac2.generate_private_key()

ac2.generate_zylus_key()

transes = Transactions(acout, 10, ac2)

block1 = Block(1, transes, time(), 1)

bc.createblock(block1)

bc.mineblock(block1)

bc.printchain()