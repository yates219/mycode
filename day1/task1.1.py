icecream = ["indentation", "spaces"]
tlgstudents= ["Bryan", "Colin", "Erik", "Gregory", "John", "Kishor", "Leia", "Maria", "Monte", "Jarrad", "Pemba", "Don", "Tim", "Travis", "Trung"]
icecream.append("4")
studentid= int(input("Enter a number from 0 - 14: "))
selection= tlgstudents[int(studentid)]
# <student_name> always uses <4> <spaces> to indent.
print(selection + " always uses " + icecream[2] + " " + icecream[1] + " to indent.")
