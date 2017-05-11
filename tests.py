import unittest

from experiments import super_add


class TestCase(unittest.TestCase):

    def test_add_4_and_2(self):
        expected = 42
        observed = super_add(4, 2)
        self.assertEqual(expected, observed)
