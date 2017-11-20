# 355_finance_program

This is a financial program that has a couple of features. This version you are looking at is currently the second iteration. Version 2.0 has the following features: Account Management, Currency Conversion, Multiple Currency Support, Persisting Database, Add/Remove Users, Transferring funds from account to account, and Salted Passwords. 

# Features

Version 2.0 contains an admin account to manage users. The admin account is able to add and remove users. The admin account also has the privilege of changing the conversion rates as regular users should not be able to affect these. The password for the admin account is “ics3552017”. This is the default password that comes with the program.

Account Mangagement is accomplished through usernames and passwords. Users are able to log in with their previously established usernames or register for a new one. Passwords must be entered two times for confirmation and also they must be longer than 8 characters. Different account users are not able to access the information of other users.

The program currently supports currency conversion. The currency conversions are inputted by the user. The user has two options, they can either upload into the program a previously constructed .csv currency conversion file with the following format.

		type,symbol1,...,symboln
		symbol1,conversion1,...,conversionN

An example currency conversion file is included in this repo "conversions_example.txt" which supports the US Dollar, Euro, and Chinese Yuan.

The program also has support for a persisting database. Every time the program is executed it looks in its directory for a csv file that contains information from previous runs. If a user wants to start over they can delete these csv files that the program creates. The program will create three different files with different purposes. credentials.csv will hold all the accounts of the users along with the passwords. accounts.csv will hold all the balances of the users along with the currency types that their account is currently in. Lastly, conversions.csv holds the currency conversions as previously mentioned.

Transfer of funds from a user to another is done through a regular user’s options. They have the option to deposit money into another account. The program does not allow a user to withdraw from another user’s account. 

Passwords in version 1.0 were easily visible in the .csv file. In version 2.0 the passwords are hashed using SHA-512 with a randomly generated salt.

# Assumptions

In version 2.0 the user can input any number value and is not restricted to a float input. A rounding function is implemented to easily change input to a two decimal place value. The program can not be run multiple times at the same time because locks are not implemented. To sign in to another account the program quits first and the user must re-run the program.

# Installation and Running

There are no dependencies to install in addition to what is already in this repository. The only requirement is that the program is written in python 3.6 so to properly run the application please use python 3.6. To install just clone the repository into your local computer. Then run the command "python financial_program.py" in the directory with the files. Make sure the four other files limited_finance.py, salt.py, finance.py, and helpers.py is also present in the directory.

# Example Runs

If the program is being run for the first time the only option for the program to do anything is for the user to log in as the admin account and add a user. The username is “admin” and the password is “ics3552017”. Once logged in the program prompts you to either load in a conversions file. Provided in the directory is a sample conversion file “conversions_example.txt”. Once done loading in conversions add in a test user with a password. The account will be saved and you may log out. Logging back in allows you to sign in as the user you just created and from here the features provided are deposit money, withdraw money, check account balance, transfer money to another account, and log out. The admin account has access to the options add user, delete user, edit conversions database, and log out.
