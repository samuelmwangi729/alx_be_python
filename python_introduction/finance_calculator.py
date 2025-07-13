#!/usr/bin/python
Income=int(input("Enter your monthly income:"))
Expenses=int(input("Enter your total monthly expenses:"))
Savings = Income-Expenses
print(f"Your monthly savings are ${Savings}.\n")
YearlySaving = int(Savings * 12 + (Savings * 12 * 0.05))
print(f"Projected savings after one year, with interest, is: ${YearlySaving}.")