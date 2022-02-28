#!/usr/bin/python3

# RPG that allows user to move around various rooms. Winning requires obtaining and consuming certain items and killing certain monsters.

def showInstructions():
    # Print a main menu and the commands
    print('''
RPG Game
========
Commands:
    go [direction]
    get [item]
    eat [item]
    hint (Type at anytime for a hint)
''')

def showStatus():
    
    # Print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    
    # Print the current inventory
    print('Inventory : ' + str(inventory))
    
    # Print any items consumed
    print('Consumed: ' + str(consumed))

    # Shows items in room
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
        print("---------------------------")

    # Shows consumables in room
    if "consumable" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['consumable'])
        print("---------------------------")
   
    # Display message about if monster is alive when you are in the pantry
    if currentRoom == 'Pantry' and 'death' in rooms['Cellar']:
        print('There seems to be something lurking to the North..') 
        print("---------------------------")

def hint():
    
    # Display hint to eat cookie
    if 'cookie' not in consumed:
        print('You seem to be hungry')

    # Display hint to kill monster
    if 'death' in rooms['Cellar']:
        print('There is something in the house not letting you out')

    # Display hint to get key
    if 'key' not in inventory:
        print('You need something to unlock the gate thats in the Garden')

    # Display hint to get map
    if 'map' not in inventory:
        print('There must be something around to help you navigate once you escape')
    
    # Display if all objectives complete
    if 'cookie' in consumed and 'death' not in rooms['Cellar'] and 'key' in inventory and 'map' in inventory:
        print("The Garden seems like a good escape")

# Creates an inventory and consumed area, initially empty
inventory = []
consumed = []

# A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key'
                     },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'knife',
                        },
            
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'map',
                  'north' : 'Pantry',
                            },
            
            'Garden' : {
                  'north' : 'Dining Room',
                  'consumable'  : 'deathberry'
                       },
            
            'Pantry' : {
                  'south' : 'Dining Room',
                  'north' : 'Cellar',
                  'consumable' : 'cookie',
                       },
           
            'Cellar' : {
                  'south' : 'Pantry',
                  'death'  : 'monster'
                       }
         }

# Start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# Loop forever
while True:

    showStatus()

    # Get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    # Split allows an items to have a space on them
    # Get golden key is returned ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    # If they type 'go' first
    if move[0] == 'go':
        
        # Check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
           
            # Set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        
        # There is no door (link) to the new room
        else:
            print('You can\'t go that way!')

        # If they type 'get' first
    if move[0] == 'get' :
        
        # If the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            
            # Add the item to their inventory
            inventory.append(move[1])
            
            # Display a helpful message
            print(move[1] + ' obtained!')
            
            # Delete the item from the room
            del rooms[currentRoom]['item']
    
        # Otherwise, if the item isn't there to get
        else:
            # Tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
      
    # If they type eat
    if move[0] == 'eat':
        
        # If the room contains a consumable
        if 'consumable' in rooms[currentRoom] and move[1] in rooms[currentRoom]['consumable']:
        
            # Add consumable to consumed
            consumed.append(move[1])
            
            # Tell them they consumed
            print(move[1] + ' eaten!')
            
            # Remove the consumable from room
            del rooms[currentRoom]['consumable']
     
        # If they aren't able to consume the item
        else:
            print('Can\'t eat ' + move[1] + '!')
    
    # If the user needs a hint
    if move[0] == 'hint':
        hint()

    # Dying from eating deathberry...duh
    if 'deathberry' in consumed:
        print('--------------------------')
        print('WHY WOULD YOU EAT A DEATHBERRY?!?! YOU DIED!')
        break

    # Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'map' in inventory and 'death' not in rooms['Cellar'] and 'cookie' in consumed:
        print('You killed the Monster and escaped the house with the ultra rare key and map...all while getting a snack. YOU WIN!')
        break

    # Killing the monster
    elif currentRoom == 'Cellar' and 'knife' in inventory:
        print('A Monster appeared and you stabbed it with your knife, killing it!')
        del rooms[currentRoom]['death'] # Deletes the monster from the room so you can win
        inventory.remove('knife') # Destroys knife after being used

    # If a player enters a room with a monster
    elif 'death' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['death']:
        print('A monster has got you... GAME OVER! Try finding a weapon next time! ')
        break
