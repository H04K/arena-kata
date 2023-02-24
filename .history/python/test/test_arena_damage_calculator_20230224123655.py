from src.arena_damage_calculator import ArenaDamageCalculator, Hero, HeroElement, Buff
import pytest


def test_compute_damage_attacker_water_should_return_defenders_list():
    attacker = Hero(HeroElement.WATER,100,100,100,100,100)
    defenders = [   
                    Hero(HeroElement.FIRE,100,100,100,100,100), 
                    Hero(HeroElement.WATER,100,100,100,100,100), 
                    Hero(HeroElement.EARTH,100,100,100,100,100)
                ]
    assert ArenaDamageCalculator().computeDamage(attacker, defenders) == defenders        
    

def test_comoute_damage_attacker_fire_should_return_defenders_list():
    attacker = Hero(HeroElement.FIRE,100,100,100,100,100)
    defenders = [   
                    Hero(HeroElement.FIRE,100,100,100,100,100), 
                    Hero(HeroElement.WATER,100,100,100,100,100), 
                    Hero(HeroElement.EARTH,100,100,100,100,100)
                ]
    assert ArenaDamageCalculator().computeDamage(attacker, defenders) == defenders
    
def test_compute_damage_attacker_earth_should_return_defenders_list():
    attacker = Hero(HeroElement.EARTH,100,100,100,100,100)
    defenders = [   
                    Hero(HeroElement.FIRE,100,100,100,100,100), 
                    Hero(HeroElement.WATER,100,100,100,100,100), 
                    Hero(HeroElement.EARTH,100,100,100,100,100)
                ]
    assert ArenaDamageCalculator().computeDamage(attacker, defenders) == defenders
    

def test_compute_damage_with_attackers_adv_fire():
    buff_attacker = Buff(1)
    buff_defenders_water = Buff(2)
    buff_defenders_fire= Buff(2)
    buff_defenders_earth = Buff(2)
    attackers = Hero(HeroElement.FIRE,100,100,100,100,100)
    defenders = [Hero(HeroElement.FIRE,100,100,100,100,100), Hero(HeroElement.WATER,100,100,100,100,100), Hero(HeroElement.EARTH,100,100,100,100,100)]
    
    defenders[0].buffs.append(buff_defenders_fire)
    defenders[1].buffs.append(buff_defenders_water)
    defenders[2].buffs.append(buff_defenders_earth)
    attackers.buffs.append(buff_attacker)
    
    defenders = ArenaDamageCalculator().computeDamage(attackers, defenders)
    print(len(defe,))
    assert defenders[0].lp == 100
    assert defenders[1].lp == 100
    assert defenders[2].lp <100
    
    
