def is_empty_or_whitespace(s: str) -> bool:
    """
    A simple function to determine if a string is empty or made of whitespaces.

    Args:
        s (str):
            The string to validate.

    Returns:
        bool:
    """
    return not s or s.isspace()