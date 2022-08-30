from random import randint, choice
from enum import Enum
import random

round_number = 0


class SuperAbility(Enum):
    CRITICAL_DAMAGE = 1
    HEAL = 2
    BOOST = 3
    SAVE_DAMAGE_AND_REVERT = 4

    def __str__(self):
        return self.CRITICAL_DAMAGE


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        GameEntity.__init__(self, name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    @defence.setter
    def defence(self, value):
        self.__defence = value


    def hit(self, boss, heroes):
        for hero in heroes:
            if boss.health > 0 and hero.health > 0:
                hero.health = hero.health - boss.damage
    # def hit(self, boss,heroes):
    #     for hero in heroes:
    #         if self.health > 0 and boss.health > 0:
    #             bo.health -= self.damage
    #
    # def choose_defence(self, heroes):
    #     chosen_hero = choice(heroes)
    #     self.__defence = chosen_hero.super_ability
    #
    # def __str__(self):
    #     return f'BOSS {self.name} health: {self.health} damage: {self.damage} , defence: {self.defence}'

class Hero(GameEntity):
    def __init__(self, name, health, damage, super_ability):
        super().__init__(name, health, damage)
        self.__super_ability = super_ability
# class Hero(GameEntity):
#     def __init__(self, name, health, damage, super_ability):
#         GameEntity.__init__(self, name, health, damage)
#         if not isinstance(super_ability, SuperAbility):
#             raise AttributeError("Wrong data type for super_ability")
#         else:
#             self.__super_ability = super_ability

    @property
    def super_ability(self):
        return self.__super_ability


    def apply_super_ability(self, boss, heroes):
        pass

    def hit(self, boss):
        if boss.health > 0 and self.health > 0:
            boss.health = boss.health - self.damage


class Warrior(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def super_ability(self, boss, heroes):
        coeffient = randint(2, 6)
        boss.health -= self.damage * coeffient
        print(f'Critical damage: {self.damage * coeffient}')


class Thor(Hero):
    def __init__(self, name, health, damage, stan=0):
        super().__init__(name, health, damage, "STAN")
        self.__stan = stan

    def apply_super_ability(self, boss, heroes_list):
        if self.health > 0 and round_number == 1:
            self.damage = self.__stan
        elif self.damage == self.__stan:
            boss.damage = 50
        else:
            boss.damage = 0


# =================
class Golem(Hero):
    def __init__(self, name, health, damage, protection=0):
        super().__init__(name, health, damage, "PROTECTION")
        self.__protection = protection

    def super_ability(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0:
                self.__protection = boss.damage // 5
                if boss.damage >= 1:
                    hero.health = hero.health + self.__protection
                else:
                    hero.health = hero.health - boss.damage


# ====================

# ====================
class Witcher(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "SAVIOR")

    def super_ability(self, boss, heroes):
        self.damage = 0
        for hero in heroes:
            if hero.health >= 0:
                self.health = hero.health
                self.health = 0
            else:
                self.health = 0


# =====================


# ====================

# ====================
class Warrior(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def super_ability(self, boss, heroes):
        if boss.health > 0 and self.health > 0:
            chance = random.randint(1, 2)
            choices = [20, 50, 100]
            damage_chance = random.choice(choices)
            if chance == 1 and damage_chance == 20:
                damage = self.damage + (self.damage / 100 * 20)
                self.health = self.health - (self.health / 100 * 10)
                boss.health -= damage
                print(f"{self.name} Нанес на 20% больше урона")
                print(f"{self.name} Потерял 20% от здоровбе")


            elif chance == 1 and damage_chance == 50:
                damage = self.damage + (self.damage / 100 * 50)
                self.health = self.health - (self.health / 100 * 25)
                boss.health -= damage
                print(f"{self.name} Нанес на 50% больше урона")
                print(f"{self.name} Потерял 25% от здоровбе")

            elif chance == 1 and damage_chance == 50:
                damage = self.damage + (self.damage * 2)
                self.health = self.health - (self.health / 100 * 45)
                boss.health -= damage
                print(f"{self.name} Нанес на 50% больше урона")
                print(f"{self.name} Потерял 45% от здоровбе")


# ===================


# ==================
round_counter = 0


def start():
    boss = Boss("Alex", 1000, 50)
    warrior = Warrior("Ahiles", 280, 10)
    thor = Thor('Thor',300, 20,8)
    golem = Golem('golem', 400, 50)
    wither = Witcher('wither', 350, 35)
    heroes_list = [warrior, thor, golem, wither]

    print_stats(boss, heroes_list)

    while (not is_game_finished(boss, heroes_list)):
        play_round(boss, heroes_list)


def play_round(boss, heroes):
    global round_counter
    round_counter += 1
    boss.choose_defence(heroes)
    # boss.hit(heroes)
    heroes_hit(boss, heroes)
    heroes_skills(boss, heroes)
    print_stats(boss, heroes)
    # for hero in heroes:
    #     if boss.defence != hero.super_ability and hero.health > 0:
    #         hero.hit(boss)
    #         hero.apply_super_ability(boss, heroes)
    # print_statistics(boss, heroes)


def boss_hits(boss, heroes):
    for h in heroes:
        if h.health > 0 and boss.health > 0:
            h.health = h.health - boss.damage


# def start():
#     boss = Boss("Alex", 1000, 50)
#     warrior = Warrior("Ahiles", 280, 10)
#     thor = Thor('Thor', 300, 20)
#     golem = Golem('golem', 400, 50)
#     wither = Witcher('wither', 350, 35)
#     heroes_list = [warrior,thor,golem, wither]
#
#     print_statistics(boss, heroes_list)
#
#     while (not is_game_finished(boss, heroes_list)):
#         play_round(boss, heroes_list)

def heroes_hit(boss, heroes):
    for h in heroes:
        if h.health > 0 and boss.health > 0:
            boss.health = boss.health - h.damage


def heroes_skills(boss, heroes):
    for h in heroes:
        if h.health > 0 and boss.health > 0:
            h.super_ability(boss, heroes)


def heroes_skills(boss, heroes):
    for h in heroes:
        if h.health > 0 and boss.health > 0:
            h.super_ability(boss, heroes)


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print("Heroes won!!!")
        return True

    all_heroes_dead = True
    for h in heroes:
        if h.health > 0:
            all_heroes_dead = False
            break

    if all_heroes_dead:
        print("Boss won!!!")

    return all_heroes_dead


def print_stats(boss, heroes):
    print(f'ROUND {round_counter} ------------------')
    print(boss)
    for hero in heroes:
        print(hero)


start()