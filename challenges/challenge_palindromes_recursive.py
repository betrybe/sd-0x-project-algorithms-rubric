def is_palindrome_recursive(word, low, high):

    if not word:
        return False

    equal_char = bool()
    if word[low] == word[high]:
        equal_char = True
    else:
        equal_char = False

    if (low + 1) >= high:
        return equal_char
    else:
        return equal_char and is_palindrome_recursive(word, low + 1, high - 1)
