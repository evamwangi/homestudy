class Customer(object):
	"""docstring for Customer"""
	def __init__(self, name, balance):
		self.name = name
		self.balance = balance

	def deposit(self,amount):
		self.balance += amount
		return self.balance

	def withdraw(self,amount):
		if amount > self.balance:
			raise RuntimeError ('amount larger than the available amount')
		else:
			self.balance -= amount

		return self.balance

l = Customer("eva",1000)
print l.deposit(1000)
print l.withdraw(1000)






		