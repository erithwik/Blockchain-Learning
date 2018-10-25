import hashlib

# This hashes the input string
def hashString(str):
	return hashlib.sha256(str.encode()).hexdigest()

# This creates a transaction with selder, reciever, and the amount
class transaction:
	def __init__(self, sender, reciever, amount):
		self.sender = sender
		self.reciever = reciever
		self.amount = amount

	def __str__(self):
		return "{0}{1}{2}".format(self.sender, self.reciever, self.amount)

	def hashSelf(self):
		return hashString(self.__str__())

# This makes the merkleRoot with a list of hashes of the transactions as input
def merkleRoot(list_of_transactions):
	# This is recursive so if the list_of_transactions has only length one, it means this is the merkle root and returns it
	if(len(list_of_transactions) == 1):
		return list_of_transactions[0]
	# makes the list_of_hashes for the next round
	nextList = []
	# for every two elements in the list of transactions, this concatenates them and hashes them	
	for i in range(len(list_of_transactions) // 2):
		nextList.append(hashString("{0}{1}".format(list_of_transactions[2*i], list_of_transactions[2*i+1])))
	# This sees if the list_of_transactions is odd. If it is, it adds the last element to the hash as well.
	if len(list_of_transactions) % 2 != 0:
		nextList.append(list_of_transactions.pop())
	# This returns a recursive function making the merkle tree of the next list.
	return merkleRoot(nextList)

# t_l is the list of fake transactions to test out the merkle tree.
t_l = []
for i in range(10):
	t_l.append(str(transaction("Alex", "Bobby", 5)))

# This prints the merkleRoot of the list of transactions: t_l
print(merkleRoot(t_l))