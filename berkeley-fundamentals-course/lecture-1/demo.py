''' Each account has an unspent transaction output which is what
they received as "packages" of cryptocurreny from other people.
It works in the following way: when someone sends you money, they send
it in the form of a piggy bank. When you want to send money to 
someone else, you break your piggy banks, make new piggy banks as needed 
and send the piggy banks you amade containing money to the other people and to 
yourself if the most recent piggy bank you broke has more money in it than what 
you wanted to send to the other person. This prevents double spending.

- Lecture 1 29:00 - 34:00
- Ending - 51:00'''

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