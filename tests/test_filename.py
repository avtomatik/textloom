import textloom as tl


def test_filename():
    assert tl.normalize_filename("Мой файл.xlsx") == "moy-fayl.xlsx"
    assert tl.normalize_filename("My File.xlsx") == "my-file.xlsx"
