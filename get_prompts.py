MAX_LINES = 3
MAX_BET = 100 
MIN_BET = 1

#=====================================================================================================#


def get_greeting():
	while True:
		invite = input("Would you like to play at this machine? (y/n)")
		if invite == 'y'or invite == 'Y' or invite == 'yes':
			print("Welcome to DIY Slots")
			break
		if invite == 'n' or invite == 'N' or invite == "no":
			print("very well than, have a nice day.")
			exit()
		else:
			print("Please enter yes or no. ")

#=====================================================================================================#

def get_number_of_lines():
	while True:
		lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")")
		if lines.isdigit():
			lines = int(lines)
			if 1 <=  lines <= MAX_LINES:
				break
			else:
				print("Amount must be greater than 0.")
		else:
			print("Please enter a number.")
	return lines

#=====================================================================================================#

def get_bet():
	while True:
		amount = input("What would you like to bet? $")
		if amount.isdigit():
			amount = int(amount)
			if MIN_BET <= amount <+ MAX_BET:
				break
			else:
				print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
		else:
			print("Please enter a number.")
	return amount

#=====================================================================================================#
