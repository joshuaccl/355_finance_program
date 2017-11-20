# File: finance.py
# Author: Joshua Lam
# File containing finance program that offers services to admin

import csv
import helpers

def bank(user):
	conversions = {}
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

	while 1:
		print("\n\t\t\tYou can either: \n\t\t\tEdit the currency conversions in the database (MAINT)\n\t\t\tAdd a new user (ADD)\n\t\t\tDelete a current user (DEL)\n\t\t\tLog out (LOG)\n")
		action = input("What do you want to do: ")
		if action == 'ADD':
			helpers.reg()
		elif action == 'DEL':
			helpers.deleteUser()
		elif action == 'MAINT':
			conversions = {}
			helpers.maintenance(conversions)
		elif action == 'LOG':
			break
		else:
			print("Sorry I did not understand what you wanted to do. Please try again.")
	
