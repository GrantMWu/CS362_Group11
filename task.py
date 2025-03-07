def conv_num(num_str):
    """
    Convert a string into a base 10 number.

    Args:
        num_str (str): String that represents a number.

    Returns:
        int or float: Converted number if possible.
        None if string is invalid.
    """
    # Check if input is a valid string and not empty after stripping whitespace
    if not isinstance(num_str, str) or not num_str.strip():
        return None

    num_str = num_str.strip()
    # Check if the number is negative
    is_negative = num_str.startswith('-')
    if is_negative:
        num_str = num_str[1:]

        # Handle hexadecimal numbers
    if num_str.lower().startswith("0x"):
        hex_part = num_str[2:]  # Extract the hexadecimal part
        # Validate hexadecimal characters (only valid hex digits)
        if not hex_part or any(c not in "0123456789abcdefABCDEF" for c in hex_part):
            return None
        # Convert hex string to integer manually
        result = 0
        for i, c in enumerate(reversed(hex_part)):
            if '0' <= c <= '9':
                value = ord(c) - ord('0')
            elif 'a' <= c.lower() <= 'f':
                value = ord(c.lower()) - ord('a') + 10
            else:
                return None
            result += value * (16 ** i)
        return -result if is_negative else result

    return None


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
