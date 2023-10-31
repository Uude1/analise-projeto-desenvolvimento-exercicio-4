from encrypt import encryptThis

def test_encryptThis_empty_string():
    assert encryptThis("") == ""

def test_encryptThis_single_letter_word():
    assert encryptThis("A") == "65"

def test_encryptThis_two_letter_word():
    assert encryptThis("ab") == "97ba"

def test_encryptThis_example_cases():
    assert encryptThis("Hello") == "72olle"
    assert encryptThis("good") == "103doo"
    assert encryptThis("hello world") == "104olle 119drlo"