# Define category class with attributes for category name and list of associated 
# expenses

class Category:
    def __init__(self,name):
        self.name = name
        self.expenses = []

    def add_expense(self, description, amount, date):
        # Get the list of expenses using a for loop and append it to the list
        # Then return the result to pass to the next function
        expenses = []
        expenses_costs = []
        expense_index = int(input("Please enter the number of expenses: "))
        for index, x in enumerate(range(expense_index), start=1):
            # Gets the name of the expense
            expense = input(f"Please enter expense {index}: ")
            expenses.append(expense)
            # Gets the costs of each expense
            expense_cost = float(input(f"Please enter the cost of {expense}: $"))
            expenses_costs.append(expense_cost)
        return expenses, expenses_costs 


    def calculate_total_expenses(self):
        expenses, expenses_costs = Category.add_expense()
        print(expenses)
        print(expenses_costs)
        total_cost = sum(expenses_costs)
        print(f"${total_cost}")





    def list_expenses():
        pass
        

# Define expense class with attributes for the description, amount, and date
# description, amount, and date are attributes
# use a constructor
class Expense:
    def __init__(self, description, amount, date):
        self.description = description
        self.amount = amount
        self.data = date


Category.calculate_total_expenses()