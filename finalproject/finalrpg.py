#!/usr/bin/python3

# RPG that allows user to move around various rooms. Winning requires obtaining and consuming certain items and killing certain monsters.

import random
import time
import os

def showInstructions():
    # Print a main menu as well as a help command
    print('''
RPG Game
========
Commands:
    go [direction] (North, South, East, West)
    look (See what is in current room)
    get [item]
    eat [consumable]
    hint (Type at anytime for a hint)
    help (Display these instructions at any time)
''')

def showStatus():
    
    # Print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    
    # Print the current inventory
    print('Inventory : ' + str(inventory))
    
    # Print any items consumed
    print('Consumed: ' + str(consumed))

def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def look():
    # Call global variables to work with main() function
    global rooms
    global currentRoom
    # Displays items in current room, if any
    if 'item' in rooms[currentRoom]:
        print("You see a " + rooms[currentRoom]['item'])
    # Displays consumables in current room, if any
    elif 'consumable' in rooms[currentRoom]:
        print("You see a " + rooms[currentRoom]['consumable'] + " you could eat")
    else:
        print("Theres nothing in here")
    # Display which way you can go
    if currentRoom == 'Hall':
        print("You see the Kitchen to the South and the Dining Room to the East")
    elif currentRoom == 'Kitchen':
        print("You see the Hall to the North")
    elif currentRoom == 'Dining Room':
        print("You see the Hall to the West, Pantry to the North, and Garden to the South")
    elif currentRoom == 'Pantry':
        print("You see the Dining Room to the South and the Cellar to the North")
        if 'death' in rooms['Cellar']:
            print("There is something lurking in the Cellar")
    elif currentRoom == 'Cellar':
        print("You see the Pantry to the South")
    elif currentRoom == 'Garden':
        print("You see the Dining Room to the North")

def hint():
    
    # Display hint to eat cookie
    if 'cookie' not in consumed:
        print('You are hungry')

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

# Implements combat
def combat():
    # Call global player to allow continuous loop in main() function as well as stopping when player dies
    global player
    # Starting health for player and enemy
    player_health = 50
    enemy_health = 50
    
    # Creates a combat loop that goes until player or enemy die
    while player_health > 0 and enemy_health > 0:
        if 'knife' in inventory:
            player_attack = random.randint(10,20) # Generates random attack damage from 10-20
            enemy_attack = random.randint(5,10)   # Generates random enemy attack damage from 5-10
            enemy_health -= player_attack         # Removes player damage dealt from enemy health
            time.sleep(.5)                        # Slows output
            print(f"You hit the monster for {player_attack} damage!")
            player_health -= enemy_attack         # Removes enemy damage dealt from player health
            time.sleep(.5)                        # Slows output
            print(f"The monster hit you for {enemy_attack} damage!")
            if enemy_health <= 0:                 # If player kills the monster, it will delete monster from room
                print('You defeated the monster!')
                
                 
                    
        else:
            player_attack = random.randint(1,5) # Generates random attack damage from 1-5
            enemy_attack = random.randint(6,10) # Generates random enemy attack damage from 6-10
            enemy_health -= player_attack       # Removes player damage dealt from enemy health
            time.sleep(.5)
            print(f"You hit the monster for {player_attack} damage!")
            player_health -= enemy_attack       # Removes enemy damage dealth from player health
            time.sleep(.5)
            print(f"The monster hit you for {enemy_attack} damage!")
            if player_health <= 0:              # Kills you when you lose the fight
                print("The monster killed you! Better get a weapon next time!")
                player = 'dead' # Kills the player, ending the game
                
            
# Creates an inventory and consumed area, initially empty
inventory = []
consumed = []

