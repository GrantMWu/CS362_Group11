import unittest
from task import conv_num


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


if __name__ == '__main__':
    unittest.main()
