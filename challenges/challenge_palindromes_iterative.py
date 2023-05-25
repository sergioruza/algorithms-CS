def is_palindrome_iterative(word):
    if word == "":
        return False
    palindrome = word.replace(" ", "").lower()

    invert = palindrome[::-1]

    if word.lower() == invert:
        return True
    else:
        return False
