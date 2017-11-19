# File: salt.py
# Author: Joshua Lam
# File containing functions to create salts

import hashlib
import random

# Return a salt of length 8
def getSalt():
	chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
	saltChars = list(chars)
	salt = []
	for i in range(0, 8):
		salt.append(random.choice(saltChars))
	return ''.join(salt)

# Return the hash of the password and salt combination
def getHash(password, salt):	
	combo = password + salt
	return hashlib.sha512(combo.encode()).hexdigest()

