# importing spy details and start chat
from spy_details import spy
from start_chat import  start_chat

#Importing termcolor to get output colorful
from termcolor import colored

#Start greeting
print (colored("\nHello!, Bro.","blue"))
print "Let's get started!\n"

#Ask the spy to continue as default spy  or create new spy
question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N): "
existing = raw_input(colored(question,"red"))

# validating input
if (existing.upper() == "Y") :
    # user wants to continue as default user.

    # concatination of salutation and name of spy.
    spy_name = spy.salutation + " " + spy.name

    # starting chat application.
    start_chat(spy.name, spy.age, spy.rating, spy.is_online)
elif (existing.upper() == "N"):
    # user wants to continue as new user
    spy.name = raw_input("What is your name :")
    # chek spy has any input or not
    if len(spy.name) > 0:
        spy.salutation = raw_input("What should we call you ? : ")


        while True:
            try:
                spy.age = int(raw_input("Enter your age: ")) # converting users input to integer (typecasting)
                break
            except ValueError:
                print "Invalid age. Try again"

        # concatination of salutation and name of spy.
        spy.name = spy.salutation + " " + spy.name

        spy.rating = float(raw_input("What is your spy rating?")) # converting users input to float (typecasting)
        spy.is_online = True

        # starting chat application.
        start_chat(spy.name, spy.age, spy.rating, spy.is_online)
    else:
        print "Invalid name. Try again."
else:
    print "Wrong choice. Try again."