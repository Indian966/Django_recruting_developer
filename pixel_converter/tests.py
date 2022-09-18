import unittest
from pixel_converter import code_converter
import os
from django.test import TestCase

# Create your tests here.


class TestConverter(unittest.TestCase):
    def test_index(self):
        # requset =
        T = code_converter.converter()
        expect = [0,0,0]
        result = T.rgb_to_dmc()
        self.assert_()
