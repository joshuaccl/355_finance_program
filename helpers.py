import csv

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
		d = input("Do you want to deposit " + currency + str(amount) + "? (y or n): ")
	else:
		print("You did not enter a valid currency type. Exiting deposit service...")
		return 0
	if d is not 'y':
		print("You did not want to deposit, exiting deposit service...")
	else:
		print("Depositing " + currency + str(amount) + "...")
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
		print("Withdrawing " + balances[user][1] + str(amount) + "...")		
	balance = balances[user]
	total = float(balance[0])
	currency = balance[1]
	if total > amount:
		total -= amount
		balance[0] = str(total)
		balances[user] = balance
	else:
		print("You only have " + currency + balance[0] + " in your account. Exiting withrawal service...")
		return 0
	with open('accounts.csv', 'w') as csvfile:
		fieldnames = ['username', 'balance', 'currency']
		writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
		writer.writeheader()
		for key in balances:
			writer.writerow({'username':key,'balance':balances[key][0],'currency':balances[key][1]})


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
	



def writeConversions(conversions):
	with open('conversions.csv', 'w') as csvfile:
		fieldnames = ['type','$','E','C']
		writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
		writer.writeheader()
		for key in conversions:
			writer.writerow({'type':key,'$':conversions[key]['$'],'E':conversions[key]['E'],'C':conversions[key]['C']})

def check(user):
	with open('accounts.csv', 'r') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			if row['username'] == user:
				print("You currently have " + row['currency'] + row['balance'])
				break