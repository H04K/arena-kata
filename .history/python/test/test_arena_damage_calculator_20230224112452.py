import unittest
from unittest import TestCase
from arena_damage_calculator import Hero, HeroElement, ArenaDamageCalculator



class TestArenaDamageCalculator(TestCase):
    
    def test_compute_damage_attacker_water(self):
        attacker = Hero(HeroElement.WA)
