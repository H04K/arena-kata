from src.arena_damage_calculator import ArenaDamageCalculator, Hero, HeroElement



class TestArenaDamageCalculator():
    
    def test_compute_damage_attacker_water(self):
        attacker = Hero(HeroElement.WATER,100,100,100,100,100)
        defenders = [   
                     Hero(HeroElement.FIRE,100,100,100,100,100), 
                     Hero(HeroElement.WATER,100,100,100,100,100), 
                     Hero(HeroElement.EARTH,100,100,100,100,100)
                    ]
        
        assertEqual(ArenaDamageCalculator().computeDamage(attacker, defenders),defenders)
        
        
        
