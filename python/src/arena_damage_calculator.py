import math
import random
from enum import Enum

class HeroElement(Enum):
    FIRE = 1
    WATER = 2
    EARTH = 3

class Buff(Enum):
    ATTACK = 1
    DEFENSE = 2

class Hero:
    def __init__(self, element: HeroElement, power, defense, leth, crtic_rate, life_points):
        self.element = element
        self.pow = power
        self.defense = defense
        self.leth = leth
        self.crtr = crtic_rate
        self.crtic_rate = crtic_rate
        self.lp = life_points
        self.life_points = life_points
        self.buffs = []

class ArenaDamageCalculator:

    def computeDamage(self, attacker: Hero, defenders: list[Hero]):
        adv,eq,dis = [],[],[]
        attacked = choose_which_defender_to_attack(attacker,defenders,adv,eq,dis)
        is_critical = random.random() * 100 < attacker.crtr
        dmg = compute_damage_value(attacker,attacked,is_critical)
        dmg = apply_attack_buffs(attacker,attacked,dmg,is_critical)
        dmg = apply_defence_buffs(attacker,attacked,dmg)
        dmg = compute_bonus(dmg,attacked,adv,eq)
        apply_full_damage_bonus_calculated(dmg,attacked)
        return defenders

def get_advantage_element(element: HeroElement) -> HeroElement:
    ''' 
        Returns element on which attacker element has advantage 
    '''
    if element == HeroElement.WATER:
        return HeroElement.FIRE
    elif element == HeroElement.FIRE:
        return HeroElement.EARTH
    elif element == HeroElement.EARTH:
        return HeroElement.WATER


def choose_which_defender_to_attack(attacker: Hero, defenders: list[Hero],advantage,equal,disadvantage) -> Hero:
    
    for hero in defenders:
        if hero.life_points > 0:
            if hero.element == attacker.element:
                equal.append(hero)
            elif hero.element == get_advantage_element(attacker.element):
                advantage.append(hero)
            else:
                disadvantage.append(hero)

        
    if len(advantage) > 0:
        return advantage[math.floor(random.random() * len(advantage))]
    elif len(equal) > 0:
        return equal[math.floor(random.random() * len(equal))]
    else:
        return disadvantage[math.floor(random.random() * len(disadvantage))]


def compute_damage_value(attacker: Hero, defender: Hero,is_critical):
        defense_ratio = (1-defender.defense / 7500)
        power = attacker.pow
        damage = 0
        
        if is_critical:
            damage = (power + (0.5 + attacker.leth / 5000) * power) * defense_ratio
        else:
            damage = power * defense_ratio

        return damage

def apply_attack_buffs(attacker: Hero, defender: Hero, damage,is_critical):
    defense_ratio = (1-defender.defense / 7500)
    power = attacker.pow
    if Buff.ATTACK in attacker.buffs:
        if is_critical:
            damage += (power * 0.25 + (0.5 + attacker.leth / 5000) * power * 0.25) * defense_ratio
        else:
            damage += power * 0.25* defense_ratio

    return damage


def apply_defence_buffs(attacker : Hero,defender:Hero,damage):

    if Buff.DEFENSE in defender.buffs:
            damage = damage / (1-defender.defense/7500) * (1-defender.defense/7500 -0.25)

    return max(damage, 0)


def compute_bonus(damage,defender,advantage,equal):
     
    if damage > 0:
        if defender in advantage:
            damage = damage + damage * 0.2
        elif defender in equal:
            pass
        else:
            damage = damage - damage * 0.2

    return math.floor(damage)


def apply_full_damage_bonus_calculated(damage,defender):
    if  damage > 0:
            defender.lp -= damage
            if defender.lp < 0:
                defender.lp = 0