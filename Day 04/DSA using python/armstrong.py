
def is_armstrong(n):
    if n < 0:
        return False

    ds = str(n)
    pw = len(ds)
    sm = sum(int(d) ** pw for d in ds)

    return sm == n


n = int(input("Enter number: "))
print("Armstrong" if is_armstrong(n) else "Not Armstrong")
