#Lab 1 (3 points)
#1. Install your favorite IDE on your computer so you can still program without access to internet.
#2. Write and save a program that prints out your name and waits for the user to Press the Enter
#key before the program ends.
print("My Name is Matt")
end_program = input("Press Enter To End This Program")

#3. Write a program that prints the following:
#People ask me, “Why do you love Python?”
#I said, “I love Python because of its clean syntax, awesome modules, and nice OOP support”
print("People ask me, \"Why Do You Love Python? \n" "I said \"I love Python because of its clean syntax, awesome modules, and nice OOP support\"" )

#4. Write a program to show me how you can right-adjust the output of the following 3 statements
#right-adjusted
#Hint: Use the string modulo operator % or rjust() method
#I love Python. Do you?
#I do. Why do you love Python?
#Python is a forgiving language. 
message1 = "I love Python. Do you?"
message2 = "I do. Why do you love Python?"
message3 = "Python is a forgiving language."

print(message1.rjust(170))
print(message2.rjust(170))
print(message3.rjust(170))
