# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 19:48:26 2023

@author: Vishwesh
"""

# Importing the unittest module for writing test cases
import unittest
from unittest.mock import patch
import untitled10
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
    
    @patch("untitled10.get_repo_info")
    def test_get_repo_with_valid_user(self, mock_get_repo):
        mock_get_repo.return_value = [200, {"Search_engine": "2",
                                            "kapilparsodkar/FitCzar-fitness-App": "14",
                                            "helloworld": "1",
                                            "SSW_567_HW_02a_Triangle": "8",
                                            "Homework-04a---Develop-with-the-Perspective-of-the-Tester-in-mind": "12",
                                            "SSW-567-HW-05-Static-Code-Analysis": "10",
                                            "JPMC_Virtual_Experience": "4"}]
        self.assertTrue(untitled10.get_repo_info("ArunRao1997")[0])

    @patch("untitled10.get_repo_info")
    def test_get_repo_return_value_with_valid_user(self, mock_get_repo):
        mock_get_repo.return_value = [200, {"Search_engine": "2",
                                            "kapilparsodkar/FitCzar-fitness-App": "14",
                                            "helloworld": "1",
                                            "SSW_567_HW_02a_Triangle": "8",
                                            "Homework-04a---Develop-with-the-Perspective-of-the-Tester-in-mind": "12",
                                            "SSW-567-HW-05-Static-Code-Analysis": "10",
                                            "JPMC_Virtual_Experience": "4"}]
        self.assertEqual(mock_get_repo()[1], untitled10.get_repo_info("ArunRao1997")[1])

    @patch("untitled10.get_repo_info")
    def test_get_repo_with_invalid_user(self, mock_get_repo):
        mock_get_repo.return_value = False
        self.assertFalse(untitled10.get_repo_info('blkfjayhatw'))

    @patch("untitled10.get_repo_info")
    def test_get_repo_return_value_with_invalid_user(self, mock_get_repo):
        mock_get_repo.return_value = False
        self.assertIs(mock_get_repo(), untitled10.get_repo_info('blkfjayhatw'))

    @patch("untitled10.get_repo_info")
    def test_get_repo_return_value_with_user_with_no_repos(self, mock_get_repo):
        mock_get_repo.return_value = [200, {""}]
        self.assertTrue(untitled10.get_repo_info("GautamP2393")[0])

    @patch("untitled10.get_repo_info")
    def test_get_repo_with_user_with_no_repos(self, mock_get_repo):
        mock_get_repo.return_value = [200, {""}]
        self.assertIs(mock_get_repo()[1], untitled10.get_repo_info("GautamP2393")[1])

        
if __name__ == '__main__':
   my_brand("HW 02A")
   print('Running unit tests')
   unittest.main()
   my_brand("HW 02A")
