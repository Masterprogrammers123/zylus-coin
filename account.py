from Crypto.PublicKey import RSA

class Account:
    def __init__(self):
        self.key = RSA.generate(2048)
        self.zylus_key = RSA.generate(2048)
        self.amount = int(10)

    def generate_public_key(self):
        self.public_key = self.key.publickey().exportKey("PEM")
        return self.public_key

    def generate_zylus_key(self):
        self.zylus_key = self.key.publickey().exportKey("PEM")
        with open("zylus key.pem", "a") as f:
            f.write(str(self.zylus_key))
        return self.key

    def generate_private_key(self):
        self.private_key = self.key.exportKey("PEM")
        return self.private_key
