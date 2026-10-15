
def binary_search(arr, tar):
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if arr[mid] == tar:
            return mid
        elif arr[mid] < tar:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1


arr = [10, 20, 30, 40, 50, 60, 70]
tar = int(input("Enter target: "))

idx = binary_search(arr, tar)
print("Index:", idx)
