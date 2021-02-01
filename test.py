import blockchain

a = blockchain.Block("LOA", None, 1, 10000)

b = blockchain.BlockChain([])

b.addblock(a)

b.printchain()