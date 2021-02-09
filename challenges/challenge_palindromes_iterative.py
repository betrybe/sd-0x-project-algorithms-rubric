def is_palindrome_iterative(word):
    if not word:
        return False

    mid = len(word) // 2
    low = 0
    high = -1

    while low != mid:
        if word[low] != word[high]:
            return False
        low += 1
        high -= 1

    return True