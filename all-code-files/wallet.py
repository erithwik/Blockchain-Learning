import ecdsa
from transaction import transaction

class wallet:
	def __init__(self, privateKey = None):
		if privateKey == None:
			self.privateKey = ecdsa.SigningKey.generate(curve = ecdsa.SECP256k1)
		else:
			self.privateKey = ecdsa.SigningKey.from_string(s.decode('hex'), curve = ecdsa.SECP256k1)
		self.publicKey = self.privateKey.get_verifying_key()

	def privateKeyString(self):
		return (self.privateKey.to_string()).hex()

	def publicKeyString(self):
		return (self.publicKey.to_string()).hex()

	def createTransaction(self):
		a = input("To whom are you sending the transaction to?")
		b = input("What amount of x-coin are you sending to this entity?")
		tr = transaction(self.publicKeyString(), a, b)
		return tr

	def sendTransaction(self, tr):
		signature = self.privateKey.sign((tr.hashSelf()).hex())
		return signature, self.publicKey, tr.hashSelf()
	
a = wallet()
tr = a.createTransaction()
print(a.sendTransaction(tr))

def verifyTransaction(signature, pubKey, tr):
	return pubKey.verify(signature, tr)