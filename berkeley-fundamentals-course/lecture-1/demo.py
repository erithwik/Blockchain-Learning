class UTXO:
	def __init__(self, amount):
		self.amount = amount


class person:
	def __init__(self, name, UTXOs=[]):
		self.name = name
		self.UTXOs = UTXOs

	def sendPersonUXTOs(self, person, amount):
		tempUTXO = self.UTXOs[:]
		for utxo in tempUTXO:
			if amount == 0:
				break
			if utxo.amount <= amount:
				newUTXO = UTXO(utxo.amount)
				amount -= utxo.amount
				self.UTXOs.remove(utxo)
				person.UTXOs.append(newUTXO)
				print(amount)
			else:
				otherUTXO = UTXO(amount)
				selfUTXO = UTXO(utxo.amount - amount)
				amount = 0
				self.UTXOs.remove(utxo)
				self.UTXOs.append(selfUTXO)
				person.UTXOs.append(otherUTXO)

# Testing to see if Unspent Transaction Output works well.
u1 = UTXO(3)
u2 = UTXO(4)
Alice = person("Alice", [u1, u2])
Bob = person("Bob")
Alice.sendPersonUXTOs(Bob, 4)
print("Alice: {0}".format([utxo.amount for utxo in Alice.UTXOs]))
print("Bob: {0}".format([utxo.amount for utxo in Bob.UTXOs]))