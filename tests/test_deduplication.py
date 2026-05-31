import textloom as tl


def test_deduplicate_names():
    assert tl.deduplicate_names(["a", "a", "a"]) == ["a", "a_2", "a_3"]
    assert tl.deduplicate_names(["a", "b", "a"]) == ["a", "b", "a_2"]
    assert tl.deduplicate_names([]) == []
