#description = "strings are..."
#print(description.upper())
#print(description.replace("are", "is"))
#print(description.replace("are...", " "))

#first_name = "Samuel"
#last_name = "Ohnona"
#print(first_name, last_name)
#print("the cow says, \"moo\"")

#x = 5
#y = 10
#z = 0
#word1 = "hello"
#word2 = "world"

#print(x < y and y > z)
#print(word1 != word2)
#print(bool(z))
#print(bool(word1))

#name = "alice"
#age = 30
#city = "New York City"
#print(f"Hello, {name}, you have {age} years old and live in {city}")

#next_week = input("What do you want to do next week ? ")
#print(f"You want to {next_week} next week")

#age = int(input("How old are you? "))
#print(f"Next year you will be {age + 1} years old")

#my_height = int(input("How tall are you ? "))

#if my_height > 200:
    #print("You are to tall to ride")
#elif my_height < 150 :
    #print("you are too short to ride")
#else:
    #print("Enjoy the ride")

#if my_height < 150 or my_height > 200:
    #print("You're not in the correct height range")
#else:
    #print("enjoy the ride")

user_num = int(input("Choose a number beetween 1 and 100 "))
#verify if it's a number multiple of 5, 3, or both.
if user_num % 15 == 0:
    print("FizzBuzz")
elif user_num % 3 == 0:
    print("Fizz")
elif user_num % 5 == 0:
    print("Buzz")
else:
    print("No Fizz & No Buzz")