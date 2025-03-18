list1 = [5, 10, 15, 20, 25, 50, 20]
list1[3] = 200
print(list1)

a_tuple = (10, 20, 30, 40)
a = a_tuple[0]
b = a_tuple[1]
c = a_tuple[2]
d = a_tuple[3]
print(a) # should print 10
print(b) # should print 20
print(c) # should print 30
print(d) # should print 40

new_list = ["Gabby", "Alex", "Sharon", "Gabby", "Alex", "Samuel", "Gabby", "Samuel"]
new_set_list = set(new_list)
print(new_set_list)
print(list(new_set_list))


num = int(input("Enter a number: "))
print(f"Multiplication table of {num}:")
for i in range(1, 21):
    print(f"{num} x {i} = {num * i}")

a_number = 1

while a_number < 11:
   # print(a_number)
    #a_number += 1

active = True

while active: 
    city = input("Please enter the name of a city you have visited (enter 'quit' when you are finished): ")
    if city == 'quit':
        active = False
    elif city == 'leave me alone':
        active = False
    elif city == 'stop':
        active = False
    else:
        print("I'd love to go to", city)

print("Goodbye !")
