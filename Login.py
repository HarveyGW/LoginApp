#############################################
#	Login and Register Program          #
#		Made By Harvey		    #
#                                           #
#############################################
import replit
from getpass import getpass
from colorama import Fore as a

userTable={}
userTable['user'] = 'password'
attempts=0
while True:

	def Register():
		user=input("Enter A Username: ")
		password = getpass("Password: ")
		cnfrm = getpass("Re-Enter Password: ")
		if password==cnfrm:
			userTable[user] = password
			replit.clear()
			print(a.GREEN+"Successfully Registered!\n"+a.WHITE)
		else:
			replit.clear()
			print(a.RED+"Passwords Do Not Match!\n"+a.WHITE)

	def Login():
		user=input("Username: ")
		password = getpass("Password: ")
		if user in userTable:
			if password == userTable[user]:
				replit.clear()
				print(a.GREEN+"You Have Logged In Successfully!\n"+a.WHITE)
			else:
				print(a.RED+"Login Attempt Unsuccessful!\n"+a.WHITE)
		else:
			print(a.RED+"Login Attempt Unsuccessful!\n"+a.WHITE)
			if attempts==4:
				print(a.LIGHTRED_EX+"Account Locked!")
			else:
				attempts+=1
	
	def test():
		replit.clear()
		choice=input("Login or Register: ").lower()

		if choice == "login":
			Login()
		elif choice == "register":
			Register()
		else:
			replit.clear()
			print(a.RED+f"{choice} is not a valid input!\n"+a.WHITE)
	
	def importFile():
		filename=input("What is the filename: ")
		with open(filename, 'r') as f:
			for line in f:
				lines = [x.strip() for x in f.readlines()]
				for i in lines:
					split=i.split(':')
					userTable[split[0]]=split[1]
		print(a.GREEN+"Users Imported!\n"+a.WHITE)

	def View():
		print(a.YELLOW+f"{userTable}"+"\n"+a.WHITE)

	q=input("Test, Save, Import, View: ").lower()

	if q == "test":
		test()
	elif q == "save":
		filename=f"save {len(userTable)}"
		with open(filename, 'w') as f:
			for item in userTable:
				f.write(f"{item}:{userTable[item]}\n")
		print(a.GREEN+"SAVED! {0}".format(filename)+"\n"+a.WHITE)
	elif q == "import":
		importFile()
	elif q == "view":
		View()
