def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])

    return merge(left, right, array.copy())


def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0

    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]

        for left_cursor in range(left_cursor, len(left)):
            merged[left_cursor + right_cursor] = left[left_cursor]

        for right_cursor in range(right_cursor, len(right)):
            merged[left_cursor + right_cursor] = right[right_cursor]

        return merged


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    sorted_first_string = merge_sort([*first_string])
    sorted_second_string = merge_sort([*second_string])

    is_anagram = False

    for index in range(len(sorted_first_string)):
        if sorted_first_string[index] != sorted_second_string[index]:
            is_anagram = False
            break
        else:
            is_anagram = True

    return is_anagram