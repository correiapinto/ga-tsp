import unittest
from Run import *


class MyTestCase(unittest.TestCase):

    def test_swap(self):
        self.run = Run()

        array_1 = [1,2,3,4,5,6,7]
        i = 1
        j = 4
        print('/nExpected:')
        expected = [1,5,3,4,2,6,7]
        print(expected)
        real = self.run.swap(array_1, i, j)
        print("Real:")
        print(real)

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
        # Todo!
        run = Run()
        array_1 = [1, 2, 3, 4, 5, 6, 7]
        result = run.mutate(array_1)
        print(array_1)
        print(result)
        # the lengths of the lists are the same
        self.assertEqual(len(array_1), len(result))
        # But the order must be different
        self.assertNotEqual(array_1, result)

    def test_crossover(self):
        run = Run()
        p1 = [1,2,3,4,5]
        p2 = [3,2,4,5,1]
        expected = [1,2,3,5,4]
        real = run.crossover(p1,p2)
        print(real)
        self.assertEqual(expected, real)




if __name__ == '__main__':
    unittest.main()
