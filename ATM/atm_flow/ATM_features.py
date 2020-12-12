
import time

######bank account class with methods for getting balance, withdrawing and depositing cash############# 
class account(object):
	def __init__(self,account_number,account_type,starting_balance):
		#self.id = 'atm1'
		self.account_number = object
		self.account_type = account_type
		self.balance = starting_balance

	def getBalance(self):
		return self.balance

	def withdraw(self,withdraw_amount):
		dispense_cash(withdraw_amount)
		self.balance -= withdraw_amount
		return None
	
	def Deposit(self,deposit):
		self.balance += deposit
		return None


###########ATM machine hardware interface functions###########

def card_reader(card_details):
	account_number = 1234

	return account_number

def dispense_cash(withdraw_amount):
	return None

def verifyDeposit():
	amount = 50

	return amount

############Bank server interface functions###########

def verifyPin(acc_no, PIN):

	return True


#######After integration with Bank, balance can be intialized directly from the server

starting_balance = 1000



############Main ATM function that serves as an interface between customer and bank########

def ATM():
	while True:

		print('please insert your card')
		account_number = card_reader(input())
		time.sleep(1)
		
		
		tries = 3
		while tries > 0 :
			print('please enter your PIN:')
			acc_PIN = input()
			time.sleep(1)
			verifylogin = verifyPin(account_number,acc_PIN)
			if verifylogin == True :
				tries = 0
			elif tries > 0:
				tries -= 1
				print('Wrong PIN, please try again. You have',tries,'tries left')
			else:
				print('failed to login, exiting to main menu')
				break
		if verifylogin == True:
			pass
		else:
			break    #would break outside to main loop

		print('Please select one of the following accounts: 1.Checking, 2.Reserve, 3.Growth')
		account_type = int(input())
		time.sleep(1)

		account_dict = {1 :'Checking',2: 'Reserve', 3:'Growth'}
		
		####initialize the customer_account object
		customer_account = account(account_number,account_dict[account_type],starting_balance)

		while True:
			print('Please select the account action from the list: 1.Check Balance, 2.Withdraw cash, 3.Deposit cash, 4.Exit')
			action = int(input())
			time.sleep(2)
			action_dict = {1:'Check Balance', 2:'Withdraw cash',3:'Deposit cash',4:'Exit'}
			if action == 1:
				balance = customer_account.getBalance()
				print('Your account balance is $', balance)
				print('##########Going back to the previous menu##########')
				time.sleep(1)
				continue
			if action == 2:
				tries = 3
				while tries > 0:
					print('Enter the amount to withdraw')
					withdraw_amount = int(input())
					if 0 < withdraw_amount <= customer_account.getBalance() :

						customer_account.withdraw(withdraw_amount)
						print('Updated balance is $',customer_account.getBalance())
						print('##########Going back to the previous menu##########')
						time.sleep(1)
						break
					elif withdraw_amount > customer_account.getBalance()  :			
						print('The account does not have enough balance to withdraw $',withdraw_amount)
						print('Your account balance is:', customer_account.getBalance())
						tries -= 1
					elif withdraw_amount < 0:
						print('withdrawing amount should be a positive number')
						tries -= 1

			if action == 3:
				print('Enter the deposit')
				print('verifying the deposit amount')
				time.sleep(2)
				amount = verifyDeposit()
				customer_account.Deposit(amount)
				print('You deposited $',amount)
				balance = customer_account.getBalance()
				print('Your updated balance is $',balance)
				print('##########Going back to the previous menu##########')
				time.sleep(1)
			if action == 4:
				print('exiting session')
				time.sleep(1)
				break
			
	
	return None

if __name__ == '__main__':

	###tests
	

	ATM()
	