from whiteboard import solution
import unittest 


class Testatt(unittest.TestCase):
    def test_one(self):
        str1 = "PPALLP"
        self.assertEqual(solution(str1), True)

    def test_two(self):
        str1 = "PPALLL"
        self.assertEqual(solution(str1), False)

    def test_three(self):
        str1 = "PPALlLL"
        self.assertEqual(solution(str1),  True)


if __name__ == '__main__':
    unittest.main()