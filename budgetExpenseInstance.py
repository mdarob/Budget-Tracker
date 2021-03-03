import sqlite3 as sq

from BudgetExpense import BudgetExpense

'''
sumAll Function adds all the expense/budget values and returns the total
'''
def sumAll(rent, insurance, food, internet, phoneBills, entertainment, shopping, pocketMoney, mischellaneous):
    total = 0
    total = rent + insurance + food + internet + phoneBills + entertainment + shopping + pocketMoney + mischellaneous
    return total

'''
result Funciton takes the total budget amount, total expense and calculates the user whether overbudgeted or underbudgeted 
Params: allBudget must be total of AllBudget, allExpense must be the total of AllExpense
'''
def result(allBudget, allExpense):
    if (allExpense) > (allBudget):
        result = allExpense - allBudget
        print(f"Your overall spending is more than your budget by ${result}")
    else: 
        result = allBudget - allExpense
        print(f"Good Job! You are on top of your budget by ${result}")  

'''
This program uses the BudgetExpense Class to save budget/expense to the Database. The user must enter year and month for budget but 
no need to enter for expense. This program asks to enter year, month, rent, insurance, ... etc. Then, it will save data to Database and print 
a result for the user by each variable. For example, if the rent expense is higher than the rent budget then it will print a message with the 
overspending amount.  
'''

print("#########################################################")
print("Enter your budget by year, month, .. (e.g. 2021, Jan, ..)")
print("#########################################################")

year_budget = int(input("Enter the year : "))
month_budget = str(input("Enter the month : "))
rent_budget = float(input("Enter the rent : $"))
insurance_budget = float(input("Enter the insurance : $"))
food_budget = float(input("Enter the food : $"))
internet_budget = float(input("Enter the internet : $"))
phoneBills_budget = float(input("Enter the phone bill : $"))
entertainment_budget = float(input("Enter the entertainment : $"))
pocketMoney_budget = float(input("Enter the pocketMoney : $"))
shopping_budget = float(input("Enter the shopping : $"))
mischellaneous_budget = float(input("Enter the mischellaneous : $"))

BudgetExpense.saveBudgetToDatabase(year_budget, month_budget, rent_budget, insurance_budget, food_budget, internet_budget, phoneBills_budget, entertainment_budget, shopping_budget, pocketMoney_budget, mischellaneous_budget)

allBudget = sumAll(rent_budget, insurance_budget, food_budget, internet_budget, phoneBills_budget, entertainment_budget, shopping_budget, pocketMoney_budget, mischellaneous_budget)

print("All budget : $", allBudget)

print("###########################################################")
print("Enter your exepense by year, month, .. (e.g. 2021, Jan, ..)")
print("###########################################################")

year_expense = year_budget
month_expense = month_budget

rent_expense = float(input("Enter the rent : $"))
insurance_expense = float(input("Enter the insurance : $"))
food_expense = float(input("Enter the food : $"))
internet_expense = float(input("Enter the internet : $"))
phoneBills_expense = float(input("Enter the phone bill : $"))
entertainment_expense = float(input("Enter the entertainment : $"))
pocketMoney_expense = float(input("Enter the pocketMoney : $"))
shopping_expense = float(input("Enter the shopping : $"))
mischellaneous_expense = float(input("Enter the mischellaneous : $"))

BudgetExpense.saveExpenseToDatabase(year_expense, month_expense, rent_expense, insurance_expense, food_expense, internet_expense, phoneBills_expense, entertainment_expense, shopping_expense, pocketMoney_expense, mischellaneous_expense)

allExpense = sumAll(rent_expense, insurance_expense, food_expense, internet_expense, phoneBills_expense, entertainment_expense, shopping_expense, pocketMoney_expense, mischellaneous_expense)

print("All Expense : $", allExpense)

result(allBudget, allExpense)

BudgetExpense.BudgetCalculationByCol(rent_budget, rent_expense, "rent")
BudgetExpense.BudgetCalculationByCol(food_budget, food_expense, "food")
BudgetExpense.BudgetCalculationByCol(insurance_budget, insurance_expense, "insurance")
BudgetExpense.BudgetCalculationByCol(internet_budget, internet_expense, "internet")
BudgetExpense.BudgetCalculationByCol(phoneBills_budget, phoneBills_expense, "phoneBills")
BudgetExpense.BudgetCalculationByCol(entertainment_budget, entertainment_expense, "entertainment")
BudgetExpense.BudgetCalculationByCol(mischellaneous_budget, mischellaneous_expense, "mischellaneous")
BudgetExpense.BudgetCalculationByCol(pocketMoney_budget, pocketMoney_expense, "pocket money")
BudgetExpense.BudgetCalculationByCol(shopping_budget, shopping_expense, "shopping")        
