import textloom as tl


def test_normalize_text():
    assert tl.normalize_text("  Hello   World  ") == "hello world"
    assert tl.normalize_text("Привет Мир") == "privet mir"
