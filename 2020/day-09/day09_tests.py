import unittest
from day09 import Day09


class TestStringMethods(unittest.TestCase):

    def test_example_part_one(self):
        challenge = Day09("example.txt", 5)
        self.assertEqual(challenge.getPartOne(), 127)


    def test_example_part_two(self):
        challenge = Day09("example.txt", 5)
        self.assertEqual(challenge.getPartTwo(), 62)


    def test_real_part_one(self):
        challenge = Day09("input.txt", 25)
        self.assertEqual(challenge.getPartOne(), 50047984)


    def test_real_part_two(self):
        challenge = Day09("input.txt", 25)
        self.assertEqual(challenge.getPartTwo(), 5407707)


if __name__ == '__main__':
    unittest.main()
