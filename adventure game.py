# LAB: ADVENTURE GAME
#
# Save your solution in a directory in practice/ named adventure.
#
# Write a NetHack-like terminal based dungeon crawler game.
#
# There are various entities in the game.
# Make each entity a class in it’s own module.
#
# Creature
#
# Location
# Health
# Weapon
# Weapon
#
# Location (or None if picked up)
# Damage
# Potion
#
# Location
# Health Restored
# Put any functions that manipulate these classes in their respective modules.

# CREATURES
class creatures():
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    def is_alive(self):
        return self.hp > 0
class onepercent(creatures):
    def __init__(self):
    super().__init__(name="The One Percent", hp=999, damage=4)
class man(creatures):
    def __init__(self):
    super().__init__(name="Modern Man", hp=50, damage=1)
class police(creatures):
    def __init__(self):
    super().__init__(name="The Police", hp=150, damage=15)
#super class
class Item():
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

        def __str__(self):
            return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)
#gold item
class Knowledge(Item):
    def self __init__(self, amt):
        self.amt = amt
        super().__init__(name="Knowledge",
                        description="Nothing more valuable",
                        value = self.amt)
    # WEAPONS
class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)
class Mind(Weapon):
    def __init__(self):
        super().__init__(name="Mind",
                         description="The most powerful",
                         value=0,
                         damage=5)
class Gun(Weapon):
    def __init__(self):
        super().__init__(name="Gun",
                         description="Dangerous in all hands",
                         value=10,
                         damage=15)
class Money(Weapon):
    def __init__(self):
        super().__init__(name="Money",
                         description="Blind with Influence",
                         value=50,
                         damage=10)
# POTIONS
class Potions(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)
class soul(Potions):
    def __init__(self):
        super().__init__(name="Soul",
                         description="keep the faith",
                         value=10,
                         damage=(-20))
class influence(Potions):
    def __init__(self):
        super().__init__(name="Influence",
                         description="denounce truth",
                         value=30,
                         damage=(-10))
