import unittest
from algo_task import string_parser as sp

class AlgoTest(unittest.TestCase):
    def test_01_ok(self):
        "> }](){"
        string = "}](){"
        get_str = sp(string)
        exp_str = "(){}"       
        self.assertEqual(get_str, exp_str, msg=f"Wait {exp_str}, get: {get_str}")

    def test_02_ok(self):
        "> sh(dh)}"
        string = "sh(dh)}"
        get_str = sp(string)
        exp_str = "sh(dh)"       
        self.assertEqual(get_str, exp_str, msg=f"Wait {exp_str}, get: {get_str}")

    def test_03_ok(self):
        "> ]h({hdb}b)["
        string = "]h({hdb}b)["
        get_str = sp(string)
        exp_str = "Infinite"       
        self.assertEqual(get_str, exp_str, msg=f"Wait {exp_str}, get: {get_str}")


if __name__ == '__main__':
    unittest.main(verbosity=2)