import math
# cruise_speed = 80
# print ("cruise speed is", cruise_speed)

# name = input("What is your name? ")
# print("Hello", name, "welcome to python learnings")

# age = input("What is your age? ")
# print("your age is" , age, "years old")
# print (type(age))

# Default = 31
# if age > str(Default):
#     print("you are eligible for driving")
# else:    
#     print("you are not eligible for driving")

print (5+3)
print("Hi" + " "+ "Karamath")

for i in range(5):
    if i == 0:
        print("[0] is 0")
    else:
        print("not 0")

count = 0
while count < 5:
    print(count)
    count += 2

def add():
    print  ("This is add function")
    print(math.sqrt(2))

add()


path = "C:/Python/ACC.py"
with open(path, "r") as f:
    data = f.read()
    print(data)

class Dog: 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof! Woof!")
my_dog = Dog("Buddy", 3)
my_dog.bark()

url = "https://github.com/bengawearcare-maker/Python_learnings/commit/82040d45a4264143e4abb628521b414ef9d63e10"
list_names = ["Karamath","sheik","mohammad"]
dic_name = {"name1":"Karamath","name2":"sheik","name3":"mohammad"}
tuple_name = ("karamath","sheik","mohammad")
print(list_names[1])
print(dic_name["name2"])
print(tuple_name[1])
if list_names[1] == dic_name["name2"] == tuple_name[1]:
    print("both are same")
else:
    print("both are different")

t_url = url.split("/")[-4]
print(t_url)

for i in range(0, 10):
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")

for i in range(1, 11):
    print("@"   * i)

for i in range (11,1,-1):
    print("@" * i)

a = 5
b = 10
a,b = b,a # swap the values of a and b
print("a is", a)
print("b is", b)