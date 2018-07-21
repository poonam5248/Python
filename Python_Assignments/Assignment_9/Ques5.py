'''Ques 5. Create a class Expenditure and initialize it with expenditure,savings.Make the following methods.
1. Display expenditure and savings
2. Calculate total salary
3. Display salary'''


class Expenditure:
	def __init__(self,expenditure,savings):
		self.expenditure=expenditure
		self.savings=savings
	def display(self):
		print("Enter Expenditure:",self.expenditure)
		print("Enter Savings: ",self.savings)
	def totalsalary(self):
		salary=self.expenditure+self.savings
		print("Total Salary  =",salary)

expenditure=int(input("Enter  Expenditure:"))
savings=int(input("Enter Savings:"))
s1=Expenditure(expenditure,savings)
s1.display()
s1.totalsalary()