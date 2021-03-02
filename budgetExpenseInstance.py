import sqlite3 as sq

from BudgetExpense import BudgetExpense

'''
sumAll function adds all the expense/budget values and returns the total
'''
def sumAll(rent, insurance, food, internet, phoneBills, entertainment, shopping, pocketMoney, mischellaneous):
    total = 0
    total = rent + insurance + food + internet + phoneBills + entertainment + shopping + pocketMoney + mischellaneous
    return total

'''
result funciton calculate total budget, total expense and tells the user 
whether overbudgeted or underbudgeted 
Params: allBudget must be total of budget, allExpense must be the total of AllExpense
'''
def result(allBudget, allExpense):
    if (allExpense) > (allBudget):
        result = allExpense - allBudget
        print(f"Your overall spending is more than your budget by ${result}")
    else: 
        result = allBudget - allExpense
        print(f"Good Job! You are on top of your budget by ${result}")  

'''
This program uses the BudgetExpense class to save to budget/expense to the DB. The user must enter year and month for budget but 
no need to enter for expense. This program, asks to enter year and month, rent, insurance, ... etc. Then, this program will saves data to DB and prints a result for 
the user by each item. For example, it will compare rent budget and rent expense. If the rent expense is higher than the rent budget then 
it will print a warning message.  
'''

choice = input("Do you want to interact with the database? Y/N : ")
if choice == "Y" or choice == "y":

    print("#########################################################")
    print("Enter your budget by year, month, .. (e.g. 2021, Jan, ..)")
    print("#########################################################")

    year = int(input("Enter the year : "))
    month = str(input("Enter the month : "))
    rent = float(input("Enter the rent : $"))
    insurance = float(input("Enter the insurance : $"))
    food = float(input("Enter the food : $"))
    internet = float(input("Enter the internet : $"))
    phoneBills = float(input("Enter the phone bill : $"))
    entertainment = float(input("Enter the entertainment : $"))
    pocketMoney = float(input("Enter the pocketMoney : $"))
    shopping = float(input("Enter the shopping : $"))
    mischellaneous = float(input("Enter the mischellaneous : $"))

    BudgetExpense.saveBudgetToDatabase(year, month, rent, insurance, food, internet, phoneBills, entertainment, shopping, pocketMoney, mischellaneous)

    allBudget = sumAll(rent, insurance, food, internet, phoneBills, entertainment, shopping, pocketMoney, mischellaneous)

    print("All budget : $", allBudget)

    print("###########################################################")
    print("Enter your exepense by year, month, .. (e.g. 2021, Jan, ..)")
    print("###########################################################")

    year_expense = year
    month_expense = month

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

    allExpense = sumAll(rent_, insurance_, food_, internet_, phoneBills_, entertainment_, shopping_, pocketMoney_, mischellaneous_)

    print("All Expense : $", allExpense)

    result(allBudget, allExpense)

    BudgetExpense.BudgetCalculationByCol(rent, rent_, "rent")
    BudgetExpense.BudgetCalculationByCol(food, food_, "food")
    BudgetExpense.BudgetCalculationByCol(insurance, insurance_, "insurance")
    BudgetExpense.BudgetCalculationByCol(internet, internet_, "internet")
    BudgetExpense.BudgetCalculationByCol(phoneBills, phoneBills_, "phoneBills")
    BudgetExpense.BudgetCalculationByCol(entertainment, entertainment_, "entertainment")
    BudgetExpense.BudgetCalculationByCol(mischellaneous, mischellaneous_, "mischellaneous")
    BudgetExpense.BudgetCalculationByCol(pocketMoney, pocketMoney_, "pocket money")
    BudgetExpense.BudgetCalculationByCol(shopping, shopping_, "shopping")        

elif choice == "N" or choice == "n":
    print("Thanks anyway, have a GOOD DAY!")