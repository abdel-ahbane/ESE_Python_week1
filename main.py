# This script calculates the factorial of a given int number.
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(f"The factorial of {n} is {factorial}")