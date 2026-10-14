def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    ans = 1
    for i in range(2, n + 1):
        ans *= i
    return ans

if __name__ == "__main__":
    n = int(input("Enter a non-negative integer: "))
    print(f"{n}! = {factorial(n)}")
