from transaction import transaction
from hashingFunc import hashString
# This makes the merkleRoot with a list of hashes of the transactions as input
def merkleRoot(list_of_transactions):
	# This is recursive so if the list_of_transactions has only length one, it means this is the merkle root and returns it
	if(len(list_of_transactions) == 1):
		return list_of_transactions[0]
	# makes the list of hashes for the next round
	nextList = []
	# for every two elements in the list of transactions, this concatenates them and hashes them	
	for i in range(len(list_of_transactions) // 2):
		nextList.append(hashString("{0}{1}".format(list_of_transactions[2*i], list_of_transactions[2*i+1])))
	# This sees if the list_of_transactions is odd. If it is, it adds the last element to the hash as well.
	if len(list_of_transactions) % 2 != 0:
		nextList.append(list_of_transactions.pop())
	# This returns a recursive function making the merkle tree of the next list.
	return merkleRoot(nextList)

def main():
	# t_l is the list of fake transactions to test out the merkle tree.
	t_l = []
	for i in range(10):
		t_l.append(transaction("Alex", "Bobby", 5).hashSelf())

	# This prints the merkleRoot of the list of transactions: t_l
	print(merkleRoot(t_l))

if __name__ == "__main__":
	main()