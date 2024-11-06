def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price * discount_percent / 100
        return final_price
    elif discount_percent < 20:
        return price
    else:
        return price


print("Hey! Welcome I can help you calculate discount on prices!!")
print("Please leave out the symbols!! I don't calculate for discount less than 20%!")
user_price = int(input('Enter your price here "e.g 2000" >  '))
user_discount = int(
    input(
        'Enter your discount here "e.g 20" or "0" if you have no discount to apply! >  '
    )
)
calc = calculate_discount(user_price, user_discount)
print(calc)
