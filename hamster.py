from monster import monster


class Naruto(monster):

    def __init__(self, name, health=20, mode='Attack'):
        self.__name = name
        self.__health = health
        self.__mode = mode

    def __str__(self):
        return "The best ninja in Konoha Village"

    def getName(self):
        return self.__name

    def getDescription(self):
        return "The best ninja in Konoha Village"

    def basicAttack(self, enemy):
        enemy.doDamage(11)

    def basicName(self):
        return "Rasen Shuriken"

    def defenseAttack(self, enemy):
        if self.__mode == 'Attack':
            self.__mode = 'Defend'

    def defenseName(self):
        return "Sage Mode"

    def specialAttack(self, enemy):
        enemy.doDamage(15)

    def specialName(self):
        return "Tailed Beast Bomb Rasen Shuriken"

    def getHealth(self):
        return self.__health

    def doDamage(self, damage):
        if self.__mode == 'Defend':
            self.__health = self.__health - (damage / 4)
        else:
            self.__health = self.__health - damage

    def resetHealth(self):
        self.__health = 20


class TenTails(monster):
    def __init__(self, name, health=40, mode='Attack'):
        self.__name = name
        self.__health = health
        self.__mode = mode

    def __str__(self):
        return "the most powerful creature in the Naruto universe"

    def getName(self):
        return self.__name

    def getDescription(self):
        return "the most powerful creature in the Naruto universe"

    def basicAttack(self, enemy):
        enemy.doDamage(4)

    def basicName(self):
        return "Shadow Clone"

    def defenseAttack(self, enemy):
        if self.__mode == 'Attack':
            self.__mode = 'Defend'

    def defenseName(self):
        return "Art of Rinne Rebirth"

    def specialAttack(self, enemy):
        enemy.doDamage(8)

    def specialName(self):
        return 'Tailed Beast Bomb'

    def resetHealth(self):
        self.__health = 20

    def getHealth(self):
        return self.__health

    def doDamage(self, damage):
        if self.__mode == 'Attack':
            self.__health = self.__health - damage
        else:
            self.__health = self.__health - (damage / 2)


class Dio(monster):

    def __init__(self, name, health=30, mode='Attack'):
        self.__name = name
        self.__health = health
        self.__mode = mode

    def __self__(self):
        return "A human turned vampire"

    def getName(self):
        return self.__name

    def getDescription(self):
        return "Hinjaku Hinjaku"

    def basicAttack(self, enemy):
        enemy.doDamage(8)

    def basicName(self):
        return "MUDAMUDAMUDAMUDA"

    def defenseAttack(self, enemy):
        if self.__mode == 'Attack':
            self.__mode = 'Defend'

    def defenseName(self):
        return "Toki wo tomare"

    def specialAttack(self, enemy):
        enemy.doDamage(30)

    def specialName(self):
        return "ROADA ROLLERDA"

    def getHealth(self):
        return self.__health

    def doDamage(self, damage):
        if self.__mode == 'Attack':
            self.__health = self.__health - damage
        else:
            self.__health = self.__health - (damage / 3)

    def resetHealth(self):
        self.__health = 30


class Guy(monster):

    def __init__(self, name, health=15, mode='Attack'):
        self.__name = name
        self.__health = health
        self.__mode = mode

    def __self__(self):
        return "Master of Taijutsu"

    def getName(self):
        return self.__name

    def getDescription(self):
        return "The roaring youth of the Hidden Leaf"

    def basicAttack(self, enemy):
        enemy.doDamage(10)
        self.__health -= 2

    def basicName(self):
        return "HIRUDORA"

    def defenseAttack(self, enemy):
        if self.__mode == 'Attack':
            self.__mode = 'Defend'

    def defenseName(self):
        return "SEKIZO"

    def specialAttack(self, enemy):
        enemy.doDamage(35)
        self.__health = 1

    def specialName(self):
        return "NIGHT GUY"

    def getHealth(self):
        return self.__health

    def doDamage(self, damage):
        if self.__mode == 'Attack':
            self.__health = self.__health - damage
        else:
            self.__health = self.__health - (damage * 4)

    def resetHealth(self):
        self.__health = 15

