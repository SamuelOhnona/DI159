#Mandatory Exercises bellow

#1
print("Hello world\n" * 4, end="")

#2
print((99**3)*8)

#3
print(5 < 3) #False 
print(3 == 3) #True
print(3 == "3") #False
print("3" > 3) #Error#@print("Hello" == "hello")#False

#4
computer_brand = "Apple"
print(f"I have an {computer_brand} computer")

#5
name = "Samuel"
age = 25
shoe_size = 44
info = f"My name is {name}, I am {age} and my shoe size is {shoe_size}"
print(info)

#6
a = 15
b = 8
if a > b:
    print("Hello World")
else:
    print("Goodbye World")

#7
num = int(input("Enter a number : "))

if num % 2 == 0:
    print("Number is pair.")
else:
    print("Number is impair.")

#8
my_name = "Samuel"
name_user = input("Enter your name :")

if my_name == name_user:
    print("WOWWWW we have the same name !!!!")
else:
    print("I prefer my name")

#9
height = int(input("Enter your height in cm: "))

if height > 145:
    print("You are tall enough to ride!")
else:
    print("Sorry, you need to grow a bit more to ride.")


## EXERCISES XP NON MANDATORY GOLD

month = int(input("Enter a month (1-12):")) #Ask the user for a month

if 3 <= month <= 5:
    print("Spring")
elif 6 <= month <= 8:
    print("Summer")
elif 9 <= month <= 11:
    print("Autumn")
elif month == 12 or 1 <= month <= 2:
    print("Winter")
else:
    print("Invalid month! Please enter a number between 1 and 12.")

## EXERCISES XP NON MANDATORY NINJA

#3

3 <= 3 < 9 #True
3 == 3 == 3 #True
bool(0) #False
bool(5 == "5") #False
bool(4 == 4) == bool("4" == "4") #True
bool(bool(None)) #False
x = (1 == True) #True
y = (1 == False) #False
a = True + 4 
b = False + 10
print("x is", x) # x is True
print("y is", y) # y is False
print("a:", a) # a : 5
print("b:", b) # b : 10

#4
my_text = "Sorry, but it was difficult to copy paste the latin text that you putted on the octopus ahahah"
print(len(my_text))

#5

longest_sentence = ""

while True:
    sentence = input("Enter the longest sentence you can without the letter 'A': ")

    if "A" in sentence or "a" in sentence:
        print("Your sentence contains the letter 'A'. Try again!")
        continue

    if len(sentence) > len(longest_sentence):
        longest_sentence = sentence
        print("🎉 Congrats, you have the new record")

    print(f"Current longest sentence: {longest_sentence}")


