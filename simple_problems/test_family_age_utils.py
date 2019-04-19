# Making functions to mess with a dictionary of names to ages
import unittest
from simple_problems.family_age_utils import FamilyAgeUtils

family = dict(Elliot=27, Oliver=23, Max=25, Ben=26, Simon=20, Mumsie=49, Phoebe=18, Fatherman=52)


class TestFamilyAgeUtils(unittest.TestCase):

    def test_total_age(self):
        self.assertEqual(FamilyAgeUtils.total_age(family), 240)

    def test_average_age(self):
        self.assertEqual(FamilyAgeUtils.average_age(family), 30)

    def test_total_age_div_by_2(self):
        self.assertEqual(FamilyAgeUtils.total_age_div_by_2({'cat': 1, 'dog': 2, 'elliot': 3}, True), 2)
        self.assertEqual(FamilyAgeUtils.total_age_div_by_2({'cat': 1, 'dog': 2, 'elliot': 3}, False), 4)

    def test_sort_by_age(self):
        self.assertEqual(FamilyAgeUtils.sort_by_age({'cat': 2, 'dog': 1, 'elliot': 3}),
                         [('dog', 1),('cat', 2),('elliot', 3)])
        self.assertEqual(FamilyAgeUtils.sort_by_age({'cat': 2, 'dog': 1, 'rabbit': 2, 'elliot': 3}),
                         [('dog', 1),('cat', 2),('rabbit', 2),('elliot', 3)])
    def test_closest_age(self):
        self.assertEqual(FamilyAgeUtils.closest_age({'cat': 1, 'dog': 5, 'elliot': 10}, 7), ['dog'])
        self.assertEqual(FamilyAgeUtils.closest_age({'cat': 1, 'dog': 5, 'fish': 5, 'elliot': 10}, 7), ['dog', 'fish'])


if __name__ == '__main__':
    unittest.main()
