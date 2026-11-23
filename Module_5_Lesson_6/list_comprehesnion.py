
num = int(input("Enter a number: "))

odd_numbers = [x for x in range(1, num) if x % 2 != 0]

print(odd_numbers)


fruits = ["apple", "banana", "orange", "grape", "mango"]

updated_fruits = [fruit.capitalize() for fruit in fruits]

print(updated_fruits)