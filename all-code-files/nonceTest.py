from hashingFunc import hashString
from transaction import transaction

nonceDifficulty = 5

# A really primitive block type that only has an id and a nonce that
# can be adjusted
class block:
	def __init__(self, idVal, nonce):
		self.id = idVal
		self.nonce = 0

	def __str__(self):
		return "block - id: {0} - nonce: {1}".format(self.id, self.nonce)

	def hashBlock(self):
		return hashString(self.__str__())

''' This function finds the nonce that would give the "nonceDifficulty"
amount of preceding zeros given the block and the difficulty
'''
def find_nonce(nonceDifficulty, block):
	# The nonce starts at an arbritrary number, lets say 0 for now
	nonceTest = 0
	blockCopy = block

	# The function looks at the first nonceDifficulty characters of the hash and
	# sees if they all equal '0'. If they do, then it says it found the nonce.
	while(list(blockCopy.hashBlock())[:nonceDifficulty] != ['0']*nonceDifficulty):
		nonceTest += 1
		blockCopy.nonce = nonceTest

	# exiting the while loop means that the nonce solved the puzzle
	
	print("The puzzle has been solved!")
	block = blockCopy
	# The reason this code changes the copy of the block instead of 
	# the block itself is because multiple people are tryig
	# to solve the block's puzzle at the same time. Changing
	# the block itself after only one person adjusts the nonce will
	# screw over everyone's puzzle solving and what nonce 
	# each individual is currently on.

	return nonceTest

def main():
	b = block(12, 0)
	n = find_nonce(nonceDifficulty, b)
	print("nonce: {0}, hashOfBlock: {1}".format(n, b.hashBlock()))


if __name__ == "__main__":
	main()