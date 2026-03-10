print("Requirement 1 : Print your favorite color")
User_fav_color = str(input("Please enter your favorite color"))
print(f"Wow! {User_fav_color} color is a great choice")

print(" Requirement 2 : Create a variable for your age and print it")
print("****WELCOME TO BANGALORE****")
my_age =int(input("Please enter your age"))
if my_age < 13:
	print("You are a kid")
elif my_age >=13 and my_age<=18:
	print("You are a teenager")
else:
	print("You are an adult")

print("Requiremtn 3 : Add two numbers and print the result")
Var1 = 10
Var2 = 20
print(f"Addition of {Var1} and {Var2} is = ", Var1 +Var2)

print(" Requirement 4 : Ask the user for their name and greet them")
Ask_name = str(input("May I know your name please"))
print(f"Hey! {Ask_name}, thank you letting me know your name")

print(" Requirement 5 : If a number is greater than 10, print Big number!")
List_of_bignumber= [1,3,10,15,20,25]
print(f"The biggest number amount the list {List_of_bignumber} is ", max(List_of_bignumber))

print(" Requirement 6 : Print each letter in the word dog using a loop")

for name in "dog":
	print(f"Letter is {name}")

	
print(" Requirement 7 : Make a list of three animals and print the first one")
Animals_names = {"Animal1": "Tiger","Animal2": "Lion","Animal3": "Camel"}
print(f"In the existing list of Animals which are {Animals_names}, the first one is", Animals_names["Animal1"])

print("Requirement 8 : Write a function that prints Good morning")

def Good_Morning():
	print("Good Morning")
Good_Morning()

print("Requirement 9 : Make a dictionary for a book with keys title and author, and print the title")
Details = {"Book_Name1": "Karamath", "Author" : "Geetha", "Title":"How to change your life with marriage"}
print(f"I have written a book name called {Details['Book_Name1']} and my name is {Details['Author']} and the book tittle is {Details['Title']}")

print("Requirement 10 : Use a while loop to print numbers from 1 to 5")
Varr1 = 0
while Varr1 < 5:
	Varr1 +=1
	print("Printing 1 to 5", Varr1)
	