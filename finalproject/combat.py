#!/usr/bin/env python3

# This is a script for defining the player, enemies, and combat for the finalrpg.py game.
import random 
import time

def combat():

    player_health = 100
    enemy_health = 100
    
    enemy_attack = randint(1,10)

    while player_health == 100 and enemy_health = 100:
        if 'knife' in inventory:
            player_attack = randint(10,20)
            enemy_health -= player_attack
            time.sleep(.5)
            player_health -= enemy_attack
            time.sleep(.5)

        else:
            player_attack = randint(1,5)
            enemy_health -= playerattack


