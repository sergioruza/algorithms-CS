def sort(str):
    str_list = list(str)

    for i in range(1, len(str_list)):
        letter = str_list[i]
        count = i - 1

        while count >= 0 and str_list[count] > letter:
            str_list[count + 1] = str_list[count]
            count -= 1

        str_list[count + 1] = letter

    return "".join(str_list)


def is_anagram(first_string, second_string):
    first_string = first_string.replace(" ", "").lower()
    second_string = second_string.replace(" ", "").lower()

    first_sorted = sort(first_string)
    second_sorted = sort(second_string)

    return (first_sorted, second_sorted, first_sorted == second_sorted)


# referencia de ajuda ChatGPT da OpenAI
