#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
  eat [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  print('Consumed: ' + str(consumed))
  #print any items consumed

  #shows items in room
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")

  if "consumable" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['consumable'])
    print("---------------------------")
   
  ## Display message about if monster is alive when you are in the pantry
  if currentRoom == 'Pantry' and 'death' in rooms['Cellar']:
    print('There seems to be something lurking to the North..') 
    print("---------------------------")

  ## Display hint to eat cookie
  if 'cookie' not in consumed:
    print('You seem to be hungry')

  ## Display hint to kill monster
  if 'monster' in rooms['Cellar']:
    print('There is something in the house not letting you out')

  ## Display hint to get key
  if 'key' not in inventory:
    print('You need something to unlock the gate thats in the Garden')

  ## Display hint to get marp
  if 'map' not in inventory:
    print('There must be something around to help you navigate once you escape')
    
#an inventory, which is initially empty
inventory = []
consumed = []
#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
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

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory.append(move[1])
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      
      #if they type eat
  if move[0] == 'eat':
      #if the room contains a consumable
    if 'consumable' in rooms[currentRoom] and move[1] in rooms[currentRoom]['consumable']:
      # add consumable to consumed
      consumed.append(move[1])
      #tell them they consumed
      print(move[1] + ' eaten!')
      #remove the consumable from room
      del rooms[currentRoom]['consumable']
      #if they aren't able to consume the item
    else:
      print('Can\'t eat ' + move[1] + '!')
  
  ## Dying from eating questionable berries
  if 'deathberry' in consumed:
    print('--------------------------')
    print('WHY WOULD YOU EAT A DEATHBERRY?!?! YOU DIED!')
    break

  ## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'map' in inventory and 'death' not in rooms['Cellar'] and 'cookie' in consumed:
    print('You killed the Monster and escaped the house with the ultra rare key and map...all while getting a snack. YOU WIN!')
    break

  ## Killing the monster
  elif currentRoom == 'Cellar' and 'knife' in inventory:
    print('A Monster appeared and you stabbed it with your knife, killing it!')
    del rooms[currentRoom]['death'] # deletes the monster from the room so you can win
    inventory.remove('knife')

  ## If a player enters a room with a monster
  elif 'death' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['death']:
    print('A monster has got you... GAME OVER! Try finding a weapon next time! ')
    break
