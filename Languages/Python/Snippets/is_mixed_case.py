def is_mixed_case(s: str) -> bool:
    """
    Returns `True` if a string uses lower and upper case characters, `False` 
    otherwise.

    Example:
        >>> is_mixed_case("Hello")
        True
        >>> is_mixed_case("HELLO")
        False

    Args:
        s (str):
        
    Returns:
        bool
    """
    return s.islower() is False and s.isupper() is False and s.lower() != s.upper()