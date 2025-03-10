# Ask the user for a string
import random #we need that function to get the bonus !!

user_input = input("Please enter a string: ")

# Check the length of the string
if len(user_input) < 10:
    print("string not long enough")
elif len(user_input) > 10:
    print("string too long")
else:
    print("perfect string")
    
    # Print the first and last characters of the string
    print("First character:", user_input[0])
    print("Last character:", user_input[-1]) #I found that -1 goes to the last character of the string

for i in range(len(user_input)):
        print(user_input[i])

#We transform our string into a list named work_list to make the random.shuffle function
work_list = list(user_input)
random.shuffle(work_list)
#Now we change the list into a string
shuffle_string = "".join(work_list)
print(shuffle_string)