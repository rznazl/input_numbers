num1= int(input("Please insert a number: ")) #this will be the dividend
num2= int(input("Please insert another number: ")) #this will be the divisor
remainder= num1 % num2

if num2 == 0:
    print("Error: Divisor cannot be zero, result will be undefined.")
elif remainder > 0:
    print(f"The remainder of the 2 numbers is {remainder}.")
else:
    print("The remainder is zero.")


