import unittest
import views
from django.test import TestCase

# Create your tests here.


class TestGenerateMap(unittest.TestCase):
    def test_index(self):
        # requset =
        T = views.index()
        expect = 0
        result = T
        self.assert_()
