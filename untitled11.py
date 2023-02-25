# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 19:48:26 2023

@author: Vishwesh
"""

# Importing the unittest module for writing test cases
import unittest
from untitled10 import get_repo_info,my_brand
# Defining a TestRepoAPI class that inherits from unittest.TestCase 
class TestRepoAPI(unittest.TestCase):

    # Test case for when user does not exist
    def testUserNotExist(self):
        # Calling the GithubApi function with a non-existent user ID
        self.assertEqual(get_repo_info('XXXYYYZZZ111222333'), "GitHub user not found.")

    # Test case for testing success message by calling my username
    def testUserSuccess(self):
        # Calling the GithubApi function with an existing user ID
        self.assertEqual(get_repo_info('VishweshMS'), "Success")
        
if __name__ == '__main__':
   my_brand("HW 02A")
   print('Running unit tests')
   unittest.main()
   my_brand("HW 02A")
