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
        power = attacker.pow
        adv = []
        eq = []
        dis = []
        attacked = choose_which_defender_to_attack(attacker,defenders,adv,eq,dis)
        
        c = random.random() * 100 < attacker.crtr
        dmg = 0
        if c:
            dmg = (attacker.pow + (0.5 + attacker.leth / 5000) * attacker.pow) * (1-attacked.defense /7500)
        else:
            dmg = attacker.pow * (1-attacked.defense / 7500)

        ## BUFFS
        if Buff.ATTACK in attacker.buffs:
            if c:
                dmg += (attacker.pow * 0.25 + (0.5 + attacker.leth / 5000) * attacker.pow * 0.25) * (1-attacked.defense/7500)
            else:
                dmg += attacker.pow * 0.25* (1-attacked.defense/7500)

        if Buff.DEFENSE in attacked.buffs:
            dmg = dmg / (1-attacked.defense/7500) * (1-attacked.defense/7500 -0.25)

        dmg = max(dmg, 0)
        if dmg > 0:
            if attacked in adv:
                dmg = dmg + dmg * 20/100
            elif attacked in eq:
                pass
            else:
                dmg = dmg - dmg *20/100

        dmg = math.floor(dmg)

        if dmg > 0:
            attacked.lp = attacked.lp - dmg
            if attacked.lp < 0:
                attacked.lp = 0
        print(defenders)
        return defenders

def get_advantage_element(element: HeroElement) -> HeroElement:
    if element == HeroElement.WATER:
        return HeroElement.FIRE
    elif element == HeroElement.FIRE:
        return HeroElement.EARTH
    elif element == HeroElement.EARTH:
        return HeroElement.WATER


def choose_which_defender_to_attack(attacker: Hero, defenders: list[Hero],advantage,equal,disadvantage) -> Hero:
    


    for hero in defenders:
        if hero.life_points == 0:
            continue
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
