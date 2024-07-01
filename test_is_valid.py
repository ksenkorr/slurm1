import unittest

from is_valid import is_valid

class IsValidTestCase(unittest.TestCase):
    def test_is_valid(self):
        self.assertTrue(is_valid('()'))

    def test_is_not_valid(self):
        self.assertFalse(is_valid('('))

    def test_is_valid():
        assert is_valid('()')

'''
python3 -m unitest test_is_valid
'''

'''
pipenv run python -m coverage run -m unitest test_is_valid
pipenv run python -m coverage report

# Будет создана папка html
pipenv run python -m coverage html


pipenv run python -m pytest ./test_is_valid.py
'''
