# Financial Calculator
# Author: Joshua Lam
# Date: 10/14/17

import csv
import finance
import limited_finance
import salt

# Create password file if first time executing program
credentials = {}
try:
	with open('credentials.csv', 'r') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			credentials[row['username']] = [row['hash'], row['salt']]
except IOError:
	with open('credentials.csv', 'w') as csvfile:
		fieldnames = ['username', 'hash', 'salt']
		writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
		writer.writeheader()
		newSalt = salt.getSalt()
		writer.writerow({'username':'admin','hash':salt.getHash('ics3552017',newSalt),'salt':newSalt})
		credentials['admin'] = [salt.getHash('ics3552017', newSalt), newSalt]
def signIn():
	username = input("Please enter your username: ")
	password = input("Please enter your password: ")
	if username in credentials:
		if salt.getHash(password,credentials[username][1]) == credentials[username][0]:
			print('Logging in...\n\n')
			return username
		else:
			print('Incorrect username and password combination\n\n')
			return 0	

banner = '\n\t\tWelcome to the Financial Calculator Program!\n\t\t\t\tVersion 2.0\n\n\t\t\tFeatures Included:\n\n\t\t\t**Account Management**\n\t\t\t**Currency Conversion**\n\t\t\t**Multiple Currency Support**\n\t\t\t**Persisting Database**\n\t\t\t**Salted Passwords**\n\t\t\t**Admin Account**\n\n\t\tDo you want to sign in (s) or quit (q)?\n'
print(banner)	
signOrReg = input("Please enter s or q: ")
if signOrReg is 's':
	s = signIn()
	if s:
		if s == 'admin':
			finance.bank(s)
		else:
			limited_finance.bank(s)
elif signOrReg is 'q':
	print("Quitting...")
else:
	print("You did not enter a valid input. Exiting...\n")

