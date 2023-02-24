import unittest
from unittest import TestCase



class TestArenaDamageCalculator(TestCase):
    def test_compute_damage(self):
        att = Hero(HeroElement.WATER, 100, 100, 100, 100, 100)