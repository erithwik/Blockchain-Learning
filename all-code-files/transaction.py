from hashingFunc import hashString
# This creates a transaction with selder, reciever, and the amount
class transaction:
	def __init__(self, sender, reciever, amount):
		self.sender = sender
		self.reciever = reciever
		self.amount = amount

	# This creates the string concatenating all of the values of the transation
	def __str__(self):
		return "{0}{1}{2}".format(self.sender, self.reciever, self.amount)

	# This creates the hash of this transaction
	def hashSelf(self):
		return hashString(self.__str__())