# A dictionary linking a room to other rooms with various items
rooms = {

            'Hall' : {
                'south' : 'Kitchen',
                'east'  : 'Dining Room',
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

# Defining our main function
def main():
   
    global player
    global currentRoom
    # Start the player off in the Hall
    currentRoom = 'Hall'
    # Start the player alive so the while loop will begin
    player = 'alive'
    # Display instructions to player
    showInstructions()

    # Loop forever until game is won or player is dead
    while True and player == 'alive':

        showStatus()

        # Get the player's next 'move'
        # .split() breaks it up into an list array
        # eg typing 'go east' would give the list:
        # ['go','east']
        move = ''
        while move == '':
            move = input('>').lower()
            print("---------------------------")
        # Split allows an items to have a space on them
        # Get golden key is returned ["get", "golden key"]          
        move = move.lower().split(" ", 1)

        clear_screen()
        # If they type 'go' first
        if move[0] == 'go':
            
            # Check to see length of input (how many words types)
            # If player doesn't give any input after typing 'go'
            if len(move) < 2: 
                print('Correctly type in which direction you want to go')
                continue
            
            # Check that they are allowed wherever they want to go
            if move[1] in rooms[currentRoom]:          
                # Set the current room to the new room
                currentRoom = rooms[currentRoom][move[1]]
            
            # If player doesn't type in correct direction or puts in a wrong direction
            else:
                print('You can\'t go that way!')

        # If they type 'get' first
        elif move[0] == 'get' :
            
            # Check to see length of input (how many words types)
            # If player doesn't input anything after typing 'get'
            if len(move) <2:
                print('Correctly type in which item you want to get')
                continue

            # If the room contains an item, and the item is the one they want to get
            if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            
                # Add the item to their inventory
                inventory.append(move[1])
            
                # Display a helpful message
                print(move[1].capitalize() + ' obtained!')
            
                # Delete the item from the room
                del rooms[currentRoom]['item']
    
                
            # Otherwise, if the item isn't there to get
            else:
                # Tell them they can't get it
                print('Can\'t get that!')
      
        # If they type eat
        elif move[0] == 'eat':
            
            # Check to see length of input (how many words types)
            # If player doesn't input anything after typing 'eat'
            if len(move) <2:
                print('Correctly type in what you want to eat')
                continue
            
            # If the room contains a consumable
            if 'consumable' in rooms[currentRoom] and move[1] in rooms[currentRoom]['consumable']:
        
                # Add consumable to consumed
                consumed.append(move[1])
            
                # Tell them they consumed
                print(move[1].capitalize() + ' consumed!')
            
                # Remove the consumable from room
                del rooms[currentRoom]['consumable']
     
            # If they aren't able to consume the item
            else:
                print('Can\'t eat that!')
    
        # If the user needs a hint
        elif move[0] == 'hint':
            hint()

        # If the user looks around room
        elif move[0] == 'look':
            look()

        # If the user inputs help
        elif move[0] == 'help':
            showInstructions()

        # If the user inputs something incorrectly
        else:
            print("I don't recognize that command")

        # Dying from eating deathberry...duh
        if 'deathberry' in consumed:
            print('--------------------------')
            print('WHY WOULD YOU EAT A DEATHBERRY?!?! YOU DIED!')
            break

        # Define how a player can win. You must kill the monster, eat the cookie, obtain the key and map, and go to the Garden.
        if currentRoom == 'Garden' and 'key' in inventory and 'map' in inventory and 'death' not in rooms['Cellar'] and 'cookie' in consumed:
            print('You killed the Monster and escaped the house with the ultra rare key and map...all while getting a snack. YOU WIN!')
            break

        # Fighting the monster 
        elif currentRoom == 'Cellar' and 'death' in rooms['Cellar']:
            fight = input('A monster appeared! Do you wish to fight or run? ').lower() # Prompt player if they want to fight or run
            if fight == 'fight': # If player wants to fight
                combat() # Initiates combat
                if player == 'alive': # If player wins the fight, remove monster and ask player to loot 
                    del rooms['Cellar']['death']
                    if 'death' not in rooms['Cellar']:
                        pickup = input("Hmm the monster dropped something...Would you like to pick it up? (Yes/No) ").lower()
                    if pickup == 'yes': # If player decides to pick up key it will add to inventory 
                        print("Key obtained!")
                        inventory.append('key')
                    else: # If player does not pick up key, it will leave the key in the Cellar so you can come back to grab it
                        rooms['Cellar'].update({'item':'key'})
                    
            elif fight == 'run':
                print('You successfully escaped!')
                currentRoom = 'Pantry'
            else:
                print('I don\'t recognize that command, I placed you back into the Pantry for safety')
                currentRoom = 'Pantry'
        
                

if __name__ == "__main__":
    main()
