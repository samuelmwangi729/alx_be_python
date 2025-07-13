#!/usr/bin/python
Income=int(input("Enter your monthly income\n"))
Expenses=int(input("Enter your total monthly expenses\n"))
Savings = Income-Expenses
YearlySaving = int(Savings * 12 + (Savings * 12 * 0.05))
print(f"Projected savings after one year, with interest, is: ${YearlySaving}.")