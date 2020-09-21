#PROGRAMMER: Frederick Herzog
#DATE: 11-11-2017
#PasswordTester

import string as st 

def read_data(file):
	passwords = []
	for line in file:
		passwords.append(line.strip())
	return passwords


def search_list(password, lst):
	for pswd in lst:
		if pswd == password:
			return True
		

def determine_strength(password):
	# Define dictionary
	numbers = [str(n) for n in range(0,10)]
	symbols = ['!','@','#','$','%','^','&','*','(',')','~','`',',','.','/','?','{','}','<','>','=','+','-','_',':',';']
	letters = list(st.ascii_lowercase)
	upper_letters = list(st.ascii_uppercase)
	# Define Counter variables
	score,num,sym,let,uppr = 0,0,0,0,0
	
	# Check to see how many numbers, symbols, letters, and upper-case letters are in the password
	for ch in password:
		if ch in numbers:
			num+=1
		if ch in symbols:
			sym+=1
		if ch in letters:
			let+=1
		if ch in upper_letters:
			uppr+=1
	
		
	# Determine the score
	if sym >= 2:
		score+=5
	if num >= 3:
		score+=5
	if let > 0 and uppr > 0:
		score+=15
	if num > 0 and let > 0:
		score+=15
	if num > 0 and sym > 0:
		score+=15
	if let > 0 and sym > 0:
		score+=15
	if num > 0 or let > 0:
		if sym == 0:
			score-=10

	score *= 2

	# Determine the strength
	if score > 75:
		return 'strong'
	elif score < 75 and score >= 50:
		return 'good'
	elif score < 50 and score >= 25:
		return 'okay'
	elif score < 25:
		return 'weak'

	
def main():
	strength = ''
	inList = False
	# Open file
	try:
		inFile = open("CROSSWD.txt")
		# Read contents of file into a list
		password_list = read_data(inFile)
		# Get password from user
		password = input("Enter your password: ")
		for ch in password:
			if ch == " ":
				print("Your password cannot contain spaces.")
				password = input("Please Enter another password: ")

		# Search to see if users password is in list
		inList = search_list(password, password_list)
		if inList:
			strength = "weak"
		# If password is not found in list, determine its strength
		else:
			strength = determine_strength(password)

		print("-"*28)
		print("Your password is:    ", strength)
		print("-"*28)

		inFile.close()
	except:
		print("File not found...")

main()
