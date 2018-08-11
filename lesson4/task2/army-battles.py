# Taken from mission The Warriors

class Warrior(object):
    def __init__(self, name={}):
         self.name= name
         self.health = 50
         self.attack = 5
         self.is_alive = True
        
class Knight(Warrior):
   def __init__(self, name={}):
         self.name= name
         self.health = 50
         self.attack = 7
         self.is_alive =True
       

def fight(unit_1, unit_2):
    while unit_1.health > 0 and unit_2.health > 0 :
        if unit_1.health > 0:
            unit_2.health = unit_2.health - unit_1.attack
            if unit_1.health > 0 and unit_2.health <= 0:
                unit_2.is_alive = False
                return True
                return unit_2.is_alive
                return unit_1.is_alive
            elif unit_1.health <= 0 and unit_2.health > 0:
                unit_1.is_alive = False
                unit_2.is_alive = True
                print ("u2", unit_2.is_alive, "u1", unit_1.is_alive)
                return False 
                return unit_2.is_alive
                return unit_1.is_alive
        if unit_2.health > 0:
            unit_1.health = unit_1.health - unit_2.attack
            if unit_1.health > 0 and unit_2.health <= 0:
                unit_2.is_alive = False
                return True
                return unit_2.is_alive
                return unit_1.is_alive
            if unit_1.health <= 0 and unit_2.health > 0:
                unit_1.is_alive = False
                return False 
                return unit_2.is_alive
                return unit_1.is_alive
        
class Army(object):
    def add_units(self, name, number):
        self.name= name
        self.name()
        self. number_of_units = number

class Battle(object):
   def fight(self, army_1, army_2):
       while army_1.number_of_units > 0:
           print ("xd")
    
       
    
        
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

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

    print("Coding complete? Let's try tests!")


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
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

    #battle tests
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
    print("Coding complete? Let's try tests!")