import sys
import os
sys.path.append(os.path.join('..', 'src'))
#from ARRLMessage import *
from ARRLMessage import function1

import unittest

class TestMyClass(unittest.TestCase):

    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def test_function1(self):

        self.assertEqual(function1(1), 2)		

if __name__ == '__main__':
    unittest.main()
#suite = unittest.TestLoader().loadTestsFromTestCase(TestMyClass)
#unittest.TextTestRunner(verbosity=1).run(suite)
