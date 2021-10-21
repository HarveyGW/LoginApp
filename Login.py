#############################################
#         Login and Register Program        #
#              Made By Harvey               #
#                                           #
#############################################

# Imports

import replit
from getpass import getpass
from colorama import Fore as a
import hashlib
import os
import secrets

# Outside While Variables

userTable = {}
userTable['user'] = 'password'
salt = secrets.token_hex(8)
imported = False
prevSalt = ''

# Start While

while True:

	# Import File Function

	def importFile():
		filename = input("What is the filename: ")
		try:
			with open(filename, 'r') as f:
				for line in f:
					lines = [x.strip() for x in f.readlines()]
					for i in lines:
						split = i.split(':')
						userTable[split[0]] = split[1]
						print(userTable)
			print(a.GREEN + "Users Imported!\n" + a.WHITE)
			with open(filename + 'salt', 'r') as prvSalt:
				prevSalt = prvSalt.readline()
			return prevSalt
		except:
			replit.clear()
			print(a.RED + "File does not exist!" + a.WHITE)

	# Register Function

	def Register():
		user = input("Enter A Username: ")
		password = getpass("Password: ")
		cnfrm = getpass("Re-Enter Password: ")
		if password == cnfrm:
			replit.clear()
			key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'),
			                          salt.encode('utf-8'), 100000).hex()
			storage = salt + key
			userTable[user] = storage
			print(a.GREEN + "Successfully Registered!\n" + a.WHITE)
		else:
			replit.clear()
			print(a.RED + "Passwords Do Not Match!\n" + a.WHITE)

	# Login Function

	def Login(prevSalt):
		try:
			user = input("Username: ")
			password = getpass("Password: ")
			if prevSalt:
				key = userTable[user][16:]
				if prevSalt + key == userTable[user]:
					replit.clear()
					print(a.GREEN + "You Have Logged In Successfully!\n" +
					      a.WHITE)
				else:
					replit.clear()
					print(a.RED + "Login Attempt Unsuccessful!\n" + a.WHITE)
			else:
				key = userTable[user][16:]
				if salt + key == userTable[user]:
					replit.clear()
					print(a.GREEN + "You Have Logged In Successfully!\n" +
					      a.WHITE)
				else:
					replit.clear()
					print(a.RED + "Login Attempt Unsuccessful!\n" + a.WHITE)
		except:
			replit.clear()
			print(a.RED + "Username or Password Is Incorrect!" + a.WHITE)

	# Save Function

	def save():
		filename = f"save {len(userTable)}"
		with open(filename + 'salt', 'w') as l:
			l.write(salt)
		with open(filename, 'w') as f:
			for item in userTable:
				f.write(f"{item}:{userTable[item]}\n")
			print(a.GREEN + "SAVED! {0}".format(filename) + "\n" + a.WHITE)

	# View The Current Username and Password Dict

	def View():
		print(a.YELLOW + f"{userTable}" + "\n" + a.WHITE)

	q = input("Login, Register, Save, Import, View: ").lower()

	if q == "test":
		test()
	elif q == "save":
		save()
	elif q == "import":
		prevSalt = importFile()
	elif q == "view":
		View()
	elif q == "login":
		Login(prevSalt)
	elif q == "register":
		Register()
	else:
		replit.clear()
		print(a.RED + f"{q} is not a valid input!\n" + a.WHITE)
