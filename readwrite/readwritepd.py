#!/usr/bin/env python3

import pandas as pd

cars = pd.read_csv('cars.csv')

cheapest = cars["Price"].min()
expensive = cars["Price"].max()

x = "yes"

def main():
    
    choice = input("Do you want to know the cheapest or more expensive car? ").lower()
        
    if choice == "cheapest":
        print(cheapest)

    elif choice == "expensive":
        print(expensive)

    else:
        print("Please try another input")

main()
