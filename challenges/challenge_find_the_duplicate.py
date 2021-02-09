def find_duplicate(nums):
    nums.sort()
    duplicate = 0
    for i in range(0, len(nums) - 1):
        if nums[i] == nums[i + 1]:
            duplicate = nums[i]
            break
        else:
            duplicate = False

    return duplicate