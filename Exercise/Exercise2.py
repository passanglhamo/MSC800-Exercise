def fibonacci(n):
    """Print Fibonacci series up to N."""
    a, b = 0, 1

    print("Fibonacci series:")
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b
    print()


def factorial(n):
    """Calculate factorial of N."""
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


def main():
    """Main function of the program."""
    n = int(input("Enter a number (N): "))

    fibonacci(n)

    fact = factorial(n)
    print(f"Factorial of {n} is: {fact}")


if __name__ == "__main__":
    main()