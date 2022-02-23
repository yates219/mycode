#!/usr/bin/env python3

# A script to help you pick out a car
print("Lets see what type of car you should get!")

x = True

while x == True: #continue to run script after prompted when complete
    
    answer = input("Do you prefer speed or comfort? ") # choose between speed/comfort
    if answer == "speed":
        speedcar = input("Do you want to spend more or less than $50,000? ").lower() # specify the amount wanting to spend
        
        if speedcar == "more":  # spending more than $50,000          
            speedcarmake = input("Would you prefer Ford, Chevy, or Dodge? ").lower() # specify car make preference
            
            if speedcarmake == "ford":  # output for a Ford
                print("You should buy a Ford Mustang GT500")
            
            elif speedcarmake == "chevy": # output for a Chevy
                print("You should buy a Chevy Corvette C8")
            
            elif speedcarmake == "dodge": # output for a Dodge
                print("You should buy a Dodge Challenger Hellcat")
            
            else: # output for any input not described above
                print("You either did not type the name correctly or we have different taste...")
            
            

        if speedcar == "less": # spending less than $50,000
            speedcarmake = input("Would you prefer Ford, Chevy, or Dodge? ").lower()
            
            if speedcarmake == "ford": # choosing a ford
                print("You should buy a Ford Mustang GT")
                
            elif speedcarmake == "chevy": # choosing a Chevy
                print("You should buy a Chevy Camaro SS")
                
            elif speedcarmake == "dodge": # choosing a Dodge
                print("You should buy a Dodge Challenger or Charger R/T")
            
            else: # did not notice input
                print("You either did not type the name correctly or we have different taste...")
            
        
    elif answer == "comfort": # choosing comfort over speed
        comfortcar = input("Do you prefer Honda, Chrysler, or Hyundai? ").lower() # asking which make they prefer
        
        if comfortcar == "honda": # choosing a honda
            print("You should buy a Honda Accord")
        
        elif comfortcar == "chrysler": # choosing a chrysler
            print("You should buy a Chrysler 300")

        elif comfortcar == "hyundai": # choosing a hyundai
            print("You should buy a Hyundai Sonata")
        
        else: # not noticing input
            print("You're on your own!")
  
    else:
        print("That was not the correct input")

    tryagain = input("Would you like to look again?(Yes/No) ").lower() # Prompt to either start loop again or exit script
    if tryagain == "yes":
        x = True
    else:
        x= False

