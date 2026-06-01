# TextLoom

[![Lint](https://github.com/avtomatik/textloom/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/avtomatik/textloom/actions/workflows/ci.yml)
[![Python Version](https://img.shields.io/pypi/pyversions/textloom)](https://pypi.org/project/textloom/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/textloom?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=downloads)](https://pepy.tech/projects/textloom)

Lightweight text processing utilities for Python.

TextLoom provides a small collection of reusable tools for:

* Transliteration
* Text normalization
* Identifier generation
* Filename normalization
* Name deduplication

The library was extracted from larger data-processing projects to provide a focused and **dependency-free toolkit** for text handling.

## Installation

```bash
pip install textloom
````

## Usage

```python
import textloom as tl
```

### Transliteration

```python
tl.transliterate("Привет Мир")
# "Privet Mir"
```

### Text normalization

```python
tl.normalize_text("  Привет   Мир  ")
# "privet mir"
```

### Identifier normalization

```python
tl.normalize_identifier("Цена товара")
# "tsena_tovara"
```

### Filename normalization

```python
tl.normalize_filename("Мой файл.xlsx")
# "moy-fayl.xlsx"
```

### Deduplication

```python
tl.deduplicate_names(["name", "name", "name"])
# ["name", "name_2", "name_3"]
```

## Design Goals

* Zero runtime dependencies
* Predictable behavior
* Small, intuitive API
* Reusable across projects
* Easy to extend

## License

MIT License. See the [LICENSE](LICENSE) file for details.
