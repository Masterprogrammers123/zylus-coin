from Crypto.PublicKey import RSA

class Transactions:
    def __init__(self, sender : str, receiver : str, amount : int):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.key = RSA.generate(2048)

    def generate_public_key(self):
        self.public_key = self.key.publickey().exportKey("PEM")
        with open("public key.pem", "a") as f:
            f.write(f"{self.public_key}\n")
        return self.public_key

    def generate_private_key(self):
        self.priv_key = self.key.exportKey("PEM")
        with open("private key.pem", "a") as f:
            f.write(f"{self.priv_key}\n")
        return self.priv_key