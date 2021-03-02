import sqlite3 as sq

class BudgetExpense:

    def __init__(self, year, month, rent, insurance, food, internet, phoneBills, entertainment, shopping, pocketMoney, mischellaneous ):
        self.year = year
        self.month = month
        self.rent = rent
        self.insurance = insurance
        self.food = food
        self.internet = internet
        self.phoneBills = phoneBills
        self.entertainment = entertainment
        self.shopping = shopping
        self.pocketMoney = pocketMoney
        self.mischellaneous = mischellaneous
    
    def saveBudgetToDatabase( year, month, rent, insurance, food, internet, phoneBills, entertainment, shopping, pocketMoney, mischellaneous):
        ''' 
        This function takes year, month, rent, insurance... etc and saves it it to the "budget.db".
        It checks if the budget table exists in the DB, if not then it creates the table. It also searches 
        the DB for the year and month that are provided by the user so that it isn't saving the same year and 
        month twice. If the year and month exists in the DB then it will ask the user to update the year & month 
        data. The user has a choice to update or not update.
        '''
        
        conn = sq.connect('budget.db')
        c = conn.cursor()

        # This is creating budget table in the DB
        c.execute('CREATE TABLE IF NOT EXISTS budget ( year INTEGER, month TEXT, rent REAL, insurance REAL, food REAL, internet REAL, phoneBills REAL, entertainment REAL, shopping REAL, pocketMoney REAL, mischellaneous REAL ) ')

        # This SQL queries the budget table to see if the year & month data exists in budget table
        c.execute("SELECT year, month FROM budget WHERE year='{}' AND month='{}' ".format(year, month) )

        try:
            # This loop is entered if and only if the above query return entered month & year
            # Otherwise, there is an exception thrown by sqlite3 module
            for year_month in c.fetchall():
                year_search = year_month[0]
                month_search = year_month[1]

            # This print statement throws the exception
            print(year_search, month_search) 

            yes_no_input = input(f"Do you want to UPDATE {year} and {month}? Y/N : ")
            
            # If the user chose to update then the year & month are updated to the entered data
            if yes_no_input == "Y" or yes_no_input == "y":
                c.execute("UPDATE budget SET year = '{}', rent ='{}', insurance='{}', food='{}', internet='{}', phoneBills='{}', entertainment='{}', pocketMoney='{}', shopping='{}', mischellaneous='{}' WHERE year='{}' AND month ='{}' ".format(year, rent, insurance, food, internet, phoneBills, entertainment, pocketMoney, shopping, mischellaneous, year, month) )
                
                # This saves to the DB, commit() function must be called otherwise data won't be saved in the table
                conn.commit()
                
            elif yes_no_input == "N" or yes_no_input == "n":
                print(f"You chose not to UPDATE {year} and {month} data.")
        except:
            print(f"This {year} and {month} don't exist in the Budget DB but we are inserting it anyway")

            # This insert data to the table
            c.execute("INSERT INTO budget VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )", ( year, month, rent, insurance, food, internet, phoneBills, entertainment, pocketMoney, shopping, mischellaneous ) )

            conn.commit() 
        
        # This prints the budget table to console
        c.execute('SELECT * FROM budget')
        print(c.fetchall())
        
    def saveExpenseToDatabase( year, month, rent, insurance, food, internet, phoneBills, entertainment, shopping, pocketMoney, mischellaneous):
        ''' 
        This function takes year, month, rent, insurance... etc and saves it it to the expense.db.
        It checks if the expense table exists in the DB, if not then it creates the table. It also searches the DB
        for the year and month that are provided by the user so that it isn't saving the same year and month twice. If the year 
        and month exists in the DB then it will ask the user to update the year & month data. The user has a choice to update or not update.
        '''
        
        conn = sq.connect('expense.db')
        c = conn.cursor()

        # This is creating expense table in the DB
        c.execute('CREATE TABLE IF NOT EXISTS expense ( year INTEGER, month TEXT, rent REAL, insurance REAL, food REAL, internet REAL, phoneBills REAL, entertainment REAL, shopping REAL, pocketMoney REAL, mischellaneous REAL ) ')

        # This SQL queries the expense table to see if the year & month data exists in expense table
        c.execute("SELECT year, month FROM expense WHERE year='{}' AND month='{}' ".format(year, month) )

        try:
            # This loop is entered if and only if the above query return entered month & year
            # Otherwise, there is an exception thrown by sqlite3 module
            for row in c.fetchall():
                year_search = row[0]
                month_search = row[1]
            
            # This print throws the exception
            print(year_search, month_search) 
            
            yes_no_input = input(f"Do you want to UPDATE {year} and {month}? Y/N : ")
            
            # If the user chose to update then the year & month are updated to the entered data
            if yes_no_input == "Y" or yes_no_input == "y":
                c.execute("UPDATE expense SET year = '{}', rent ='{}', insurance='{}', food='{}', internet='{}', phoneBills='{}', entertainment='{}', pocketMoney='{}', shopping='{}', mischellaneous='{}' WHERE year='{}' AND month ='{}' ".format(year, rent, insurance, food, internet, phoneBills, entertainment, pocketMoney, shopping, mischellaneous, year, month) )
                
                # This saves to the DB, commit() function must be called otherwise data won't be saved in the table
                conn.commit()
                
            elif yes_no_input == "N" or yes_no_input == "n":
                print(f"You chose not to UPDATE {year} and {month} data.")
        except:
            print(f"This {year} and {month} don't exist in the Expense DB but we are inserting it anyway")

            # This insert data to the table
            c.execute("INSERT INTO expense VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )", ( year, month, rent, insurance, food, internet, phoneBills, entertainment, pocketMoney, shopping, mischellaneous ) )

            conn.commit() 
        
        # This prints the expense table to console
        c.execute('SELECT * FROM expense')
        print(c.fetchall())
    
    def searchByYearMonth(year, month, budget_or_expense):
        '''
        This searches the desired DB (e.g. expense or budget) to see if the year &
        month exists in the DB 
        @param: searchByYearMonth(2021, "Jan", budget) This will search the budget.db to see 2021 January data are there
        '''

        if budget_or_expense == "budget" or budget_or_expense == "Budget":
            conn = sq.connect('budget.db')
            c = conn.cursor()
            c.execute("SELECT * FROM budget WHERE year='{}' AND month='{}' ".format(year, month) )
            print(c.fetchall())

        elif budget_or_expense == "expense" or budget_or_expense == "Expense":
            conn = sq.connect('expense.db')
            c = conn.cursor()
            c.execute("SELECT * FROM expense WHERE year='{}' AND month='{}' ".format(year, month) )
            print(c.fetchall())

        else: 
            print("Please enter Budget or Expense")

    def BudgetCalculationByCol(budgetCol, expenseCol, anyvalue):
        # calculate and tell user how much overspending or saving by each column
        if expenseCol > budgetCol:
            result = expenseCol - budgetCol
            print(f"You are overspending {anyvalue} by ${result}")
        else: 
            result = budgetCol - expenseCol
            if result == 0:
                print(f"Good Job! Your {anyvalue} budget & expense is the same")
            else:
                print(f"Good Job! You're under spending {anyvalue} by ${result}")