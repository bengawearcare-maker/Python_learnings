a = 5
b = 10
a,b = b,a # swap the values of a and b
print("a is", a)
print("b is", b)
print(type(a))
print(type(b))
from_input = input("Enter your name")
print("Hello", from_input, "Welcome to Python programming")
from_age = input("Enter your age")
print("Your age is", from_age)
print(type(from_age))

ECU_name = "BCM"
Network_name = "CAN"
Baudrate = 500
print(f"You are working with {ECU_name} and with network {Network_name} having baudrate of {Baudrate} kbps")

for i in range(0, 6):
    print("Karamath" * i)

for i in range(3,0, -1):
    print("sheik" *i)

path = r"C:\Python\test.txt"
with open(path, "w") as w:
    w.write("This text is writtern by script")

with open(path, "r") as r:
    Read_Lines = r.read()
    print("Automation reading",Read_Lines)

Name = "Karamath"
List_Names = ["Sheik","Mohammad","Inaaya"]
Dic_names = {"Surname": "Sheik", "First name" : "Innaya", "Middle Name" : "Mohammad"}
tupple_names = ("Sheik","Mohammad","Inaaya")
print(List_Names[0])
print(List_Names[1])
print(List_Names[2])
print(Dic_names["Surname"])
print(Dic_names["First name"])
print(Dic_names["Middle Name"])
print(tupple_names[0])
print(tupple_names[1])
print(tupple_names[2])

with open(path, "a") as a:
    a.write("\n\nThis is written when this function call is 2")


with open(path, "r") as r:
    Read_Lines = r.read()
    print("Automation reading when function call 2",Read_Lines)

Two_words = ["Hello","Inaaya"]
Join_words = ' '.join(Two_words)
print(Join_words)

Twwo_words = {"Name": "Karamath", "Surname": "Sheik"}
Join_Twwo_words = ' '.join(Twwo_words.values())
print(Join_Twwo_words)

Splitting = Join_Twwo_words.split()
print(Splitting)
print(Splitting[0])
print(Splitting[1])

List_of_numbers = [1,2,3,4]
List_of_numbers.append(10)
print(List_of_numbers)

List_of_numbers.extend([20,21,23])
print(List_of_numbers)

List_of_numbers.insert(5,6)
print(List_of_numbers)

Remove_number = List_of_numbers.pop()
print("Removed number is", Remove_number)
print(List_of_numbers)

String_replace = {"Name":"Karamath","Surname":"Sheik"}
S_replaced_with = String_replace["Surname"].replace("Sheik","Mohammed")
print("Replaced Sheik with :" + S_replaced_with)
print(String_replace["Name"] + " " + S_replaced_with)

String_formatting = "Karamath"
Greeting = f"Hello {String_formatting}"
print(Greeting)
