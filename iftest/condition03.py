#!/usr/bin/env python3
hostname = input("What value should we set for hostname? ")
## Notice how the next line has changed
## here we use the str.lower() method to return a lowercase string
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg") 
    print("Hostname matches expected config.") 

print("Exiting the script.") # displays a line no matter the outcome of if statement

