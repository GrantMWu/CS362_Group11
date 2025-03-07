def conv_num(num_str):
    """
    Convert a string into a base 10 number.

    Args:
        num_str (str): String that represents a number.

    Returns:
        int or float: Converted number if possible.
        None if string is invalid.
    """
    # Check if input is a valid string (non empty)
    if not isinstance(num_str, str) or not num_str.strip():
        return None

    num_str = num_str.strip()
    is_negative = num_str.startswith('-')
    if is_negative:
        num_str = num_str[1:]

    # Hexadecimal processing
    if num_str.lower().startswith("0x"):
        num_str = num_str[2:]  # Remove '0x'
        if not num_str or any(c not in "0123456789abcdefABCDEF" for c in num_str):
            return None
        # Convert hex string to integer manually
        result = 0
        for c in num_str:
            result = result * 16 + (ord(c) - ord('0') if '0' <= c <= '9' else
                                    ord(c.lower()) - ord('a') + 10)
        return -result if is_negative else result

    # Handle decimal and integer numbers
    if num_str.count('.') > 1 or not num_str.replace('.', '').isdigit():
        return None

    # Process floating-point numbers
    if '.' in num_str:
        left, right = num_str.split('.')
        # Convert integer part manually
        int_part = sum((ord(c) - ord('0')) * (10 ** i) for i, c in
                       enumerate(reversed(left))) if left else 0
        # Convert fractional part manually
        frac_part = sum((ord(c) - ord('0')) * (10 ** -i) for i, c in
                        enumerate(right, start=1)) if right else 0
        return -(int_part + frac_part) if is_negative else int_part + frac_part

    # Integer conversion
    result = sum((ord(c) - ord('0')) * (10 ** i) for i, c in enumerate(reversed(num_str)))
    return -result if is_negative else result


def my_datetime(num_sec):
    """
    Convert number of seconds since epoch into a readable date.

    Args:
        num_sec (int): Number of seconds to convert.

    Returns:
        str: Converted date with format MM-DD-YYYY.
    """
    pass


def conv_endian(num, endian='big'):
    """
    Converts an int to a hexadecimal number.

    Args:
        num (int): Number to convert to hexadecimal.
        endian (str, optional): Determines output endianness.
            Values can be either 'big' or 'little'.
            Defaults to 'big'.

    Returns:
        str: Converted hexadecimal number in specified notation.
    """
    pass
