import unittest
import random
import swagger as s
from time import sleep
'''
Superhero API test v0.4
'''
hd1 = {
  "fullName": "Skitter",
  "birthDate": "1985-06-23",
  "city": "Brokton Bay",
  "mainSkill": "Bug control",
  "gender": "f",
  "phone": "+74998884400"
}

hd3 = {
  "fullName": "Grue",
  "birthDate": "1983-03-03",
  "city": "Brokton Bay",
  "mainSkill": "Make darknes",
  "gender": "m",
  "phone": "+74998884401"
}

hd5 = {
  "fullName": "Bonesaw",
  "birthDate": "2000-03-23",
  "city": "Johanessburg",
  "mainSkill": "Bio control",
  "gender": "ж",
  "phone":  "+74998884402"
}

hd2 = {
  "fullName": "Imp",
  "birthDate": "1980-01-25",
  "mainSkill": "Stranger 9",
  "gender": "f",
  "phone": "+74998884422"
}

hd4 = {
  "fullName": "Regent",
  "birthDate": "1900-03-23",
  "city": "Brokton Bay",
  "mainSkill": "Other people control",
  "gender": "m",
  "phone": "DON'T CALL THIS GUY"
}

hd8 = {
  "fullName": "Doll",
  "birthDate": "1987-01-25",
  "city": "Brokton Bay",
  "mainSkill": "Make big doll",
}

hd6 = {
  "fullName": None,
  "city": 11223,
  "mainSkill": ["aaa", 'bbb'],
  "phone": "+74998884403"
}


def get_hero_data(valid=True):
    if valid:
        return random.choice([hd1, hd3, hd5])
    else:
        return random.choice([hd2, hd4, hd8])

def get_hero_id():
    r = s.get_superheroes()
    r_format = s.req_info(r)
    hero = random.choice(r_format[1])
    try:
        my_id = hero['id']
    except (KeyError, ValueError) as e:
        my_id = "Error get id"
    return my_id

