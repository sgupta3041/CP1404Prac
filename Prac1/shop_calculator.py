total = 0

Number_of_items = int(input("Number of items: "))
while Number_of_items < 0:
    print("Invalid number of items")

    Number = int(input("Number of items: "))
Number_of_items = int(input("Enter the number of items: "))

for i in range(Number_of_items):
    price = float(input("Enter the price: "))
    total += price

if total > 100:
    total *= 0.9

print("Total price for ", Number_of_items, " items is $:", total, sep='')