#Take a string from a user input
user_input = input("Enter a string: ")

#Remove any spaces and line breaks inside the string the user has input
modified_string = user_input.replace(" ", "").replace("\n","")

#Displays the user's string without any spaces
print("Modified string:", modified_string)
