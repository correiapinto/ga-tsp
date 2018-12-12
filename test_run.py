import unittest
from Run import *


class MyTestCase(unittest.TestCase):

    def test_swap(self):
        self.run = Run()

        array_1 = [1,2,3,4,5,6,7]
        i = 1
        j = 4
        expected = [1,5,3,4,2,6,7]
        real = self.run.swap(array_1, i, j)

        self.assertEqual(real, expected)

    def test_pick_two_swappers(self):
        run = Run()
        array_1 = [1, 2, 3, 4, 5, 6, 7]

        real = run.pick_two_swappers(array_1)

        self.assertGreater(real[0], 0)
        self.assertGreater(real[1], 0)
        self.assertLessEqual(real[0], 7)
        self.assertLessEqual(real[1], 7)
        self.assertEqual(len(real), 2)

    def test_mutate(self):
        run = Run()
        array_1 = [1, 2, 3, 4, 5, 6, 7]
        result = run.mutate(array_1)
        self.assertEqual(len(array_1), len(result))
        self.assertNotEqual(array_1, result)




if __name__ == '__main__':
    unittest.main()
