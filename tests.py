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


if __name__ == '__main__':
    unittest.main()
