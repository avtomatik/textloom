import textloom as tl


def test_identifier():
    assert tl.normalize_identifier("Revenue ($)") == "revenue"
    assert tl.normalize_identifier("___A___") == "a"
    assert tl.normalize_identifier("Цена товара") == "tsena_tovara"
    assert tl.normalize_identifier("") == ""
