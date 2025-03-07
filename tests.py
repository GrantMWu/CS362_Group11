import unittest
from task import conv_num, my_datetime, conv_endian


class TestConvNum(unittest.TestCase):

    def test1(self):
        self.assertEqual(conv_num('12345'), 12345)

    def test2(self):
        self.assertEqual(conv_num('-123.45'), -123.45)

    def test3(self):
        self.assertEqual(conv_num('.45'), 0.45)

    def test4(self):
        self.assertEqual(conv_num('123.'), 123.0)

    def test5(self):
        self.assertEqual(conv_num('0xAD4'), 2772)

    def test6(self):
        self.assertEqual(conv_num('0Xad4'), 2772)

    def test7(self):
        self.assertEqual(conv_num('-0xAD4'), -2772)

    def test8(self):
        self.assertIsNone(conv_num('0xAZ4'))

    def test9(self):
        self.assertIsNone(conv_num('12345A'))

    def test10(self):
        self.assertIsNone(conv_num('12.3.45'))

    def test11(self):
        self.assertIsNone(conv_num(''))

    def test12(self):
        self.assertIsNone(conv_num('   '))

    def test13(self):
        self.assertIsNone(conv_num(None))

    def test14(self):
        self.assertIsNone(conv_num('None'))

    def test15(self):
        self.assertIsNone(conv_num(123))

    def test16(self):
        self.assertIsNone(conv_num('0x'))

class TestMyDatetime(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)


class TestConvEndian(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
