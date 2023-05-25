def is_anagram(first_string, second_string):
    if (
        len(first_string) != len(second_string)
        or first_string == ""
        or second_string == ""
    ):
        return False

    first_string = list(first_string.lower())
    second_string = list(second_string.lower())

    for index in range(len(first_string)):
        for i in range(len(first_string) - index - 1):
            if first_string[i] > first_string[i + 1]:
                first_string[i], first_string[i + 1] = (
                    first_string[i + 1],
                    first_string[i],
                )

    for index in range(len(second_string)):
        for i in range(len(second_string) - index - 1):
            if second_string[i] > second_string[i + 1]:
                second_string[i], second_string[i + 1] = (
                    second_string[i + 1],
                    second_string[i],
                )

    first_word_sort = "".join(first_string)
    second_word_sort = "".join(second_string)
    result = (
        first_word_sort,
        second_word_sort,
        first_word_sort == second_word_sort,
    )
    return result
