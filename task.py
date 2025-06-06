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
        invalid_digs = any(c not in "0123456789abcdefABCDEF" for c in hex_part)
        if not hex_part or invalid_digs:
            return None
        # Convert hex string to integer manually
        result = 0
        for c in hex_part:
            # Convert each character to its decimal equivalent
            if '0' <= c <= '9':
                digit = ord(c) - ord('0')
            else:
                digit = ord(c.lower()) - ord('a') + 10
            result = result * 16 + digit
        return -result if is_negative else result

    # Validate decimal format
    multiple_decimal = num_str.count('.') > 1
    valid_digits = all(c.isdigit() or c == '.' for c in num_str)

    if multiple_decimal or not valid_digits:
        return None

    # Convert to float if it contains a decimal point
    if '.' in num_str:
        # Split the string at the decimal point
        integer_part, decimal_part = num_str.split('.')

        # Convert the integer part manually
        integer_value = sum(
            (ord(c) - ord('0')) * (10 ** i)
            for i, c in enumerate(reversed(integer_part))
        ) if integer_part else 0

        # Convert the decimal part manually
        decimal_value = sum(
            (ord(c) - ord('0')) * (10 ** -(i + 1))
            for i, c in enumerate(decimal_part)
        ) if decimal_part else 0

        result = integer_value + decimal_value
        return -result if is_negative else result

    # Process as integer if no decimal point is found
    integer_value = sum(
        (ord(c) - ord('0')) * (10 ** i)
        for i, c in enumerate(reversed(num_str))
    )

    return -integer_value if is_negative else integer_value


def my_datetime(num_sec):
    """
    Convert number of seconds since epoch into a readable date.

    Args:
        num_sec (int): Number of seconds to convert.

    Returns:
        str: Converted date with format MM-DD-YYYY.
    """
    # Set the year of the date.
    num_sec, year = _increment_year(num_sec)

    # Set the month of the year.
    num_sec, month = _increment_month(num_sec)

    # Set the day of the month.
    num_sec, day = _increment_day(num_sec)

    # Add a day offset for first two months of a leap year.
    if _is_leap_year(year):
        day = _add_offset_day(num_sec, month, day)

    # Format month, if month is a single digit.
    month = _format_single_digit(month + 1)

    # Format day, if day is a single digit.
    day = _format_single_digit(day)

    return '{}-{}-{}'.format(month, day, year)


def _add_offset_day(num_sec, month, day):
    """
    Conditionally increment the day of a leap year.

    Args:
        num_sec (int): Number of seconds remaining in date calculation.
        month (int): The month of the year.
        day (int): The day of the month to increment.

    Returns:
        int: The incremented day of a leap year.
    """
    FEB = 1
    MAX_DAYS = 29

    if num_sec >= 0 and month <= FEB and day <= MAX_DAYS:
        day += 1

    return day


def _increment_year(num_sec):
    """
    Increment the year, starting in 1970, with the given number of seconds.

    Args:
        num_sec (int): Number of seconds with which to increment the year.

    Returns:
        Tuple: (Adjusted num_sec, incremented year).
    """
    SEC_PER_DAY = (24 * 60 * 60)
    YEAR_SECS = (365 * SEC_PER_DAY)
    year = 1970

    while num_sec >= YEAR_SECS:
        year += 1
        if _is_leap_year(year):
            num_sec -= (YEAR_SECS + SEC_PER_DAY)
        else:
            num_sec -= YEAR_SECS

    return num_sec, year


def _increment_month(num_sec):
    """
    Increment the month with the given number of seconds.

    Args:
        num_sec (int): Number of seconds with which to increment the month.

    Returns:
        Tuple: (Adjusted num_sec, incremented month).
    """
    MONTH_DAY_COUNT = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    SEC_PER_DAY = (24 * 60 * 60)
    month = 0

    while num_sec >= (MONTH_DAY_COUNT[month] * SEC_PER_DAY):
        num_sec -= (MONTH_DAY_COUNT[month] * SEC_PER_DAY)
        month += 1

    return num_sec, month


def _increment_day(num_sec):
    """
    Increment the day with the given number of seconds.

    Args:
        num_sec (int): Number of seconds with which to increment the day.

    Returns:
        Tuple: (Adjusted num_sec, incremented day).
    """
    SEC_PER_DAY = (24 * 60 * 60)
    day = 1

    while num_sec >= SEC_PER_DAY:
        num_sec -= SEC_PER_DAY
        day += 1

    return num_sec, day


def _is_leap_year(year):
    """
    Determine if a given year is a leap year.

    Args:
        year (int): The year being considered.

    Returns:
        bool: True, if year is a leap year, otherwise False.
    """
    is_mod_4 = year % 4 == 0
    is_mod_100 = year % 100 == 0
    is_mod_400 = year % 400 == 0

    return (is_mod_4 and not is_mod_100) or (is_mod_400 and is_mod_100)


def _format_single_digit(digit):
    """
    Format a digit as a string, depending on if it's a single digit.

    Args:
        digit (int): The digit being formatted.

    Returns:
        string: A formatted string with the adjusted digit.
    """
    return '{}'.format(digit) if digit >= 10 else '0{}'.format(digit)


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
