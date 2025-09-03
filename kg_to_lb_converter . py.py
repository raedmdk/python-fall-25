#!/usr/bin/env python3
"""
kg_to_lb_converter.py
---------------------

Assignment: Convert kilograms to pounds using variables and formatting.

Directions:
- Use at least four different sample kilogram values.
- Apply the conversion factor: 1 kilogram = 2.20462 pounds.
- Print results using f-strings, formatted to 2 decimal places.
- Follow variable naming rules (lowercase with underscores).
- Submit this file on GitHub.

Author: Raed Kiswani
Date: September 2, 2025
"""

# Conversion factor: 1 kilogram = 2.20462 pounds
conversion_factor = 2.20462

# Sample values in kilograms (choose different ones than the example 5 kg)
kg_value_1 = 10
kg_value_2 = 25.5
kg_value_3 = 50
kg_value_4 = 72.3

# Perform the conversions
lb_value_1 = kg_value_1 * conversion_factor
lb_value_2 = kg_value_2 * conversion_factor
lb_value_3 = kg_value_3 * conversion_factor
lb_value_4 = kg_value_4 * conversion_factor

# Output the results with 2 decimal places
print(f"{kg_value_1} kilograms is equal to {lb_value_1:.2f} pounds.")
print(f"{kg_value_2} kilograms is equal to {lb_value_2:.2f} pounds.")
print(f"{kg_value_3} kilograms is equal to {lb_value_3:.2f} pounds.")
print(f"{kg_value_4} kilograms is equal to {lb_value_4:.2f} pounds.")
