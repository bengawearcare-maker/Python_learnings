print("Requirement 1 : Write code to print your name five times using a loop.")
name = "karamath"
number = 0
for i in range(1, 6):
    number += 1
    print("As per requirement I have printed my name 5 times:", number,")", name)

print("Requirement 2 : Create two variables, swap their values, and print them")
Var1 = 10
Var2 = 20
print ("Before swapping: Var1 =", Var1, "and Var2 =", Var2)
Var1, Var2 = Var2, Var1
print ("After swapping: Var1=", Var1, "Var2 is =", Var2)

print ("Requirement 3 : Ask the user for their age and print “You are a kid!” if the age is less than 13.")
print("Welcome to shoppingMall")
Ask_age = int(input("Please enter your age : "))
if Ask_age < 13:
    print("You are a kid!")
elif Ask_age >= 13 and Ask_age < 18:
    print("You are a teenager!")
else:
    print("You are an adult!")

print("Requirement 4 : Make a list of your three favorite fruits and print the second one.")
List_of_fruits = ["Mango","Banana","orange"]
print(f"In the existing list of fruits {List_of_fruits} I like {List_of_fruits[1]}")

def even_or_odd():
    print("Requirement 5 : Write a function that takes a number and prints “Even” if it’s even, or “Odd” if it’s odd.")
    User_input = int(input("Please enter a number to know even or odd"))
    if User_input %2 == 0:
        print("Even")
    else:
        print("Odd")
even_or_odd()

print("Requirement 6 : Print all numbers from 1 to 10, but only print the even ones.")
for i in range(1,11):
    if i % 2 == 0:
        print("Even number" ,i)

print ("Requirement 7 : Reverse the word “Python” and print it")
Word = "Python"
print(f"{Word} when reversed it will be = {Word[::-1]}")

print("Requirement 8 :Count how many times the letter a appears in the word banana")
Count_of_a = "banana"
print(f"total letter A present in {Count_of_a} = {Count_of_a.count("a")}")
