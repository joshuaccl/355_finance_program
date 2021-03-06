# File: helpers.py
# Author: Joshua Lam

import csv
import salt

# Deposit amount into user account
def deposit(user, conversions):
	amount = float(input("How much would you like to deposit? Please only enter a numeric number with two decimal places for example 5 dollars will be 5.00. I will ask you for the currency type later. "))
	try:
		amount += 0.0
	except TypeError:
		print("You did not enter a number. Exiting deposit service...")
		return 0
	if amount <= 0:
		print("You cannot deposit no or negative money. Exiting deposit service...")
		return 0
	currency = input("What kind of money are you depositing? ( USD ($), EURO (E), Chinese currency (C): ")
	if currency is '$' or currency is 'E' or currency is 'C':
		d = input("Do you want to deposit " + currency + round(amount) + "? (y or n): ")
	else:
		print("You did not enter a valid currency type. Exiting deposit service...")
		return 0
	if d is not 'y':
		print("You did not want to deposit, exiting deposit service...")
	else:
		print("Depositing " + currency + round(amount) + "...")
		balances = {}
		with open('accounts.csv', 'r') as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				balances[row['username']] = [row['balance'],row['currency']]
	balance = balances[user]
	total = float(balance[0])
	if balance[1] == currency:
		total += amount
		balance[0] = str(total)
		balances[user] = balance
	else:
		currencies = conversions[currency]
		conversion = float(currencies[balance[1]])
		amount *=  conversion
		total += amount
		balance[0] = str(total)
		balances[user] = balance
	with open('accounts.csv', 'w') as csvfile:
		fieldnames = ['username', 'balance', 'currency']
		writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
		writer.writeheader()
		for key in balances:
			writer.writerow({'username':key,'balance':balances[key][0],'currency':balances[key][1]})

# Withdraw amount from a users account
def withdraw(user, conversions):
	amount = float(input("How much would you like to withdraw? Please only enter a numeric number with two decimal places. For example 5 dollars would be 5.00. "))
	try:
		amount += 0.0
	except TypeError:
		print("You did not enter a number. Exiting withdrawal service...")
		return 0
	if amount <= 0.0:
		print("You cannot withdraw no or negative money. Exiting withdrawal service...")
		return 0
	else:
		balances = {}
		with open('accounts.csv', 'r') as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				balances[row['username']] = [row['balance'],row['currency']]
		type_of_currency = input("What kind of currency do you want your withdrawal in? ( USD ($), EURO (E), Chinese Currency (C))")
		if type_of_currency != '$' and type_of_currency != 'E' and type_of_currency != 'C':
			print("You did not enter a valid currency. Exiting withdrawal service...")
			return 0
		print("Withdrawing " + type_of_currency + round(amount) + "...")		
	balance = balances[user]
	total = float(balance[0])
	currency = balance[1]
	currencies = conversions[type_of_currency]
	amount *= float(currencies[currency])
	if total >= amount:
		total -= amount
		balance[0] = str(total)
		balances[user] = balance
	else:
		print("You only have " + currency + round(balance[0]) + " in your account. Exiting withrawal service...")
		return 0
	with open('accounts.csv', 'w') as csvfile:
		fieldnames = ['username', 'balance', 'currency']
		writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
		writer.writeheader()
		for key in balances:
			writer.writerow({'username':key,'balance':balances[key][0],'currency':balances[key][1]})

# Called when user wants to add in their own conversions
def maintenance(conversions):
	if not conversions:
		setup = input("Would you like to upload some conversions from a file? (y or n): ")
		if setup is 'y':
			filename = input("Please enter the filename: ")	
			try:
				with open(filename, 'r') as csvfile:
					reader = csv.DictReader(csvfile)
					for row in reader:
						conversions[row['type']] = {'$':row['$'], 'E':row['E'], 'C':row['C']}
				writeConversions(conversions)
				return conversions
			except IOError:
				tryAgain = input("The file does not exist. Are you sure you spelled it correct? Do you want to try again? (y or n): ")
				if tryAgain is 'y':
					return maintenance(conversions)
				else:
					conversions = userinput()
					writeConversions(conversions)
					return conversions
		else:
			conversions =  userinput()
			writeConversions(conversions)
			return conversions
			
# Asks user for input for maintenance function
def userinput():
	ue = float(input("How many Euros are in a US Dollar? "))
	uc = float(input("How many Chinese Yuans are in a US Dollar? "))
	eu = float(input("How many US Dollars are in a Euro? "))
	ec = float(input("How many Chinese Yuans are in a Euro? "))
	cu = float(input("How many US Dollars are in a Chinese Yuan? "))
	ce = float(input("How many Euros are in a Chinese Yuan? "))
	try:
		ue += 0.0
		uc += 0.0
		eu += 0.0
		ec += 0.0
		cu += 0.0
		ce += 0.0
		return {'$':{'$':1,'E':ue,'C':uc},'E':{'$':eu,'E':1,'C':ec},'C':{'$':cu,'E':ce,'C':1}}
	except TypeError:
		print("You did not enter correct conversion values. Please try again")
		return userinput()

