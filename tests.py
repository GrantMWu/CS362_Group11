import unittest
from task import conv_endian


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


if __name__ == '__main__':
    unittest.main()
