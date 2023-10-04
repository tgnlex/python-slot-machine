import random
from get_prompts import *

ROWS = 3 
COLS = 3 

symbol_count = {
	"7": 2, 
	"HI": 4,
	"@": 6,
	"X": 8, 
	"#": 10
}
symbol_value = {
	"7": 50, 
	"HI": 25,
	"@": 12.5,
	"X": 7.5, 
	"#": 3
}

#=====================================================#
def deposit():
	while True:
		amount = input("How much would you like to deposit? $")
		if amount.isdigit():
			amount = int(amount)
			if amount > 0:
				break
			else:
				print("Amount must be greater than 0.")
		else:
			print("Please enter a number.")

	return amount


#=====================================================#
def spin(balance):
	while True:
		lines = get_number_of_lines()
		bet = get_bet()
		total_bet = bet * lines
		
		if total_bet > balance:
			print(f"You do not have enough to bet that amount, your current balance is ${balance}")
		else:
			break
	print(f"You are betting ${bet} on ${lines} lines. Total bet is equal to: ${total_bet}")

	slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
	print_slot_machine(slots)
	winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value) 
	print(f"You won ${winnings}.")
	print(f"You won on lines:", *winning_lines)
	return winnings - total_bet
#=====================================================#

def get_slot_machine_spin(rows, cols, symbols):
	all_symbols = []
	for symbol, symbol_count in symbols.items():
		for _ in range(symbol_count):
			all_symbols.append(symbol)

	columns = []
	for _ in range(cols):
		column = []
		current_symbols = all_symbols[:]
		for _ in range(rows):
			value = random.choice(current_symbols)
			current_symbols.remove(value)
			column.append(value)
		columns.append(column)
	return columns

#=====================================================#

def print_slot_machine(columns):
	for row in range(len(columns[0])):
		for i, column in enumerate(columns):
			if i != len(columns) - 1:
				print(column[row],  end="|")
			else:
				print(column[row], end="")
		print()

#=====================================================#

def check_winnings(columns, lines, bet, values):
	winnings = 100
	winning_lines = []
	for line in range(lines):
		symbol = columns[0][line] 
		for column in columns:
			symbol_to_check = column[line]
			if symbol != symbol_to_check:
				break
		else:
			winnings += values[symbol] * bet
			winning_lines.append(lines + 1)
	return winnings, winning_lines


#=====================================================================================================#
