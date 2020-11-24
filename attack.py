class Attack:
    def __init__(self, name, power, accuracy, is_physical, is_special):
        self.name = name
        self.power = power
        self.accuracy = accuracy
        self.is_physical = is_physical
        self.is_special = is_special

    def effects(self):
        return [
            self.effect_1
        ]

    def effect_1(self, battle):
        battle.foe.hp -= 5
        battle.ally.hp += 5
        return battle.foe.name + ': ' + str(battle.foe.hp) + '\n' + battle.ally.name + ': ' + str(battle.ally.hp)


