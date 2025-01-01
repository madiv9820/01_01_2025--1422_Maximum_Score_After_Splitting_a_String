from timeout_decorator import timeout
from Solution import Solution
import unittest

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testcases = {1: ('011101', 5), 2: ('00111', 5), 
                            3: ('1111', 3), 4: ('00', 1)}
        self.__obj = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_case_1(self):
        s, output = self.__testcases[1]
        result = self.__obj.maxScore(s = s)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_case_2(self):
        s, output = self.__testcases[2]
        result = self.__obj.maxScore(s = s)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_case_3(self):
        s, output = self.__testcases[3]
        result = self.__obj.maxScore(s = s)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_case_4(self):
        s, output = self.__testcases[4]
        result = self.__obj.maxScore(s = s)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

if __name__ == '__main__': unittest.main()