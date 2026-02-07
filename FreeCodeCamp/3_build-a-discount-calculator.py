# ============================================================
# Build a Discount Calculator
# ============================================================
#
# In this lab you will write a function that calculates the
# final price of an item after applying a percentage discount.
#
# For example:
#   If the price of an item is 50 and a discount of 20 is applied,
#   the discount amount is 10, and the final price is 40.
#
# ------------------------------------------------------------
# Objective
# ------------------------------------------------------------
# Fulfill the user stories below to complete the lab.
#
# ------------------------------------------------------------
# User Stories
# ------------------------------------------------------------
# - You should define a function named apply_discount.
#
# - The apply_discount function should take exactly two
#   parameters:
#       price
#       discount
#
# - If price is not a number (int or float), the function should
#   return:
#       The price should be a number.
#
# - If discount is not a number (int or float), the function
#   should return:
#       The discount should be a number.
#
# - If price is less than or equal to 0, the function should
#   return:
#       The price should be greater than 0.
#
# - If discount is less than 0 or greater than 100, the function
#   should return:
#       The discount should be between 0 and 100.
#
# - If both inputs are valid, the function should calculate the
#   discount as a percentage of the price.
#
# - The function should return the final price after applying
#   the discount.
#
# ------------------------------------------------------------
# Tests
# ------------------------------------------------------------
# Waiting: 1. You should have a function named apply_discount.
#
# Waiting: 2. Your apply_discount function should take two
#             parameters: price and discount.
#
# Waiting: 3. When apply_discount is called with a price (first
#             argument) that is not a number (int or float),
#             it should return:
#             The price should be a number.
#
# Waiting: 4. When apply_discount is called with a discount
#             (second argument) that is not a number (int or
#             float), it should return:
#             The discount should be a number.
#
# Waiting: 5. When apply_discount is called with a price lower
#             than or equal to 0, it should return:
#             The price should be greater than 0.
#
# Waiting: 6. When apply_discount is called with a discount
#             lower than 0 or greater than 100, it should
#             return:
#             The discount should be between 0 and 100.
#
# Waiting: 7. apply_discount(100, 20) should return 80.
#
# Waiting: 8. apply_discount(200, 50) should return 100.
#
# Waiting: 9. apply_discount(50, 0) should return 50.
#
# Waiting: 10. When apply_discount is called with a discount
#              of 100, it should return 0.
#
# Waiting: 11. apply_discount(74.5, 20.0) should return 59.6.
#
# ============================================================

def apply_discount(price, discount):
    if not isinstance(price, (int, float)):
        return "The price should be a number"
    if not isinstance(discount, (int, float)):
        return "The discount should be a number"
    if price <= 0:
        return "The price should be greater than 0"
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"
    discount_amount = price * (discount/100)
    final_price = price - discount_amount
    return final_price

print(apply_discount(100, 20))
print(apply_discount(200, 50))
print(apply_discount(50, 0))
print(apply_discount(74.5, 20.0))
