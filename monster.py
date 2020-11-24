class Monster:
    def __init__(self, name, number, status, hp, max_hp):
        self.name = name
        self.number = number
        self.status = status
        self.hp = hp
        self.max_hp = max_hp

    def hit(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0

