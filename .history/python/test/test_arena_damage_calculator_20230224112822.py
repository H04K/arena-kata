import unittest
from unittest import TestCase
from arena_damage_calculator import Hero, HeroElement, ArenaDamageCalculator



class TestArenaDamageCalculator(TestCase):
    
    def test_compute_damage_attacker_water(self):
        attacker = Hero(HeroElement.WATER,100,100,100,100,100)
        defenders = [   
                     Hero(HeroElement.FIRE,100,100,100,100,100), 
                     Hero(HeroElement.WATER,100,100,100,100,100), 
                     Hero(HeroElement.EARTH,100,100,100,100,100)
                    ]
        
        damage = ArenaDamageCalculator().ComputeDamage(attacker )
        
