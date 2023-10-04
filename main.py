from slot_machine import *
from get_prompts import *

def main():
	get_greeting()
	balance = deposit()
	while True:
		print(f"Current balance is ${balance}")
		print("Note: Press q to quit")
		wait = input("Press enter to spin!")
		if wait == "q":
			exit()
		balance += spin(balance)
	print(f"You left with ${balance}")
main()