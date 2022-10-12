import unittest
import io
import sys
from unittest.mock import patch

from contacts import *

import os
def remove_file(filename):
    if os.path.exists(filename):
        os.remove(filename)

class Test01_AddContact(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test01 *** GIVEN: filename t99.dat = {'7145551111': ['Steve', 'Jobs'], '5625553333': ['Bill', 'Gates']} AND contacts = Contacts(filename='t99.dat') *** FUNCTION CALL: contacts.add_contact(id = '7145551212', first_name = 'Richard', last_name = 'Stallman') *** EXPECT: filename t99.dat = {'7145551111': ['Steve', 'Jobs'], '5625553333': ['Bill', 'Gates'], '7145551212': ['Richard', 'Stallman']} ***
        """
        with open('t99.dat', 'w') as f:
            json.dump({'7145551111': ['Steve', 'Jobs'], '5625553333': ['Bill', 'Gates']}, f)
        contacts = Contacts(filename='t99.dat')
        r = contacts.add_contact(id = '7145551212', first_name = 'Richard', last_name = 'Stallman')
        c = {}
        with open('t99.dat', 'r') as f:
            c = json.load(f)
        self.assertEqual(c, {'7145551111': ['Steve', 'Jobs'], '5625553333': ['Bill', 'Gates'], '7145551212': ['Richard', 'Stallman']})
        remove_file('t99.dat')
        print()

class Test02_AddContact(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test02 *** GIVEN: filename t99.dat = {'7145551111': ['Steve', 'Jobs'], '5625553333': ['Bill', 'Gates']} AND contacts = Contacts(filename='t99.dat') *** FUNCTION CALL: r = contacts.add_contact(id = '7145551212', first_name = 'Richard', last_name = 'Stallman') *** EXPECT: filename t99.dat = {'7145551111': ['Steve', 'Jobs'], '5625553333': ['Bill', 'Gates'], '7145551212': ['Richard', 'Stallman']} ***
        """
        with open('t99.dat', 'w') as f:
            json.dump({'7145551111': ['Steve', 'Jobs'], '5625553333': ['Bill', 'Gates']}, f)
        contacts = Contacts(filename='t99.dat')
        r = contacts.add_contact(id = '7145551111', first_name = 'Richard', last_name = 'Stallman')
        self.assertEqual(r, 'error')
        remove_file('t99.dat')
        print()

class Test03_ModifyContact(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test03 *** GIVEN: filename t99.dat = {'7145551111': ['Steve', 'Jobs'], '5625553333': ['Bill', 'Gates']} AND contacts = Contacts(filename='t99.dat') *** FUNCTION CALL: contacts.modify_contact(id = '7145551111', first_name = 'Richard', last_name = 'Stallman') *** EXPECT: filename t99.dat = {'5625553333': ['Bill', 'Gates'], '7145551111': ['Richard', 'Stallman']} ***
        """
        with open('t99.dat', 'w') as f:
            json.dump({'7145551111': ['Steve', 'Jobs'], '5625553333': ['Bill', 'Gates']}, f)
        contacts = Contacts(filename='t99.dat')
        r = contacts.modify_contact(id = '7145551111', first_name = 'Richard', last_name = 'Stallman')
        c = {}
        with open('t99.dat', 'r') as f:
            c = json.load(f)
        self.assertEqual(c, {'5625553333': ['Bill', 'Gates'], '7145551111': ['Richard', 'Stallman']})
        remove_file('t99.dat')
        print()

class Test04_ModifyContact(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test04 *** GIVEN: filename t99.dat = {'7145551111': ['Steve', 'Jobs'], '5625553333': ['Bill', 'Gates']} AND contacts = Contacts(filename='t99.dat') *** FUNCTION CALL: r = contacts.modify_contact(id = '7145559999', first_name = 'Richard', last_name = 'Stallman') *** EXPECT: r = 'error' ***
        """
        with open('t99.dat', 'w') as f:
            json.dump({'7145551111': ['Steve', 'Jobs'], '5625553333': ['Bill', 'Gates']}, f)
        contacts = Contacts(filename='t99.dat')
        r = contacts.modify_contact(id = '7145559999', first_name = 'Richard', last_name = 'Stallman')
        self.assertEqual(r, 'error')
        remove_file('t99.dat')
        print()

class Test05_DeleteContact(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test05 *** GIVEN: filename t99.dat = {'7145551111': ['Steve', 'Jobs'], '5625553333': ['Bill', 'Gates']} AND contacts = Contacts(filename='t99.dat') *** FUNCTION CALL: contacts.delete_contact(id = '7145551111') *** EXPECT: filename t99.dat = {'5625553333': ['Bill', 'Gates']} ***
        """
        with open('t99.dat', 'w') as f:
            json.dump({'7145551111': ['Steve', 'Jobs'], '5625553333': ['Bill', 'Gates']}, f)
        contacts = Contacts(filename='t99.dat')
        r = contacts.delete_contact(id = '7145551111')
        c = {}
        with open('t99.dat', 'r') as f:
            c = json.load(f)
        self.assertEqual(c, {'5625553333': ['Bill', 'Gates']})
        remove_file('t99.dat')
        print()

class Test06_DeleteContact(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test06 *** GIVEN: filename t99.dat = {'7145551111': ['Steve', 'Jobs'], '5625553333': ['Bill', 'Gates']} AND contacts = Contacts(filename='t99.dat') *** FUNCTION CALL: r = contacts.delete_contact(id = '7145551111') *** EXPECT: r = 'error' ***
        """
        with open('t99.dat', 'w') as f:
            json.dump({'7145551111': ['Steve', 'Jobs'], '5625553333': ['Bill', 'Gates']}, f)
        contacts = Contacts(filename='t99.dat')
        r = contacts.delete_contact(id = '7145559999')
        self.assertEqual(r, 'error')
        remove_file('t99.dat')
        print()


if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
