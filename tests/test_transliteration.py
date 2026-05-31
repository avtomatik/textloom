import textloom as tl


def test_transliterate():
    assert tl.transliterate("Привет") == "Privet"
    assert tl.transliterate("123") == "123"
    assert tl.transliterate("Привет, World!") == "Privet, World!"
    assert tl.transliterate("Ёж") == "Yozh"
    assert tl.transliterate("") == ""
