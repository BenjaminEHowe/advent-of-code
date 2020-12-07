import unittest
from day07 import Day07


class TestStringMethods(unittest.TestCase):

    def test_example_part_one(self):
        challenge = Day07("example.txt")
        self.assertEqual(challenge.getPartOne(), 4)

    
    def test_example_part_two(self):
        challenge = Day07("example2.txt")
        self.assertEqual(challenge.getPartTwo(), 126)


    def test_real_part_one(self):
        challenge = Day07("input.txt")
        self.assertEqual(challenge.getPartOne(), 226)

    
    def test_real_part_two(self):
        challenge = Day07("input.txt")
        self.assertEqual(challenge.getPartTwo(), 9569)


if __name__ == '__main__':
    unittest.main()
