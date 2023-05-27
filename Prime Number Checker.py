def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Test the function
while True:
    try:
        num = int(input("Enter a positive number: "))
        if num <= 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
