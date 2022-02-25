#!/usr/bin/env python3

import csv
cheapest= 999999999
highest = 0
with open("cars.csv", "r") as carfile:
    carlist = csv.DictReader(carfile)
    question = input("Do you want to know the cheapest or most expensive car? ").lower()
    if question == "cheapest":
        for row in carlist:
            x= float(row["Price"])
            if x < cheapest:
                cheapest = x
                print(f"The cheapest car is {x}")

    if question == "expensive":
        for row in carlist:
            x= float(row["Price"])
            if x > highest:
                highest = x 
                print(f"The most expensive car is {x}")
            print(x)
            
