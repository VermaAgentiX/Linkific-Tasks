def fibonacci(count):
    if count < 1:
        raise ValueError("Enter a positive number of terms.")
    vals = []
    a, b = 0, 1
    for _ in range(count):
        vals.append(a)
        a, b = b, a + b
    return vals

if __name__ == "__main__":
    count = int(input("How many terms? "))
    print(*fibonacci(count), sep=", ")
