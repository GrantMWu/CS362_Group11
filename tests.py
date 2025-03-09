import unittest
from task import conv_num, my_datetime, conv_endian


class TestConvNum(unittest.TestCase):

    def test1(self):
        """Test standard positive integer"""
        self.assertEqual(conv_num('12345'), 12345)

    def test2(self):
        """Test negative floating-point number"""
        self.assertEqual(conv_num('-123.45'), -123.45)

    def test3(self):
        """Test floating-point number with no leading digit"""
        self.assertEqual(conv_num('.45'), 0.45)

    def test4(self):
        """Test floating-point number with no trailing digit"""
        self.assertEqual(conv_num('123.'), 123.0)

    def test5(self):
        """Test valid uppercase hexadecimal conversion"""
        self.assertEqual(conv_num('0xAD4'), 2772)

    def test6(self):
        """Test valid lowercase hexadecimal conversion"""
        self.assertEqual(conv_num('0Xad4'), 2772)

    def test7(self):
        """Test valid negative hexadecimal conversion"""
        self.assertEqual(conv_num('-0xAD4'), -2772)

    def test8(self):
        """Test invalid hexadecimal with non-hex character"""
        self.assertIsNone(conv_num('0xAZ4'))

    def test9(self):
        """Test invalid number containing alphabetic character"""
        self.assertIsNone(conv_num('12345A'))

    def test10(self):
        """Test invalid floating-point number with multiple dots"""
        self.assertIsNone(conv_num('12.3.45'))

    def test11(self):
        """Test empty string input"""
        self.assertIsNone(conv_num(''))

    def test12(self):
        """Test input with only whitespace"""
        self.assertIsNone(conv_num('   '))

    def test13(self):
        """Test None as input"""
        self.assertIsNone(conv_num(None))

    def test14(self):
        """Test string 'None' as input"""
        self.assertIsNone(conv_num('None'))

    def test15(self):
        """Test non-string integer input"""
        self.assertIsNone(conv_num(123))

    def test16(self):
        """Test incomplete hexadecimal string"""
        self.assertIsNone(conv_num('0x'))


class TestMyDatetime(unittest.TestCase):
    """Verifies that my_datetime computes the correct datetime from seconds"""

    def test1(self):
        """Tests that 0 seconds returns 01-01-1970."""
        self.assertEqual(my_datetime(0), '01-01-1970')

    def test2(self):
        """Tests 1 day increment to 01-02-1970 at 12AM secs"""
        self.assertEqual(my_datetime(86400), '01-02-1970')

    def test3(self):
        """Tests 3-1 12AM in the first year."""
        self.assertEqual(my_datetime(5097600), '03-01-1970')

    def test4(self):
        """Tests Feb 29 12AM in the first leap year."""
        self.assertEqual(my_datetime(68_169_600), '02-29-1972')

    def test5(self):
        """Tests 1 day at 11:59PM secs"""
        self.assertEqual(my_datetime(172799), '01-02-1970')

    def test6(self):
        """Tests date after first leap year."""
        self.assertEqual(my_datetime(123456789), '11-29-1973')

    def test7(self):
        """Tests date of non-leap year well into the future."""
        self.assertEqual(my_datetime(9876543210), '12-22-2282')

    def test8(self):
        """Tests Feb 29 of leap year well into the future."""
        self.assertEqual(my_datetime(201653971200), '02-29-8360')

    def test9(self):
        """Tests the last second of a month in a year before next leap year."""
        self.assertEqual(my_datetime(168134399), '04-30-1975')

    def test10(self):
        """Tests Feb 29 of the second leap year."""
        self.assertEqual(my_datetime(194450000), '02-29-1976')

    def test11(self):
        """Tests last second of Feb 29 of the second leap year."""
        self.assertEqual(my_datetime(194486399), '02-29-1976')

    def test12(self):
        """Tests first second of 3-1 of the second leap year."""
        self.assertEqual(my_datetime(194486400), '03-01-1976')

    def test13(self):
        """Tests last second of 12-31 of the second leap year."""
        self.assertEqual(my_datetime(220881599), '12-31-1976')


class TestConvEndian(unittest.TestCase):
    """Test conv_endian function"""

    def test1(self):
        """Test invalid endian value"""
        self.assertIsNone(conv_endian(954786, 'small'))

    def test2(self):
        """Test value of 0"""
        self.assertEqual(conv_endian(0), '00')

    def test3(self):
        """Test positive number with even number nibbles in big endian"""
        self.assertEqual(conv_endian(10785661, 'big'), 'A4 93 7D')

    def test4(self):
        """Test positive number with odd number nibbles in big endian"""
        self.assertEqual(conv_endian(954786), '0E 91 A2')

    def test5(self):
        """Test negative number with even number nibbles in big endian"""
        self.assertEqual(conv_endian(-10785661), '-A4 93 7D')

    def test6(self):
        """Test negative number with odd number nibbles in big endian"""
        self.assertEqual(conv_endian(-954786, 'big'), '-0E 91 A2')

    def test7(self):
        """Test positive number with even number nibbles in little endian"""
        self.assertEqual(conv_endian(10785661, 'little'), '7D 93 A4')

    def test8(self):
        """Test positive number with odd number nibbles in little endian"""
        self.assertEqual(conv_endian(954786, 'little'), 'A2 91 0E')

    def test9(self):
        """Test negative number with even number nibbles in little endian"""
        self.assertEqual(conv_endian(-10785661, 'little'), '-7D 93 A4')

    def test10(self):
        """Test negative number with odd number nibbles in little endian"""
        self.assertEqual(conv_endian(-954786, 'little'), '-A2 91 0E')

    def test11(self):
        """Test single byte value"""
        self.assertEqual(conv_endian(255), 'FF')

    def test12(self):
        """Test negative single byte value"""
        self.assertEqual(conv_endian(-255), '-FF')

    def test13(self):
        """Test large number requiring multiple bytes"""
        self.assertEqual(conv_endian(101562942140), '17 A5 9F 82 BC')

    def test14(self):
        """Test named parameters in reversed order"""
        self.assertEqual(conv_endian(endian='big', num=954786), '0E 91 A2')

    def test15(self):
        """Test case sensitivity of endian parameter"""
        self.assertEqual(conv_endian(954786, 'BIG'), None)
        self.assertEqual(conv_endian(954786, 'Little'), None)


if __name__ == '__main__':
    unittest.main()