# When new conversions are made this function writes it to file
def writeConversions(conversions):
	with open('conversions.csv', 'w') as csvfile:
		fieldnames = ['type','$','E','C']
		writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
		writer.writeheader()
		for key in conversions:
			writer.writerow({'type':key,'$':conversions[key]['$'],'E':conversions[key]['E'],'C':conversions[key]['C']})

# Checks the balance of a given user
def check(user):
	with open('accounts.csv', 'r') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			if row['username'] == user:
				print("You currently have " + row['currency'] + round(row['balance']))
				break

# Changes an input value into a monetary value. i.e. two decimal places
def round(money):
	listx = list(str(money))
	for i in range(0, len(listx)):
		if listx[i] == '.':
			break
	if len(listx) == i+1:
		listx.append('.')
		listx.append('0')
		listx.append('0')
		return ''.join(listx)
	elif len(listx) == i + 2:
		listx.append('0')
		return ''.join(listx)
	else:
		return ''.join(listx[0:i+3])

# Delete a user from the database
def deleteUser():
	credentials = {}
	accounts = {}
	with open('credentials.csv', 'r') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			credentials[row['username']] = [row['hash'], row['salt']]
	print("The users in the database are...")
	for key in credentials:
		print(key)
	with open('accounts.csv', 'r') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			accounts[row['username']] = [row['balance'], row['currency']]
	whom = input("Which user do you want to delete?: ")
	if whom == 'admin':
		print("You cannot delete the admin account")
		return 0
	if whom in credentials:
		del credentials[whom]
		del accounts[whom]
		with open('credentials.csv', 'w') as csvfile:
			fieldnames = ['username', 'hash', 'salt']
			writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
			writer.writeheader()
			for key in credentials:
				writer.writerow({'username':key, 'hash':credentials[key][0],'salt':credentials[key][1]})
		with open('accounts.csv', 'w') as csvfile:
			fieldnames = ['username', 'balance', 'currency']
			writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
			writer.writeheader()
			for key in accounts:
				writer.writerow({'username':key, 'balance': accounts[key][0], 'currency': accounts[key][1]})
	else:
		print("That user does not exist in the database")
	
# Function to register a new account	
def reg():
	credentials = {}
	with open('credentials.csv', 'r') as csvfile:
        	reader = csv.DictReader(csvfile)
        	for row in reader:
                	credentials[row['username']] = [row['hash'], row['salt']]
	breakout = input("Do you really want to register an account? (y or n): ")
	if breakout is 'n':
        	return 0
	elif breakout is not 'y':
        	print("You did not input a y")
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
                	fieldnames = ['username', 'hash', 'salt']
                	writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
                	newSalt = salt.getSalt()
                	writer.writerow({'username':username,'hash':salt.getHash(password,newSalt), 'salt':newSalt})
		credentials[username] = [salt.getHash(password,newSalt), newSalt]
		return username

# Transfers money from one account to another

def transfer(user):
	accounts = {}
	with open('accounts.csv', 'r') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			accounts[row['username']] = [float(row['balance']), row['currency']]
	if len(accounts) == 1:
		print("No other accounts available to transfer money to")
	print("The available accounts to transfer money to are...")
	for key in accounts:
		print(key)
	whom = input("Which account do you want to transfer your money too? ")
	if whom not in accounts:
		print("That is not a valid account. Exiting...")
		return 0
	amount = float(round(input("How much money would you like to transfer from your account to " + key + "? ")))
	try:
		amount += 0.00
	except TypeError:
		print("You did not enter a valid monetary amount. Exiting...")
		return 0
	if amount < 0:
		print("You cannot transfer anything less than 0. Exiting...")
		return 0
	type_curr = input("What type of money do you want to transfer? USD ($) , EURO (E) , Chinese Currency (C) ")
	if type_curr != '$' and type_curr != 'E' and type_curr != 'C':
		print("You did not enter a valid currency type. Exiting...")
		return 0
	print("Now transferring " + type_curr + round(amount) + " to " + whom)
	conversions = {}
	with open('conversions.csv', 'r') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			conversions[row['type']] = {'$':row['$'], 'E':row['E'], 'C':row['C']}
	currencies = conversions[type_curr]
	conversionRate = float(currencies[accounts[user][1]])
	withdrawal = amount * conversionRate
	if withdrawal > (accounts[user][0]):
		print("You did not have enough funds in your account. Exiting...")
		return 0
	else:
		accounts[user][0] -= withdrawal
		withdrawal = withdrawal * float(conversions[accounts[user][1]][accounts[whom][1]])
		accounts[whom][0] += withdrawal
		with open('accounts.csv', 'w') as csvfile:
			fieldnames = ['username', 'balance', 'currency']
			writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
			writer.writeheader()
			for key in accounts:
				writer.writerow({'username':key,'balance':accounts[key][0],'currency':accounts[key][1]})




