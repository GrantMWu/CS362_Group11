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
    if endian != 'big' and endian != 'little':
        return None

    # check if number is positive or negative
    sign = '-' if num < 0 else ''
    num = abs(num)

    # divide num by 16 until num = 0
    hex_str = ''
    while num != 0:
        # get next hex digit
        hex_dig = num % 16
        hex_dig = hex_dig if hex_dig < 10 else hex_dig + 7
        hex_dig = chr(hex_dig + 48)

        # convert remainder into string and add to current string
        hex_str = hex_dig + hex_str
        num //= 16

    # when string is two digits long, append it to hex list
    # read hex list forwards or backwards depending on endianess
    hex_str = sign + hex_str
    return hex_str


print(conv_endian(954786, endian='big'))
