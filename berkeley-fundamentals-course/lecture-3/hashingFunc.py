import hashlib

# This hashes the input string
def hashString(str):
	return hashlib.sha256(str.encode()).hexdigest()
