def find_duplicate(nums):
    ordered_nums = merge_sort(nums)

    if not nums:
        return False

    for index in range(len(ordered_nums) - 1):

        if (
            type(ordered_nums[index]) != int
            or ordered_nums[index] < 0
            or ordered_nums[index + 1] < 0
        ):
            return False

        if ordered_nums[index] == ordered_nums[index + 1]:
            return ordered_nums[index]


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
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged
