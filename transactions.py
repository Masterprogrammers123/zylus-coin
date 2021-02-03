from Crypto.PublicKey import RSA

class Transactions:
    def __init__(self, amount : int, key, sender, reciver):
        self.amount = amount
        self.key = RSA.generate(2048)

    def generate_public_key(self):
        public_key = self.key.publickey().exportKey("PEM")
        return public_key

    def generate_private_key(self):
        priv_key = self.key.exportKey("PEM")
        return priv_key