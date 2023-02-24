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
    buff_attacker = Buff(1)
    buff_defenders_water = Buff(2)
    buff_defenders_fire= Buff(2)
    buff_defenders_earth = Buff(2)
    attackers = Hero(HeroElement.EARTH,100,100,100,100,100)
    defenders = [Hero(HeroElement.FIRE,100,100,100,100,100), Hero(HeroElement.WATER,100,100,100,100,100), Hero(HeroElement.EARTH,100,100,100,100,100)]
    
    defenders[0].buffs.append(buff_defenders_fire)
    defenders[1].buffs.append(buff_defenders_water)
    defenders[2].buffs.append(buff_defenders_earth)
    attackers.buffs.append(buff_attacker)
    
    
    response_arena_damage = ArenaDamageCalculator().computeDamage(attackers, defenders)
    attacked = response_arena_damage[1] 
    dmg = response_arena_damage[2]
    
    assert dmg == 100
    assert attacked == defenders[1]
       
    