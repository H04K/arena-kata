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
    

def test_compute_damage_with_attack_buff():
    buff_defenders = Buff(1)
    attack
    