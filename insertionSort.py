import timeit


def insertion_sort(arr):
    for step in range(1, len(arr)):
        key = arr[step]
        i = step - 1

        while i >= 0 and key < arr[i]:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key


data = [324, 25, 37, 1414, 23]
data2 = [23, 25, 37, 324, 1414]

start = timeit.default_timer()
insertion_sort(data)
print('sorted array(not sorted by me):')
print(data)
stop = timeit.default_timer()
print('Time: ', stop - start)

start = timeit.default_timer()
insertion_sort(data2)
print('sorted array (sorted by me):')
print(data2)
stop = timeit.default_timer()
print('Time: ', stop - start)



