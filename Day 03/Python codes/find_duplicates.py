def find_duplicates(vals):
    seen = set()
    dup = []
    for val in vals:
        if val in seen and val not in dup:
            dup.append(val)
        else:
            seen.add(val)
    return dup

if __name__ == "__main__":
    vals = [1, 2, 3, 2, 4, 5, 1]
    print("Input:", vals)
    print("Duplicates:", find_duplicates(vals))  # [2, 1]
