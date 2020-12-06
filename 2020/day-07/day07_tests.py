import unittest
from day07 import Day07


class TestStringMethods(unittest.TestCase):

    def test_example_part_one(self):
        challenge = Day07("example.txt")
        self.assertEqual(challenge.getPartOne(), None)

    
    @unittest.skip("Not yet completed part one")
    def test_example_part_two(self):
        challenge = Day07("example.txt")
        self.assertEqual(challenge.getPartTwo(), None)


    @unittest.skip("Not yet completed example part one")
    def test_real_part_one(self):
        challenge = Day07("input.txt")
        self.assertEqual(challenge.getPartOne(), None)

    
    @unittest.skip("Not yet completed example part two")
    def test_real_part_two(self):
        challenge = Day07("input.txt")
        self.assertEqual(challenge.getPartTwo(), None)


if __name__ == '__main__':
    unittest.main()
