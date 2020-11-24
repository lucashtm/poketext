import sys
from attack import Attack
from monster import Monster
from battle import Battle

def main(argv):
    foe = Monster('scyter', 123, 0, 100, 100)
    ally = Monster('bulbasaur', 1, 0, 100, 100)
    battle = Battle(foe, ally)
    att = Attack('splash', 0, 100, False, True)
    for effect in att.effects():
        sys.stdout.write(effect(battle))
    sys.stdout.write('\n')

if __name__ == '__main__':
    main(sys.argv)

