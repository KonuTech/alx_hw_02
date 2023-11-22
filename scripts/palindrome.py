import re


def is_palindrome(text):
    # Removing punctuation and white spaces
    text = re.sub(r"[^a-zA-Z0-9]", "", text.lower())
    # Checking if the text is equal to its reversed version
    return text == text[::-1]


def test_is_palindrome():
    """
    Function to test the 'is_palindrome' function.
    """
    assert is_palindrome("kajak") is True
    assert is_palindrome("Kajak") is True
    assert is_palindrome("Kobyła ma mały bok") is True
    assert is_palindrome("Kobyła, ma mały bok!") is True
    assert is_palindrome("Sator arepo tenet opera rotas") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("12321") is True
    assert is_palindrome("A man, a plan, a canal, Panama") is True
    assert is_palindrome("Madam, in Eden, I'm Adam") is True
    assert is_palindrome("Palindrome") is False


# Testing is_palindrome function
test_is_palindrome()
