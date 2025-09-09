"""
PE1 2.6: Interacting with the User: Input
Assignment: Budget Breakdown Calculator

This program asks the user for their total monthly budget (net income)
and spending in different categories. It then calculates:
1. The percentage of the budget spent in each category.
2. The total spent across all categories.
3. The amount of money left over.

Author: Raed Kiswani
Date: 2025
"""

# Prompt the user to enter their total monthly budget
total_budget = float(input("Enter your total monthly budget (net income): $"))

# Ask the user for spending in different categories
housing = float(input("Enter your housing costs (rent/mortgage): $"))
utilities = float(input("Enter your utilities costs: $"))
groceries = float(input("Enter your groceries costs: $"))
transportation = float(input("Enter your transportation costs: $"))
health_care = float(input("Enter your health care costs: $"))
personal_care = float(input("Enter your personal care costs: $"))
clothing = float(input("Enter your clothing costs: $"))
debt = float(input("Enter your debt payments: $"))

# Calculate total spent
total_spent = (housing + utilities + groceries + transportation +
               health_care + personal_care + clothing + debt)

# Calculate remaining budget
remaining = total_budget - total_spent

# Display percentages for each category
print("\n📊 Budget Breakdown 📊")
print(f"Housing:        {housing/total_budget*100:.2f}%")
print(f"Utilities:      {utilities/total_budget*100:.2f}%")
print(f"Groceries:      {groceries/total_budget*100:.2f}%")
print(f"Transportation: {transportation/total_budget*100:.2f}%")
print(f"Health Care:    {health_care/total_budget*100:.2f}%")
print(f"Personal Care:  {personal_care/total_budget*100:.2f}%")
print(f"Clothing:       {clothing/total_budget*100:.2f}%")
print(f"Debt:           {debt/total_budget*100:.2f}%")

# Print totals
print("\n💰 Total spent: $" + str(total_spent))
print(f"💵 Money left: ${remaining:.2f}")

# TODO: Add more categories like Entertainment or Savings in the future
