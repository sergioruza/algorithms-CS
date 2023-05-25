from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    message = "Hello, World!"
    assert encrypt_message(message, 4) == "!dlroW ,o_lleH"
    assert encrypt_message(message, 3) == "leH_!dlroW ,ol"
    assert encrypt_message(message, 50) == "!dlroW ,olleH"

    with pytest.raises(TypeError):
        encrypt_message(message, "44")


print(encrypt_message("hello world", 50))
