import unittest
import luhnmod10

class TestMethods(unittest.TestCase):
    def test_valid(self):
        tests = [
          ("0", True),
          ("00", True),
          ("18", True),
          ("0000000000000000", True),
          ("4242424242424240", False),
          ("4242424242424241", False),
          ("4242424242424242", True),
          ("4242424242424243", False),
          ("4242424242424244", False),
          ("4242424242424245", False),
          ("4242424242424246", False),
          ("4242424242424247", False),
          ("4242424242424248", False),
          ("4242424242424249", False),
          ("42424242424242426", True),
          ("424242424242424267", True),
          ("4242424242424242675", True),
          ("000000018", True),
          ("99999999999999999999", True),
          ("99999999999999999999999999999999999999999999999999999999999999999997", True),
        ]

        for t in tests:
            number, expected_valid = t
            valid = luhnmod10.valid(number)
            self.assertEqual(valid, expected_valid, "Luhn.valid?(%(number)s) == %(valid)s, expected %(expected_valid)s" % locals())

if __name__ == '__main__':
    unittest.main()
