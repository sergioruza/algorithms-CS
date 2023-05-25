from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    message = "Hello, World!"
    key = 4
    expected_result = "!dlroW ,o_lleH"
    assert encrypt_message(message, key) == expected_result


# print(encrypt_message("hello world", 5))
