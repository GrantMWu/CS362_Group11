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
        # Remove the negative sign for processing
        num_str = num_str[1:]

    # Handle hexadecimal numbers
    if num_str.lower().startswith("0x"):
        hex_part = num_str[2:]  # Extract the hexadecimal part
        # Validate hexadecimal characters
        if not hex_part or any(c not in "0123456789abcdefABCDEF" for c in hex_part):
            return None
        # Convert hex string to integer manually
        result = 0
        for c in hex_part:
            # Convert each character to its decimal equivalent
            result = result * 16 + (ord(c) - ord('0') if '0' <= c <= '9' else ord(c.lower()) - ord('a') + 10)
        return -result if is_negative else result

    # Validate decimal format (only one dot and all other characters must be digits)
    if num_str.count('.') > 1 or not all(c.isdigit() or c == '.' for c in num_str):
        return None

    # Convert to float if it contains a decimal point
    if '.' in num_str:
        # Split the string at the decimal point
        integer_part, decimal_part = num_str.split('.')
        # Convert the integer part manually
        integer_value = sum((ord(c) - ord('0')) * (10 ** i) for i, c in
                            enumerate(reversed(integer_part))) if integer_part else 0
        # Convert the decimal part manually
        decimal_value = sum((ord(c) - ord('0')) * (10 ** -(i + 1)) for i, c in
                            enumerate(decimal_part)) if decimal_part else 0
        result = integer_value + decimal_value
        return -(result) if is_negative else result

    # Process as integer if no decimal point is found
    return (-1 if is_negative else 1) * sum((ord(c) - ord('0')) * (10 ** i) for i, c in enumerate(reversed(num_str)))

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
    # check if endian is valid value
    if endian not in ('big', 'little'):
        return None

    # check if number is positive or negative
    sign = '-' if num < 0 else ''
    num = abs(num)
    hex_bytes = []

    # edge case of 0
    if num == 0:
        return '00'

    # accumulate bytes into hex_bytes
    while num > 0:
        byte = ''
        for i in range(2):
            hex_dig = num % 16
            hex_char = chr(hex_dig + 48) if hex_dig < 10 else chr(hex_dig + 55)
            byte = hex_char + byte
            num //= 16

        hex_bytes.append(byte)

    # adjust hex_bytes for endianess
    if endian == 'big':
        hex_bytes.reverse()

    return sign + ' '.join(hex_bytes)
