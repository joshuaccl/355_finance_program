# Financial Calculator
# Author: Joshua Lam
# Date: 10/14/17

import csv

credentials = {}
try:
	csvfile = open('credentials.csv', 'r')
except IOError:
	csvfile = open('credentials.csv', 'w')
	fieldnames = ['username', 'password']
	writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
	writer.writeheader()
reader = csv.DictReader(csvfile)
try:
	for row in reader:
		credentials[row['username']] = row['password']
except IOError:
	donothing = 3

def signIn():
	username = input("Please enter your username: ")
	password = input("Please enter your password: ")
	if username in credentials:
		if password == credentials[username]:
			print('Logging in...\n\n')
			return 1
		else:
			print('Incorrect username and password combination\n\n')
			return 0	
	else:
		callReg = input("Username does not exist. Do you want to create a new account? (y or n): ")
		if callReg is 'y':
			reg()
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
		return 1


banner = '\n\t\tWelcome to the Financial Calculator Program!\n\t\t\t\tVersion 1.0\n\n\t\t\tFeatures Included:\n\n\t\t\t**Account Management**\n\t\t\t**Currency Conversion**\n\t\t\t**Multiple Currency Support**\n\t\t\t**Persisting Database**\n\n\t\tDo you want to sign in (s) or register (r) or quit (q)?\n'
while 1:
	print(banner)	
	signOrReg = input("Please enter s or r or q: ")
	if signOrReg is 's':
		if signIn():
			print('call next function')
	elif signOrReg is 'r':
		if reg():
			print('call next function')
	elif signOrReg is 'q':
		break
	else:
		print("You did not enter a valid input. Returning to Home Page\n")

