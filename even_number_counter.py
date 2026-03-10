even_count = 0

print("Please enter 10 numbers: ")

for i in range (1,11):
    number = int(input(f"Enter number {i}: "))

    if number % 2 == 0:
        even_count += 1

print(f"The total of the even numbers are: {even_count}")