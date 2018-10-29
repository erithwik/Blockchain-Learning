import ecdsa

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

	def sendTransaction(self, addrTo, amount):
		tr = Transaction(self.publicKey, addrTo, amount)
		signature = self.privateKey.sign(tr.hashSelf())
		return signature, self.publicKey


a = wallet()
print(a.privateKeyString())
print(a.publicKeyString())