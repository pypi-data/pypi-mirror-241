import re
from typing import Any, Callable, Iterable


def only(func: Callable[[Any], bool], values: Iterable):
    """Checks if exactly only one item in values has truth

    Args:
        func:
        values (Iterable): iterable of values to check for

    Returns:
        bool: True if 1 else False
    """
    return len(list(filter(func(), values))) == 1


def slugify(text: str, replacement_char: str = "_", max_length: int = None) -> str:
    """
    Normalizes a string by
    Removing all special characters and replacing with a specified character
    Changing all cases to lower case
    Truncating the resulting string to a specified maximum length
    """
    text = text.strip().lower()
    text = re.sub(r"[^\w\s]", replacement_char, text)
    text = re.sub(r"[\s]+", replacement_char, text)
    if max_length is not None and len(text) > max_length:
        text = text[:max_length]
    return text


__all__ = ["only", "slugify"]
