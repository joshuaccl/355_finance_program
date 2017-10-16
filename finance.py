# File containing finance program that offers services to user

import csv
import helpers

def bank(user):
	conversions = {}
	accountExists = 0
	try:
		with open('conversions.csv', 'r') as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				conversions[row['type']] = {'$':row['$'],'E':row['E'],'C':row['C']}
	except IOError:
		conversions = helpers.maintenance(conversions)
	try:
		with open('accounts.csv', 'r') as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				if row['username'] == user:
					balance = row['balance']
					currency = row['currency']
					accountExists = 1
					break
	except IOError:
		with open('accounts.csv', 'w') as csvfile:
			fieldnames = ['username', 'balance', 'currency']
			writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
			writer.writeheader()
		accountExists = 0
	if not accountExists:
		newaccount = input("Our records show that you do not have an account with us. Would you like to make one? (y or n): ")
		if newaccount == 'y':
			currency = input('What kind of currency do you want to use? We have support for USD ($), EURO (E), or Chinese currency (C): ')
			if currency is '$' or currency is 'E' or currency is 'C':	
				with open('accounts.csv', 'a') as csvfile:
					fieldnames = ['username', 'balance', 'currency']
					writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
					writer.writerow({'username':user,'balance':0,'currency':currency})
				balance = 0.00
			else:
				print("You did not enter a supported currency. Quitting the Bank Teller...")
				return 0
		else:
			print("Okay returning to log in screen...")
			return 0

	while 1:
		print("\n\t\t\tYou can either: \n\t\t\tCheck your balance (CHECK)\n\t\t\tDeposit money (DEP)\n\t\t\tWithdraw money (WITH)\n\t\t\tEdit the currency conversions in the database (MAINT)\n\t\t\tLog out (LOG)\n")
		action = input("What do you want to do: ")
		if action == 'CHECK':
			helpers.check(user)
		elif action == 'DEP':
			helpers.deposit(user, conversions)
		elif action == 'WITH':
			helpers.withdraw(user, conversions)
		elif action == 'MAINT':
			conversions = {}
			helpers.maintenance(conversions)
		elif action == 'LOG':
			break
		else:
			print("Sorry I did not understand what you wanted to do. Please try again.")
	
