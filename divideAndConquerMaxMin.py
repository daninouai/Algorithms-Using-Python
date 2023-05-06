instance = [5, 6, 36, -6, 31, 98, -16, 67]


def divide_max_min(selected_list):
    print(len(selected_list))
    if len(selected_list) == 1:
        return selected_list[0], selected_list[0]
    half = len(selected_list) // 2
    left_max, left_min = divide_max_min(selected_list[:half])
    right_max, right_min = divide_max_min(selected_list[half:])
    maximum = max(left_max, right_max)
    minimum = min(left_min, right_min)
    return maximum, minimum


max_num, min_num = divide_max_min(instance)
print(f'max value is: {max_num} and min value is: {min_num}')
