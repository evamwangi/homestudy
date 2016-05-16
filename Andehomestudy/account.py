class Account(object):
	"""docstring for Account"""
	def __init__(self, holder,balance,number,credit_line=1500):
		self.Holder = holder
		self.Balance = balance
		self.Number = number
		self.Credit_line = credit_line

	def deposit(self,amount):
		self.Balance = amount

	def withdraw(self,amount):
		if (self.Balance - amount < self.Credit_line):
			return False
		else:
			self.Balance -= amount
			return true

	def balance(self):
		return self.Balance

	def transfer(self, target, amount):
		if(self.Balance - amount < self.Credit_line):
			return False
		else:
			self.Balance -= amount
			target.Balance += amount
			return True
			return true


		
		