class SuperheroAPITest(unittest.TestCase):
    
    # 1,2,3,4,5,6,7,8,9,10,11,12,13,14
    skip_test = []

    @unittest.skipIf(1 in skip_test, " for debug") 
    def test_01_post_ok(self):
        "=> Send and chek new superhero: positive"
        hero = get_hero_data()
        r = s.post_superheroes(hero)
        r_format = s.req_info(r)
        del r_format[1]['id']
        self.assertEqual(r_format[0], 200, msg=f"Status code is: {r_format[0]}, expected: 200")
        msg=f"The data received is different from the data sent\nsend:{hero}\nget:{r_format[1]}"
        self.assertDictEqual(r_format[1], hero, msg=msg)

    @unittest.skipIf(2 in skip_test, " for debug") 
    def test_02_post_fail(self):
        "=> Send and chek new superhero: negative 403"
        hero = get_hero_data(False)
        r = s.post_superheroes(hero)
        r_format = s.req_info(r)
        self.assertEqual(r_format[0], 403, 
            msg=f"Status code is: {r_format[0]}, expected: 403\n{r_format[1]}\n{hero}")

    @unittest.skipIf(3 in skip_test, " for debug")     
    def test_03_post_fail(self):
        "=> Send and chek new superhero: negative 400"
        hero = hd6
        r = s.post_superheroes(hero)
        r_format = s.req_info(r)
        self.assertEqual(r_format[0], 400, 
            msg=f"Status code is: {r_format[0]}, expected: 400\n{r_format[1]}\n{hero}")

    @unittest.skipIf(4 in skip_test, " for debug")
    def test_04_get_ok(self):
        "=> Get all superhero: positive"
        r = s.get_superheroes()
        r_format = s.req_info(r)
        self.assertEqual(r_format[0], 200, msg=f"Status code is: {r_format[0]}, expected: 200")
        self.assertIsInstance(r_format[1], list, msg=f"Expected list, get {type(r_format[1])}")
        self.assertIsInstance(r_format[1][0], dict, msg=f"Expected dict, get {type(r_format[1][0])}")

    @unittest.skipIf(5 in skip_test, " for debug")  
    def test_05_get_ok(self):
        "=> Get superhero by id: positive"
        try:
            my_id = get_hero_id()
        except (KeyError, ValueError) as e:
            my_id = "Error get id"
        r = s.get_superheroes(my_id)
        r_format = s.req_info(r)
        my_hero = r_format[1]
        msg = f"Status code is: {r_format[0]}, expected: 200\nid:{my_id}\nget:{my_hero}"
        self.assertEqual(r_format[0], 200, msg=msg)
        msg = f"The data received is different from the data sent\nget:{my_hero}\nid:{my_id}"
        self.assertIsInstance(my_hero, dict, msg=f"Expected dict, get {my_hero}")

    @unittest.skipIf(6 in skip_test, " for debug")
    def test_06_get_fail(self):
        "=> Get superhero: negative get w/o id"
        r = s.get_superheroes(None, "sh")
        r_format = s.req_info(r)
        self.assertEqual(r_format[0], 404, msg=f"Status code is: {r_format[0]}, expected: 404")
    
    @unittest.skipIf(7 in skip_test, " for debug")
    def test_07_get_fail(self):
        "=> Get superhero: negative get with 0"
        r = s.get_superheroes(0)
        r_format = s.req_info(r)
        self.assertEqual(r_format[0], 400, msg=f"Status code is: {r_format[0]}, expected: 400")

    @unittest.skipIf(8 in skip_test, " for debug")
    def test_08_put_ok(self):
        "U> Update superhero by id: positive"
        try:
            my_id = get_hero_id()
        except (KeyError, ValueError) as e:
            my_id = "Error get id"
        r = s.get_superheroes(my_id)
        r_format = s.req_info(r)
        hero = r_format[1]
        upd_for_hero = get_hero_data()
        del upd_for_hero['phone']
        r = s.put_superheroes(my_id,upd_for_hero)
        r_format = s.req_info(r)
        
        msg = f"Status code is: {r_format[0]}, expected: 200\nsend:{hero}\nid:{my_id}\nget:{r_format[1]}"
        self.assertEqual(r_format[0], 200, msg=msg)
        r = s.get_superheroes(my_id)
        r_format = s.req_info(r)
        msg = f"Status code is: {r_format[0]}, expected: 200\nsend:{hero}\nid:{my_id}\nget:{r_format[1]}"
        self.assertEqual(r_format[0], 200, msg=msg)
        del r_format[1]['id']
        del r_format[1]['phone']
        msg = f"The data received is different from the data sent\nsend:{upd_for_hero}\nid:{my_id}\nget:{r_format[1]}"
        self.assertDictEqual(r_format[1], upd_for_hero, msg=msg)

    @unittest.skipIf(9 in skip_test, " for debug")
    def test_09_put_fail(self):
        "U> Update superhero by id: negative 403"
        try:
            my_id = get_hero_id()
        except (KeyError, ValueError) as e:
            my_id = "Error get id"
        self.assertNotEqual(my_id,"Error get id", msg=my_id)
        upd_for_hero = get_hero_data(False)
        r = s.put_superheroes(my_id,upd_for_hero)
        r_format = s.req_info(r)
        msg = f"Status code is: {r_format[0]}, expected: 403\nsend:{upd_for_hero}\nid:{my_id}\nget:{r_format[1]}"
        self.assertEqual(r_format[0], 403, msg=msg)

    @unittest.skipIf(10 in skip_test, " for debug")    
    def test_10_put_fail(self):
        "U> Update superhero by id: negative 400"
        try:
            my_id = get_hero_id()
        except (KeyError, ValueError) as e:
            my_id = "Error get id"
        self.assertNotEqual(my_id,"Error get id", msg=my_id)
        upd_for_hero = hd6
        r = s.put_superheroes(my_id,upd_for_hero)
        r_format = s.req_info(r)
        msg = f"Status code is: {r_format[0]}, expected: 400\nsend:{upd_for_hero}\nid:{my_id}\nget:{r_format[1]}"
        self.assertEqual(r_format[0], 400, msg=msg)

    @unittest.skipIf(11 in skip_test, " for debug")    
    def test_11_del_ok(self):
        ">X< Delete superhero by id: positive"
        try:
            my_id = get_hero_id()
        except (KeyError, ValueError) as e:
            my_id = "Error get id"
        r = s.del_superheroes(my_id)
        r_format = s.req_info(r)
        self.assertEqual(r_format[0], 200, msg=f"Status code is: {r_format[0]}, expected: 200")
        sleep(1)
        r = s.get_superheroes(my_id)
        r_format = s.req_info(r)
        self.assertNotEqual(r_format[0], 200, msg=f"Status code is: {r_format[0]}, wait 4xx")

    @unittest.skipIf(12 in skip_test, " for debug")    
    def test_12_del_fail(self):
        ">X< Delete superhero by id: negative 405"
        my_id = ""#999#999999
        r = s.del_superheroes(my_id)
        r_format = s.req_info(r)
        self.assertEqual(r_format[0], 405, msg=f"Status code is: {r_format[0]}, wait 405")
        
    @unittest.skipIf(13 in skip_test, " for debug")    
    def test_13_del_fail(self):
        ">X< Delete superhero by id: negative 400"
        my_id = "aa"#999#999999
        r = s.del_superheroes(my_id)
        r_format = s.req_info(r)
        self.assertEqual(r_format[0], 400, msg=f"Status code is: {r_format[0]}, wait 400") 

    @unittest.skipIf(14 in skip_test, " for debug")
    def test_14_del_fail(self):
        ">X< Delete superhero by id: negative 4xx"
        my_id = 999        #999999
        r = s.get_superheroes(my_id)
        r_format = s.req_info(r)
        self.assertNotEqual(r_format[0], 200, msg=f"Status code is: {r_format[0]}, wait 4xx")
        r = s.del_superheroes(my_id)
        r_format = s.req_info(r)
        self.assertNotEqual(r_format[0], 200, msg=f"Status code is: {r_format[0]}, wait 4xx") 

if __name__ == '__main__':
    unittest.main(verbosity=2)