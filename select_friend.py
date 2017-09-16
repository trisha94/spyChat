# importing older friend if exist
from spy_details import friends

#from globals import friends

# importing termcolor for colorful output
from termcolor import colored

# function to select friend from friend list.
def select_friend():

    # indexing position of friend.
    counter = 1

    # to select a friend with indexing
    for friend in friends:
        print str(counter) + ". " + friend.name + "Age : " + str(friend.age)

        counter = counter + 1

    # ask user which friend he wants to select to chat with
    result = int(raw_input(colored("\nSelect from the list : ", 'magenta')))
    # result the selected friend to perform action
    return result - 1