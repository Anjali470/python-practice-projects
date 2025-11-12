def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        result = "Sorry!! you cannot divide a number by zero"
        return result

def power(base, exponent):
    return base ** exponent

def modulus(num1, num2):
    return num1 % num2
def main():

    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Power\n6. Modulus\n7. Exit")

    while True:

        choice = int(input("Enter your choice (1-7): "))

        if choice not in (1, 2, 3, 4, 5, 6, 7):
            print("Enter a correct choice")
            continue
        elif choice == 7:
            print("Exiting from the calculator")
            break

        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if choice == 1:
            result = add(num1, num2)
            print(f"Addition of {num1} and {num2} is {result}")
        elif choice == 2:
            result = subtract(num1, num2)
            print(f"Subtraction of {num1} and {num2} is {result}")
        elif choice == 3:
            result = multiply(num1, num2)
            print(f"Multiplication of {num1} and {num2} is {result}")
        elif choice == 4:
            result = divide(num1, num2)
            if num2 == 0:
                print(result)
            else:
                print(f"Division of {num1} and {num2} is {result}")
        elif choice == 5:
            result = power(num1, num2)
            print(f"{num1} to the power of {num2} is {result}")
        elif choice == 6:
            result = modulus(num1, num2)
            print(f"Modulus of {num1} and {num2} is {result}")

    pass

if __name__ == "__main__":
    main()