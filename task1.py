import unittest
from functions import Position, a, b, c, d, my_list


class Test(unittest.TestCase):

    def test_parsing_name1(self):
        self.assertEqual(Position.get_full_name(a), 'ilia kvetenadze')

    def test_parsing_name2(self):
        self.assertNotEqual(Position.get_full_name(a), 'kvetenadze ilia')

    def test_parsing_income1(self):
        self.assertEqual(Position.get_total_income(a), 7000)

    def test_parsing_income2(self):
        self.assertNotEqual(Position.get_total_income(a), 6000)

    def test_bool1(self):
        self.assertTrue(Position.get_total_income(a))

    def test_bool2(self):
        self.assertFalse(
            Position.get_total_income(a) - Position.get_total_income(b))

    def test_is(self):
        self.assertIs(a, c)

    def test_is_not(self):
        self.assertIsNot(a, b)

    def test_is_notnone(self):
        self.assertIsNotNone(a)

    def test_is_instance(self):
        self.assertIsInstance(a, Position)

    def test_assert_raises(self):
        with self.assertRaises(Exception):
            a - b

    def test_in(self):
        self.assertIn(a, my_list)

    def test_not_in(self):
        self.assertNotIn(d, my_list)


if __name__ == '__main__':
    unittest.main()
