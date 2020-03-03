#!/usr/bin/env python3

# This is a very sophisticated program for printing messages to the terminal.
#
# Written by ewk

print("This is a very sophisticated program.")
print("It writes messages to the screen!")
print("")

# Ask user for message to print
while True:
    msg = input("Enter your message: ")
    if msg == 'quit':
        print "Bye bye!"
        break
    else:
        print(msg)
