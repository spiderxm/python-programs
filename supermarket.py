# import the random module
# use "winnings = random.randint(2, 10)" to generate a random int from 2 - 10 and store in a variable "winnings"
import random

# unit price of a lottery ticket
constant_lottery_unit_price = 2

# unit price of an apple
constant_apple_unit_price = .99

# unit price of a can of beans
constant_canned_beans_unit_price = 1.58

# unit price of a soda
constant_soda_unit_price = 1.23

# the user has initial $5 for shopping
money = 5

# the user has spent $0 initially
money_spent = 0

# the amounts of lottery tickets, apples, cans of beans, and sodas the user has purchased
lottery_amount, apple_amount, canned_beans_amount, soda_amount, winnings = 0, 0, 0, 0, 0


print("Welcome to the supermarket! We have the following items")
print(f" - Lottery Tickets cost : $ {constant_lottery_unit_price} each")
print(f" - Apples cost : $ {constant_apple_unit_price} each")
print(f" - Can of Beans cost: $ {constant_canned_beans_unit_price } each")
print(f" - Soda cost: $ {constant_soda_unit_price} each")


def purchase(price, item_name):
    global money, money_spent
    qty = 0
    print(f"You have $ {money} with you.")
    ans = input(f" Would you like to purchase {item_name}? (y/n) ")

    if ans != 'y' and ans != 'Y':
        print(f"No {item_name}(s) were purchased.")
    else:
        try:
            qty = input(f"How many {item_name} do you want to buy?  ")
            qty = int(qty)
        except ValueError as e:
            print(f"Numerical values only. No {item_name} selected")

        payable_amt = qty * price
        print(f"The user wants to buy {qty} {item_name}. This will cost {payable_amt}")
        if payable_amt > money:
            print("Not enough money")
        else:
            print(f"The user has enough money. {qty} {item_name}(s) purchased.")
            money -= payable_amt
            money_spent += payable_amt
            return qty


print(f"You have $ {money} available.")
x = input("First, do you want to buy a $2 lottery ticket for a chance at winning $2-$10? (y/n)")

# Lottery Ticket Purchase

if x == 'y' or x == 'Y':
    res = random.randint(0, 2)
    money -= constant_lottery_unit_price
    money_spent += constant_lottery_unit_price
    lottery_amount += 1
    if res != 0:
        print("Sorry you did not win the lottery.")
    else:
        winnings = random.randint(2, 10)
        print(f"Congratulations! You won $ {winnings}.")
        money += winnings
else:
    print("No lottery tickets were purchased.")

# Apples Purchase

apple_amount = purchase(constant_apple_unit_price, 'Apples')
canned_beans_amount = purchase(constant_canned_beans_unit_price , 'Can of Beans')
soda_amount = purchase(constant_soda_unit_price, 'Soda')

print(f"Money Left: $ {money}")
print("Lottery ticket(s) purchased: 1")
print("Lottery Winnings: $ " + str(winnings))
print(f"Apple(s) purchased : {apple_amount}")
print(f"Can(s) of Beans purchased : {canned_beans_amount}")
print(f"Soda(s) purchased : {soda_amount}")
print("Good Bye!")
