def find_duplicates(arr):
    seen = set()
    dup = []

    for x in arr:
        if x in seen and x not in dup:
            dup.append(x)
        else:
            seen.add(x)

    return dup


arr = [1, 2, 3, 2, 4, 5, 1]

print("Input:", arr)
print("Duplicates:", find_duplicates(arr))