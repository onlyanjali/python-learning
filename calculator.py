def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def multi(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

choice = input("Choose operation (+, -, *, /): ")

if choice == "+":
    print(add(num1, num2))

elif choice == "-":
    print(sub(num1, num2))

elif choice == "*":
    print(multi(num1, num2))

elif choice == "/":
    print(div(num1, num2))

else:
    print("Invalid operation")