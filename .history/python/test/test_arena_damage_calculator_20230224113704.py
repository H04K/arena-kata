import unittest
from unittest import TestCase
import src.arena_damage_calculator a

class TestArenaDamageCalculator(TestCase):
    
    def test_compute_damage_attacker_water(self):
        attacker = Hero(HeroElement.WATER,100,100,100,100,100)
        defenders = [   
                     Hero(HeroElement.FIRE,100,100,100,100,100), 
                     Hero(HeroElement.WATER,100,100,100,100,100), 
                     Hero(HeroElement.EARTH,100,100,100,100,100)
                    ]
        
        self.assertEqual(ArenaDamageCalculator().computeDamage(attacker, defenders),defenders)
        
        
        

if __name__ == "__main__":
    unittest.main()