num1= int(input("Give me a number: ")) #this number should be smaller than num2 
num2= int(input("Give me another number: "))
print(f"The number between the two numbers is/are: ")

for i in range(num1+1, num2):
    print(i)