instance = [27, 10, 12, 20, 25, 13, 15, 22]


def merge_sort(list_to_divide):
    len_of_list = len(list_to_divide)

    if len_of_list <= 1:
        return list_to_divide

    middle = len_of_list // 2
    left_of_list = list_to_divide[:middle]
    right_of_list = list_to_divide[middle:]

    left_of_list = merge_sort(left_of_list)
    right_of_list = merge_sort(right_of_list)

    return merge(left_of_list, right_of_list)


def merge(left, right):
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


print(merge_sort(instance))
