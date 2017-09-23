import sys
import os
sys.path.append(os.path.join('..', 'src'))
from ARRLMessage import *
#from ARRLMessage import function1

import unittest

class TestARRLMessage(unittest.TestCase):

	def setUp(self):
		pass
    
	def tearDown(self):
		pass

	def test_is_word(self):

		self.assertTrue(is_word("test"))		
		self.assertFalse(is_word("ooglaham"))

	def test_is_mixed_group(self):

		self.assertTrue(is_mixed_group("abc123"))
		self.assertFalse(is_mixed_group("test"))


	def test_is_homophone(self):

		self.assertTrue(is_homophone("you", build_homophone_list()))


if __name__ == '__main__':
    unittest.main()
#suite = unittest.TestLoader().loadTestsFromTestCase(TestMyClass)
#unittest.TextTestRunner(verbosity=1).run(suite)
