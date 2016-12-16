import unittest
from engine import judge


class TestJudge(unittest.TestCase):
    def test_accuracy(self):
        audiofile = 2
        self.assertEqual(judge.accuracy(audiofile), 0)


if __name__ == '__main__':
    unittest.main()
