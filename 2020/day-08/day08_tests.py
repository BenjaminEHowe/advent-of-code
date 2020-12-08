import unittest
from day08 import Day08


class TestStringMethods(unittest.TestCase):

    def test_example_part_one(self):
        challenge = Day08("example.txt")
        self.assertEqual(challenge.getPartOne(), 5)


    def test_example_part_two(self):
        challenge = Day08("example.txt")
        self.assertEqual(challenge.getPartTwo(), 8)


    def test_real_part_one(self):
        challenge = Day08("input.txt")
        self.assertEqual(challenge.getPartOne(), 1394)

    
    def test_real_part_two(self):
        challenge = Day08("input.txt")
        self.assertEqual(challenge.getPartTwo(), 1626)


if __name__ == '__main__':
    unittest.main()
