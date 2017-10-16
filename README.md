# 355_finance_program

This is a financial program that has a couple of features. This version you are looking at is currently the first iteration. Version 1.0 has the following features: Account Management, Currency Conversion, Multiple Currency Support, and Persisting Database. 

# Features

Account Mangagement is accomplished through usernames and passwords. Users are able to log in with their previously established usernames or register for a new one. Passwords must be entered two times for confirmation and also they must be longer than 8 characters. Different account users are not able to access the information of other users.

The program currently supports currency conversion. The currency conversions are inputted by the user. The user has two options, they can either upload into the program a previously constructed .csv currency conversion file with the following format.

		type,symbol1,...,symboln
		symbol1,conversion1,...,conversionN

An example currency conversion file is included in this repo "conversions_example.txt" which supports the US Dollar, Euro, and Chinese Yuan.

The program also has support for a persisting database. Every time the program is executed it looks in its directory for a csv file that contains information from previous runs. If a user wants to start over they can delete these csv files that the program creates. The program will create three different files with different purposes. credentials.csv will hold all the accounts of the users along with the passwords. accounts.csv will hold all the balances of the users along with the currency types that their account is currently in. Lastly, conversions.csv holds the currency conversions as previously mentioned.

# Assumptions

The program has a lot of input validation already but there are some assumptions on the user input. One of these is the assumption that the user will submit amount values with two decimal places. The program will still accept integer values but floats with two decimal places are preferred. Another assumption is that withdrawing can only be done with one type of currency because in real life you are just withdrawing from you bank account.

# Installation and Running

There are no dependencies to install in addition to what is already in this repository. To install just clone the repository into your local computer. Then run the command "python financial_program.py" in the directory with the files. Make sure the two other files finance.py and helpers.py is also present in the directory.

# Example Runs

There are two ways to use this program. When the program starts up it will ask if you want to sign in, register, or quit. Signing in will fail if you do not have an account and thus you will be prompted to make an account. Register will avoid this longer execution. Once registered the program will ask if a currency conversion file will be uploaded into the database. This is the option the user has. If yes, then for an example you can upload the provided file, or upload your own. If no, then the program will ask if you will input your own conversions. Once that is done the program will ask you if you want to create an account because as a new user there is no account found. You can choose the type of currency for the new account. Once this is done the bank interface will show, which includes five commands, Deposit, Withdraw, Check, Maintenance, or Log out. From here the user may choose whatever they please.
