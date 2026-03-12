print("Requirement 1 : Ask the user for two numbers and print their product (multiplication)")
Number_user1 = int(input("Please enter first number to multiply"))
Number_user2 = int(input("Please enter second number to multiply"))
Result = Number_user1 * Number_user2
print(f"The multiplication of {Number_user1} and {Number_user2} are =", Result)

print("Requirement 2 : Make a list of your three favorite colors and print them one by one using a loop")
MyFav_colors = ["Green", "White", "Blue"]
for i in MyFav_colors:
    print(i)

print("Requirement 3 : Write a function that takes a name as input and prints “Hello, [name]!")
def take_name_and_Greet():
    input_name = input("Please enter your name")
    print(f"Hello, {input_name}, welcome to python learnings")
take_name_and_Greet()

My_pet = {"Type" : "Dog", "Name" : "Julee"}
print(f"I have a pet which is a {My_pet['Type']} and her name is {My_pet['Name']}")

default_number = 5
while default_number > 0:
    print("Printing 5 to 1", default_number)
    default_number -= 1