import unittest
from day06 import Day06


class TestStringMethods(unittest.TestCase):

    def test_example_part_one(self):
        challenge = Day06("example.txt")
        self.assertEqual(challenge.getPartOne(), 11)

    
    def test_example_part_two(self):
        challenge = Day06("example.txt")
        self.assertEqual(challenge.getPartTwo(), 6)


    def test_real_part_one(self):
        challenge = Day06("input.txt")
        self.assertEqual(challenge.getPartOne(), 6625)

    
    def test_real_part_two(self):
        challenge = Day06("input.txt")
        self.assertEqual(challenge.getPartTwo(), 3360)


if __name__ == '__main__':
    unittest.main()
