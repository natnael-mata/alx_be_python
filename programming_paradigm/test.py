import unittest

class DemoTest(unittest.TestCase):

    def setUp(self):
        print("👉 setUp() runs before each test")
        self.value = 10

    def test_first(self):
        print("Running test_first")
        self.assertEqual(self.value, 10)

    def test_second(self):
        print("Running test_second")
        self.assertTrue(self.value > 5)

    def tearDown(self):
        print("👋 tearDown() runs after each test\n")

if __name__ == "__main__":
    unittest.main()