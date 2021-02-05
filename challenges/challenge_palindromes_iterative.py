def is_palindrome_iterative(word):

    if not word:
        return False

    word_array = list(word)

    for index, value in enumerate(word_array):
        if value == word_array[-1 - index]:
            pass
        else:
            return False

    return True
