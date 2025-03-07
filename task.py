def conv_num(num_str):
    """
    Convert a string into a base 10 number.

    Args:
        num_str (str): String that represents a number.

    Returns:
        int or float: Converted number if possible.
        None if string is invalid.
    """
    pass


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
