from atm_flow import ATM_features
import unittest



class TestATM(unittest.TestCase):
	def testbalance(self):
		account_no = '1000'
		account_type = 'Checking'
		starting_balance = 1000
		customer_account = ATM_features.account('1234','Checking',1000)	
		balance = customer_account.getBalance()
		self.assertEqual(balance,1000)
	def testwithdraw(self):
		account_no = '1000'
		account_type = 'Checking'
		starting_balance = 1000
		customer_account = ATM_features.account('1234','Checking',1000)	
		customer_account.withdraw(100)
		new_balance = customer_account.getBalance()
		self.assertEqual(new_balance,900)

	def testdeposit(self):
		account_no = '1000'
		account_type = 'Checking'
		starting_balance = 1000
		customer_account = ATM_features.account('1234','Checking',1000)	
		customer_account.Deposit(50)
		new_balance = customer_account.getBalance()
		self.assertEqual(new_balance,1050)


if __name__ == '__main__':
	unittest.main()

