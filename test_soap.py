import unittest
import random
import soapwsdl as s
from time import sleep


class SoapAPITest(unittest.TestCase):
    
    # 1,2,3,4,5,6,7,8,9,10,11,12,13,14
    skip_test = []
    cid = 0
    eid = 0
    @unittest.skipIf(1 in skip_test, " for debug") 
    def test_01_add_company_ok(self):
        "+> AddCompany: positive"
        c_name = "PRT" 
        y = s.get_reply(s.add_company, c_name)
        x = s.company_id_name(y)
        global cid
        cid = x[0]
        self.assertEqual(y[0], 200, msg=f"Status code is: {y[0]}, expected: 200")
        self.assertEqual(x[1], c_name, msg=f"Different name, send: {c_name}, get: {x[1]}")

    @unittest.skipIf(2 in skip_test, " for debug") 
    def test_02_add_emp_ok(self):
        "+> AddEmployee: positive"
        f_name = "Thomas"
        l_name = "Kalvert" 
        y = s.get_reply(s.add_empl, f_name, l_name)
        x = s.empl_id_name(y)
        global eid
        eid = x[0]
        self.assertEqual(y[0], 200, msg=f"Status code is: {y[0]}, expected: 200")
        self.assertEqual(x[1], f_name, msg=f"Different name, send: {f_name}, get: {x[1]}")

    @unittest.skipIf(3 in skip_test, " for debug") 
    def test_03_add_emp_to_comp(self):
        "+> AddEmployeesToCompany: positive"
        global cid
        global eid
        y = s.get_reply(s.add_empl_to_company, cid, eid)
        self.assertEqual(y[0], 200, msg=f"Status code is: {y[0]}, expected: 200")

    @unittest.skipIf(4 in skip_test, " for debug") 
    def test_04_get_comp(self):
        "0> GetCompany: positive"
        global cid
        y = s.get_reply(s.get_company, cid)
        self.assertEqual(y[0], 200, msg=f"Status code is: {y[0]}, expected: 200")

    @unittest.skipIf(5 in skip_test, " for debug") 
    def test_05_upd_emp(self):
        "u> UpdateEmployee: positive"
        global eid
        f_name = "Kalvert"
        l_name = "Thomas"
        m_name = f_name+"."+l_name
        y = s.get_reply(s.upd_empl, eid, f_name, l_name, m_name)
        self.assertEqual(y[0], 200, msg=f"Status code is: {y[0]}, expected: 200") 


if __name__ == '__main__':
    unittest.main(verbosity=2)