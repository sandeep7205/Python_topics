# ============================================================
# File Name: movie-ticket-booking-calculator.py
# ============================================================
#
# Description:
# This script calculates the final movie ticket price based on
# user eligibility, age restrictions, membership discounts,
# show timing, seat type, and applicable charges.
#
# ============================================================

# Base ticket price
base_price = 15

# User details
age = 21
seat_type = 'Gold'
show_time = 'Evening'

# Eligibility check based on age
if age > 17:
    print('User is eligible to book a ticket')

# Evening show eligibility
if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')

# Membership and weekend status
is_member = False
is_weekend = False

# Discount calculation
discount = 0
if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')

print('Discount:', discount)

# Extra charges calculation
extra_charges = 0
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')

print('Extra charges:', extra_charges)

# Final ticket booking condition
if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    # Service charges based on seat type
    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1

    print('Service charges:', service_charges)

    # Final price calculation
    final_price = (base_price + extra_charges + service_charges) - discount
    print('Final price of ticket:', final_price)

else:
    print('Ticket booking failed due to restrictions')
