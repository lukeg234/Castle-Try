import random

class Player():
    def __init__(self, name, health, value):
        self.name = name
        self.health = health
        self.location = randint(0,5)
        self.inventory =['Torch', 'Stick']
        self.value = value

    def move(self,row,col):
        self.location = [row,col] 

class Item():
    def __init__(self, name, value):
        self.name = name
        self.value = value

def get_random_item():
    item1 = Item('a bar of gold',100)
    item2 = Item('a branch',10)
    item3 = Item('fuck all',0)
    item_list = [item1,item2,item3,item3,item3,item3,item3] 
    random_item = random.choice(item_list)
    item_value = random_item.value
    return (random_item.name,item_value)

def randint(x,y):
    random_row = random.randint(x,y)
    random_col = random.randint(x,y)
    return [random_row] , [random_col]

def move_player():
    current_row = player1.location[0]
    current_col = player1.location[1]
    print(current_row,current_col)
    while True:
        goodinput = False
        while not goodinput:
            try:
                print("")
                row = int(input('Enter a row >>  '))
                col = int(input('Enter a col >> '))
                if (row >= 0 or col >= 0) and ([row] != current_row) and ([col] != current_col): #if positve
                    goodinput = True
                else:
                    print("New location MUST not be current location and MUST be positive numbers ")
            except ValueError:
                print("That's not an integer")
        player1.move(row,col)
        print('You have moved to location >> [{}],[{}]'.format(player1.location[0],player1.location[1]))
        item = get_random_item()
        item_name = item[0]
        item_value = item[1]
        print('well done you found {} it has a value of {}'.format(item_name,item_value))
        player1.inventory.append(item)
        player1.value += item_value

player1 = Player('Luke', random.randint(0,100), 0)
print('''
Welcome to Castle game
Name >> {}
Health >> {}%
Location in room >> {},{}
Inventory >> {}
Inventory value >> {}
'''.format(player1.name, player1.health, player1.location[0],player1.location[1], player1.inventory, player1.value))

move_player()

