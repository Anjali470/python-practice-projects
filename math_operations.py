def is_prime(number):
    if number == 1:
        return "1 is neither prime nor composite"
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False

    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i ==0:
            return False
    return True

def get_primes_in_range(start, end):
    prime_list = []

    for i in range(start, end + 1):
        if is_prime(i):
            prime_list.append(i)

    return prime_list

def is_perfect_number(number):
    total = 1
    for i in range(2, number // 2 + 1):
        if number % i == 0:
           total += i

    if total == number:
        return True
    else:
        return False

def fibonacci(number):

    lst = [0,1]
    if number == 1:
        return list(lst[0])
    elif number == 2:
        return lst
    for i in range(2, number):
        lst.append(lst[i-1] + lst[i-2])
    return lst


def main():
    number = int(input("Enter a number: "))
    if is_prime(number):
        print(f"{number} is a prime number")
    elif not is_prime(number):
        print(f"{number} is not a prime number")
    else:
        print(is_prime(number))

    start = int(input("Enter the start number of your range: "))
    end = int(input("Enter the end number of your range: "))
    if start > end :
        print("End number should be greater than start number")
    else:
        print(f"List of primes in the given range: {get_primes_in_range(start, end)}")

    number = int(input("Enter your number to check for perfect number: "))
    if is_perfect_number(number):
        print(f"{number} is a perfect number")
    else:
        print(f"{number} is not a perfect number")

    number = int(input("Enter your number for fibonacci series: "))
    print(f"Fibonacci series list: {fibonacci(number)}")

if __name__ == "__main__":
    main()