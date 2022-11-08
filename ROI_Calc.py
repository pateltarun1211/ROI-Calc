from time import sleep
from IPython.display import clear_output

class calculator:
    def __init__(self):
        self.ROI = 0
        self.incomes = 0
        self.expenses = 0
        self.total_investment = 0
        self.cash_flow = 0
        self.cashROI = 0
        self.income_dict = {}
        self.expense_dict = {}
        self.invest_dict = {}

    
    def total_income(self):
        print("\n----- ADD INCOME SOURCES -----\n")
        print("\n{:<15} {:<8}".format('Income Source','Amount'))
        for k, v in self.income_dict.items():
            print("\n- {:<15} {:<8}".format(k.title(), v))
        while True:
            inc_action = input("\nWould you like to add an income source (Y/N)? ").lower().strip()
            if inc_action == 'y':
                inc_name = input("\nEnter name of income source: ").lower().strip()
                inc_value = input(f"\nEnter amount for '{inc_name.title()}': ").lower().strip()
                self.income_dict[inc_name] = float(inc_value)
            elif inc_action == 'n':
                break
            else:
                print("\nPlease choose a valid response")
        print("\n{:<15} {:<8}".format('Income Source','Amount'))
        for k, v in self.income_dict.items():
            print("\n- {:<15} {:<8}".format(k.title(), v))
        self.incomes = sum(self.income_dict.values())
        print(f"\nYour total monthly income: ${self.incomes}")

    def remove_income(self):
        print("\n----- REMOVE INCOME SOURCES -----\n")

        print("{:<15} {:<8}".format('Income Source','Amount'))
        for k, v in self.income_dict.items():
            print("\n- {:<15} {:<8}".format(k.title(), v))
        if self.income_dict == {}:
            print("\nYou have not entered any income sources!")
            return
        while True:
            del_inc = input("\nEnter which income source you would like to remove (type return to exit): ").lower().strip()
            if del_inc in self.income_dict.keys():
                del_confirm = input(f"\nAre you sure you want to delete '{del_inc.title()}' from income (Y/N)? ").lower().strip()
                if del_confirm == 'y':
                    del self.income_dict[del_inc]
                elif del_confirm == 'n':
                    print(f"\n'{del_inc.title()}' was NOT removed.")
            elif del_inc == 'return':
                self.incomes = sum(self.income_dict.values())
                return
            else:
                ("Invalid Option")
    
    def total_expenses(self):
        print("\n----- ADD EXPENSES -----\n")
        print("\nEnter your monthly expenses for the property")
        print("{:<15} {:<8}".format('Expense','Amount'))
        for k, v in self.expense_dict.items():
            print("\n- {:<15} {:<8}".format(k.title(), v))
        while True:
            exp_action = input("\nWould you like to add an expense (Y/N)? ").lower().strip()
            if exp_action == 'y':
                exp_name = input("\nEnter name of expense: ").lower().strip()
                exp_value = input(f"\nEnter amount for '{exp_name.title()}': ").lower().strip()
                self.expense_dict[exp_name] = float(exp_value)
            elif exp_action == 'n':
                break
            else:
                print("\nPlease choose a valid response")
                
        self.expenses = sum(self.expense_dict.values())

        print("{:<15} {:<8}".format('Expense','Amount'))
        for k, v in self.expense_dict.items():
            print("\n- {:<15} {:<8}".format(k.title(), v))

        print(f"\nYour total monthly expenses: ${self.expenses}")

    def remove_expenses(self):
        print("\n----- Remove Expenses -----\n")

        print("{:<15} {:<8}".format('Expense','Amount'))
        for k, v in self.expense_dict.items():
            print("\n- {:<15} {:<8}".format(k.title(), v))
        if self.expense_dict == {}:
            print("\nYou have not entered any expenses!")
            return
        else:
            while True:
                del_exp = input("\nEnter which expense you would like to remove (type return to exit): ").lower().strip()
                if del_exp in self.expense_dict.keys():
                    del_confirm = input(f"\nAre you sure you want to delete '{del_exp.title()}' from expenses (Y/N)? ").lower().strip()
                    if del_confirm == 'y':
                        del self.expense_dict[del_exp]
                    elif del_confirm == 'n':
                        print(f"\n'{del_exp.title()}' was NOT removed.")
                elif del_exp == 'return':
                    self.expenses = sum(self.expense_dict.values())
                    return
                else:
                    ("Invalid Option")

                print("{:<15} {:<8}".format('Expense','Amount'))
                for k, v in self.expense_dict.items():
                    print("\n- {:<15} {:<8}".format(k, v))


    def total_investments(self):
        print("\n----- ADD INVESTMENTS -----\n")
        print("\nEnter your fixed investments for the property")
        print("{:<15} {:<8}".format('Investment','Amount'))
        for k, v in self.invest_dict.items():
            print("\n- {:<15} {:<8}".format(k.title(), v))
        while True:
            inv_action = input("\nWould you like to add a fixed investment (Y/N)? ").lower().strip()
            if inv_action == 'y':
                inv_name = input("\nEnter name of Investment: ").lower().strip()
                inv_value = input(f"\nEnter amount for {inv_name}: ").lower().strip()
                self.invest_dict[inv_name] = float(inv_value)
            elif inv_action == 'n':
                break
            else:
                print("\nPlease choose a valid response")
                
        self.total_investment = sum(self.invest_dict.values())

        print("{:<15} {:<8}".format('Investment','Amount'))
        for k, v in self.invest_dict.items():
            print("\n- {:<15} {:<8}".format(k.title(), v))

        print(f"\nYour total Fixed Investments: ${self.total_investment}")

    def remove_investments(self):
        print("----- Remove Investments -----")
        print("{:<15} {:<8}".format('Investment','Amount'))
        for k, v in self.invest_dict.items():
            print("\n- {:<15} {:<8}".format(k.title(), v))
        if self.invest_dict == {}:
            print("\nYou have not entered any expenses!")
            return
        else:
            while True:
                del_inv = input("\nEnter which expense you would like to remove (type return to exit): ").lower().strip()
                if del_inv in self.invest_dict.keys():
                    del_confirm = input(f"\nAre you sure you want to delete {del_inv} from expenses (Y/N)? ").lower().strip()
                    if del_confirm == 'y':
                        del self.expense_dict[del_inv]
                    elif del_confirm == 'n':
                        print(f"\n{del_inv} was NOT removed.")
                elif del_inv == 'return':
                    self.total_investment = sum(self.invest_dict.values())
                    return
                else:
                    ("Invalid Option")

                print("{:<15} {:<8}".format('Investment','Amount'))
                for k, v in self.invest_dict.items():
                    print("\n- {:<15} {:<8}".format(k.title(), v))

    def cashflow(self):
        print("\n----- Cash Flow -----\n")

        if self.incomes <= 0 or self.expenses <= 0:
            print("\nThere is an issue with your income or expenses")
        else:
            self.cash_flow = self.incomes - self.expenses
            print(f"\nCash flow: {self.cash_flow}")
    
    def cashoncashROI(self):
        print("----- Cash on Cash ROI -----")
        self.cashflow()
        print(f"\nYour total investment: ${self.total_investment}")
        self.cashROI = ((self.cash_flow * 12) / self.total_investment) * 100
        print(f"\n Cash on Cash ROI: {self.cashROI}%")


    def run(self):

        print("\nAre you ready to change your life?")
        sleep(0.5)
        print("\nWelcome to the best ROI calculator ever written in python by a Coding Temple Student whose name is Tarun.")
        sleep(0.5)


        print("""\n
        Calculator Functions:

        Calculator Functions:
        1) Income
        2) Expenses
        3) Investments
        4) Cash Flow
        5) ROI
        6) Quit
        7) Display Options
        """)
        self.title = input("\nEnter a title for calculations: ").title()
        while True:
            action = input("\nEnter your option (1, 2, 3, 4, 5, 6, (7 - Display Menu): ")
            if action == '1':
                inc_action = input("\nWould you like to 'add'; 'del'; or 'print' items from Income? ").lower().strip()
                if inc_action == 'add':
                    self.total_income()
                elif inc_action == 'del':
                    self.remove_income()
                elif inc_action == 'print':
                    print("{:<15} {:<8}".format('Income Source','Amount'))
                    for k, v in self.income_dict.items():
                        print("\n- {:<15} {:<8}".format(k.title(), v))
            elif action == '2':
                exp_action = input("\nWould you like to 'add', 'del', or 'print' items from Expenses? ").lower().strip()
                if exp_action == 'add':
                    self.total_expenses()
                elif exp_action == 'del':
                    self.remove_expenses()
                elif exp_action == 'print':
                    print("{:<15} {:<8}".format('Expense','Amount'))
                    for k, v in self.expense_dict.items():
                        print("\n- {:<15} {:<8}".format(k.title(), v))
            elif action == '3':
                inv_action = input("\nWould you like to 'add', 'del', or 'print' items from 'Investments'? ").lower().strip()
                if inv_action == 'add':
                    self.total_investments()
                elif inv_action == 'del':
                    self.remove_investments()
                elif inv_action == 'print':
                    print("{:<15} {:<8}".format('Investment','Amount'))
                    for k, v in self.invest_dict.items():
                        print("\n- {:<15} {:<8}".format(k.title(), v))
            elif action == '4':
                self.cashflow()
            elif action == '5':
                self.cashoncashROI()
            elif action == '6':
                print("\nThanks for using the ROI Calculator")
                with open("Calculated_ROI.txt", "a") as f:
                    print("\nHere are your totals for each category: ")
                    print(f"{self.title}", file=f)
                    print(f"    Income: ${self.incomes}")
                    print(f"    Expenses: ${self.expenses}")
                    print(f"    Cash Flow: ${self.cash_flow}")
                    print(f"    Cash on Cash ROI: {self.cashROI}%")
                    print("Data saved to 'Calculated_ROI.txt'")
                    print(f"\n\n{self.title}", file=f)
                    print(f"Income: ${self.incomes}", file=f)
                    print(f"Expenses: ${self.expenses}", file=f)
                    print(f"Cash Flow: ${self.cash_flow}", file=f)
                    print(f"Cash on Cash ROI: {self.cashROI}%", file=f)
                    print("\n", file=f)
                    print("{:<15} {:<8}".format('Income Source','Amount'), file=f)
                    for k, v in self.income_dict.items():
                        print("\n- {:<15} {:<8}".format(k.title(), v), file=f)
                    print("\n", file=f)
                    print("{:<15} {:<8}".format('Expense','Amount'), file=f)
                    for k, v in self.expense_dict.items():
                        print("\n- {:<15} {:<8}".format(k.title(), v), file=f)
                    print("\n", file=f)
                    print("{:<15} {:<8}".format('Investment','Amount'), file=f)
                    for k, v in self.invest_dict.items():
                        print("\n- {:<15} {:<8}".format(k.title(), v), file=f)
                break
            elif action == '7':
                        print("""\n
                                Calculator Functions:
                                1) Income
                                2) Expenses
                                3) Investments
                                4) Cash Flow
                                5) ROI
                                6) Quit
                                7) Display Options
                                """)
            else:
                print("Invalid input, please choose number from the list!")


test_calc = calculator()
test_calc.run()
