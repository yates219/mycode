#!/usr/bin/env python3

import pandas as pd

cars = pd.read_csv('cars.csv') # creates a DF

cheapest = cars["Price"].min() # this gathers the lowest value of price in the file
expensive = cars["Price"].max() # this gathers the highest value

def main():
    
    choice = input("Do you want to know the cheapest or more expensive car? ").lower()
        
    if choice == "cheapest":
        print(cheapest)

    elif choice == "expensive":
        print(expensive)

    else:
        print("Please try another input")

main()
