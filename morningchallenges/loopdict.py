#!/usr/bin/env python3


fruitcompanies= [{"name":"Zesty","employees":["Bryan", "Colin", "Erik", "Greg", "John"]},
                 {"name":"Ripe.ly","employees":["Kishor", "Leia", "Maria", "Chad"]},
                 {"name":"FruitBee","employees":["Monte", "Jarrad", "Pemba", "Don"]},
                 {"name":"JuiceGrove","employees":["Tim", "Travis", "Trung"]}]

#for x in fruitcompanies[0]["employees"]:
    #print(x)


#choice = input("Choose a company: Zesty, Ripe.ly, FruitBee, JuiceGrove\n")

#for company in fruitcompanies:
   # if choice == company["name"]:
       # print(company["employees"])
fruitcompanies[1]["employees"].remove("Chad")
x = 0 
for company in fruitcompanies:
    x += 1 
    print(f"{x}. {company['name']}")

choice = int(input("Choose your company!\n"))

for x in fruitcompanies[choice - 1]["employees"]:
    print(x)
