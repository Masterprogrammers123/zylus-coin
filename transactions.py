from account import Account
from Crypto.PublicKey import RSA

class Transactions:
    def __init__(self, receiver : Account, amount : int, sender : Account):
        self.receiver = receiver 
        self.amount = amount
        self.sender = sender
    
    def add_transaction(self, sk):
        if self.receiver == self.sender:
            print("U are sending money to urself. U will not earn money.")
            return False
        if self.private_key:
            if self.private_key == sk:
                return True
        if self.sender.money < self.amount:
            print("U have less money then ur sending. PLease get more money.")
            return False
        else:
            print("Please generate your keys before trying to send zylus coins, thanks!")
            return False

        if self.private_key:
            if self.private_key == sk:
                return True
                self.receiver.money += self.amount   


    def verify_transaction(self, transaction, pk):  
        if not self.pk or len(self.pk) > 7:
            print("There is no signature. Nice try!")
            return False
        if transaction == True:
            pass 
                