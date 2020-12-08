from array import array

#array that contains all the clues
clues_list_array = ["an adjective","a noun","a verb, past tense", "an adverb","an adjective","a noun","a noun","an adjective","a verb","an adverb","a verb, past tense","an adjective"]
clues_array_length = len(clues_list_array)

print("Welcome to Mad Lib! You will be presented a series of inputs, please fill in the blanks:\n")

user_inputs_array = []

#the program stores the user's entries in another array
for index in range(clues_array_length):
        user_input = input("Write " + clues_list_array[index] + ": ")
        print("\n")
        user_inputs_array.append(user_input)

#the program prints the user's entries in the blank parts of the story
print("A DAY AT THE ZOO.\n")
print("Today I went to the zoo. I saw a "+ user_inputs_array[0] + " " + user_inputs_array[1] + " jumping up and down in its tree.")
print("He " + user_inputs_array[2] + " " + user_inputs_array[3] + " through the large tunnel that led to its " + user_inputs_array[4] + " " + user_inputs_array[5] + ".")
print("I got some peanuts and passed them through the cage to a gigantic " + user_inputs_array[6] + " towering above my head.")
print("Feeding that animal made me hungry. I went to get a " + user_inputs_array[7] + " scoop of ice cream.")
print("It filled my stomach. Afterwards I had to " + user_inputs_array[8] + " " + user_inputs_array[9] + " to catch our bus.")
print("When I got home I " + user_inputs_array[10] + " my mom for a " + user_inputs_array[11] + " day at the zoo.\n")