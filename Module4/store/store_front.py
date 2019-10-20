"""
Program: store_front.py
Author: Ty Hobbs
Last date modified: 09/18/2019



The purpose of this program is to take in a price, cash coupon amount and a percent coupon and figure the total with tax and shipping.
"""


def calculate_order(price, cash_coupon, percent_coupon):
    if cash_coupon > 0:
        cash_discount_price = price - cash_coupon
        if percent_coupon > 0:
            percent_off = cash_discount_price * percent_coupon
            new_subtotal = cash_discount_price - percent_off
            new_subtotal
        else:
            new_subtotal = cash_discount_price
            new_subtotal
    elif cash_coupon == 0:
        percent_off = price * percent_coupon
        new_subtotal = price - percent_off

    tax = new_subtotal * .06
    new_subtotal = new_subtotal + tax

    if new_subtotal < 10:
        return round(new_subtotal + 5.95, 2)
    elif new_subtotal >= 10 and new_subtotal < 30:
        return round(new_subtotal + 7.95, 2)
    elif new_subtotal >= 30 and new_subtotal < 50:
        return round(new_subtotal + 11.95, 2)
    else:
        return round(new_subtotal, 2)


if __name__ == '__main__':
    price = float(input("Enter the price of the product: "))
    cash_coupon = float(input("Enter the amount of the cash coupon: "))
    percent_coupon = int(input("Enter the percent for the coupon: "))
    percent_coupon = percent_coupon/100

    print("The total is $",calculate_order(price, cash_coupon, percent_coupon))
