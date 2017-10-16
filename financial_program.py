# Financial Calculator
# Author: Joshua Lam
# Date: 10/14/17

import csv
import finance

credentials = {}
try:
	with open('credentials.csv', 'r') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			credentials[row['username']] = row['password']
except IOError:
	with open('credentials.csv', 'w') as csvfile:
		fieldnames = ['username', 'password']
		writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
		writer.writeheader()
def signIn():
	username = input("Please enter your username: ")
	password = input("Please enter your password: ")
	if username in credentials:
		if password == credentials[username]:
			print('Logging in...\n\n')
			return username
		else:
			print('Incorrect username and password combination\n\n')
			return 0	
	else:
		callReg = input("Username does not exist. Do you want to create a new account? (y or n): ")
		if callReg is 'y':
			return reg()
		else:
			return 0

def reg():
	breakout = input("Do you really want to register an account? (y or n): ")
	if breakout is 'n':
		return 0
	username = input("Please enter your username: ")
	password = input("Please enter your password: ")
	confirm = input("Please re-enter your password for confirmation: ")
	if username in credentials:
		print("This username already exists!!! Please try again!")
		reg()
	elif password != confirm:
		print("The passwords did not match. Please try again")
		reg()
	elif len(password) < 8:
		print("Please enter a password that is longer than 8 characters")
		reg()
	else:
		with open('credentials.csv', 'a') as csvfile:
			fieldnames = ['username', 'password']
			writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
			writer.writerow({'username':username,'password':password})
		credentials[username] = password
		return username


banner = '\n\t\tWelcome to the Financial Calculator Program!\n\t\t\t\tVersion 1.0\n\n\t\t\tFeatures Included:\n\n\t\t\t**Account Management**\n\t\t\t**Currency Conversion**\n\t\t\t**Multiple Currency Support**\n\t\t\t**Persisting Database**\n\n\t\tDo you want to sign in (s) or register (r) or quit (q)?\n'
while 1:
	print(banner)	
	signOrReg = input("Please enter s or r or q: ")
	if signOrReg is 's':
		s = signIn()
		if s:
			finance.bank(s)
	elif signOrReg is 'r':
		r = reg()
		if r:
			finance.bank(r)
	elif signOrReg is 'q':
		break
	else:
		print("You did not enter a valid input. Returning to Home Page\n")

