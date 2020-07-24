# https://py.checkio.org/en/mission/army-battles/


class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self) -> bool:
        return self.health >= 0


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


def fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        unit_2.health -= unit_1.attack
        if unit_2.is_alive:
            unit_1.health -= unit_2.attack
    return unit_1.is_alive


class Army():
    def __init__(self):
        self.units = []

    def add_units(self, fighter, quantity):
        [self.units.append(fighter()) for num in range(quantity)]

    def __len__(self):
        return len(self.units)


class Battle():
    def __init__(self):
        pass

    def fight(self, army_1, army_2):
        while len(army_1) > 0 and len(army_2) > 0:
            if fight(army_1.units[0], army_2.units[0]):
                army_2.units.pop(0)
            else:
                army_1.units.pop(0)

        return army_2.units == []


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding completed")
