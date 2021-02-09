def is_palindrome_recursive(word, low=0, high=-1):
    if not word:
        return False

    mid = len(word) // 2

    if word[low] != word[high]:
        return False

    elif low == mid:
        return True

    low += 1
    high -= 1

    return is_palindrome_recursive(word, low, high)