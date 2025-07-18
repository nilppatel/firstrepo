amount = int(input("Enter amount: "))

start = 1
denominations = []

while start != 0:
    start = int(input("Enter denomination 1 by 1 (Enter '0' to stop): "))

    if start != 0:
        denominations.append(start)

denominations.sort(reverse=True)

count = 0
remaining = amount

for denomination in denominations:
    temp = remaining // denomination
    count = count + temp
    remaining = remaining - temp * denomination

    if remaining == 0:
        print(f"Minimum {count} coins required.")
        break

else:
    print("Amount is not possible with provided denominations.")