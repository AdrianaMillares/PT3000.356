"""
S6. Input and Output in Python
Author: Adriana Millares
Date: 25/08/2023
"""

#1.	Display Hola Mundo, my name is your-name.
"""
Input -> No input
Process 
  1. Display the sentence with your name
Output -> Hola Mundo, my name is Adri
"""

print("Hola Mundo, my name is Adri\n")

#2. Input the user’s name.
"""
Input -> Name
Process 
  1. Ask the user for their name
  2. Display the name given by the user
Output -> User's name: [name]
"""

name = input("Type your name: ")
print("User's name:", name)
print()

#3.	Display three animals in the same line (separated by a space).
"""
Input -> No input
Process 
  1. Display three animals
Output -> Bear, Bird, Bee
"""

#Option 1
print("Option 1")
print("Bear Bird Bee")

print()

#Option 2
print("Option 2")
print("Bear",end=" ")
print("Bird",end=" ")
print("Bee\n\n")

#4.	Display three even numbers in different lines. 
"""
Input -> No input
Process 
  1. Display three even numbers
Output -> 2
          4
          6
"""

#Option 1
print("Option 1")
print(2)
print(4)
print(6)
print()

#Option 2
print("Option 2")
print("2\n4\n6\n")


#5.	Input the user’s address
"""
Input -> Epigmenio González 500, San Pablo, 76130 Santiago de Querétaro, Qro.
Process 
  1. Ask the user for an addess
  2. Display the addres given by the user
Output -> Address: Epigmenio González 500, San Pablo, 76130 Santiago de Querétaro, Qro.
Process 
"""

address = input("Type an address: ")
print("Address:", address)
print()

#6.	Display a verse poem (4 lines) with the corresponding heading.
"""
Input -> No input
Process 
  1. Display the name and author of the poem 
  2. Display the poem in 4 lines
Output -> I’m Nobody! Who are you? | Emily Dickinson
          I’m Nobody! Who are you?
          Are you – Nobody – too?
          Then there’s a pair of us!
          Don't tell! they'd advertise – you know!
"""

#Option 1
print("Option 1")
print("============================")
print("| I’m Nobody! Who are you? |")
print("|      Emily Dickinson     |")
print("============================")
print("I’m Nobody! Who are you?\n Are you – Nobody – too?\n Then there’s a pair of us!\n Don't tell! they'd advertise – you know!\n")


#Option 2
print("Option 2")
print("============================")
print("| I’m Nobody! Who are you? |")
print("|      Emily Dickinson     |")
print("============================")
print("I’m Nobody! Who are you?")
print("Are you – Nobody – too?") 
print("Then there’s a pair of us!")
print("Don't tell! they'd advertise – you know!\n")

#7.	Ask the user if he liked your poem.   
"""
Input -> User answer
Process 
  1. Ask the user if they like the poem (use the user's name)
  2. Tell the user thank you!
Output -> Thank you!
"""

print(name,"Do you like the poem?\n")
input()
print("\nThank you!\n")

#8.	Display See you soon =)
"""
Input -> No input
Process 
  1. Display the sentence See you soon =)
Output -> See you soon =)
"""
print("See you soon =)")
