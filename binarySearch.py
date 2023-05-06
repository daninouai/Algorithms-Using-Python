arr = [1, 3, 4, 7, 9, 11, 15, 18, 22, 25]


def binary_search(arr, x):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1


index = binary_search(arr, 4)
if index != -1:
    print("number found on ", index)
else:
    print("nothing found")
