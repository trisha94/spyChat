# importing select friend and spy details (friend details here from spy details)
from select_friend import select_friend
from spy_details import friends

#importing termcolor for colorful output.
from termcolor import colored

# function to read chat history
def read_chat_history():
    read_chat = select_friend()

    print '\n'

    for chat in friends[read_chat].chats:
        # message is sent by me
        if (chat.sent_by_me != False) :
            # the date and time with yellow color
            print (colored(str(chat.time.strftime("%d %B %Y %A %H:%M"))+ ", ", 'yellow')),
            # the message is printed in red
            print (colored("You said: ", 'red')),
            # default color black for text
            print str(chat.message)
        # message is sent by another spy
        else:
            # the date and time with yellow color
            print (colored(str(chat.time.strftime("%d %B %Y %A %H:%M"))+ ", ", 'yellow')),
            # the message is printed in red
            print (colored(str(friends[read_chat].name)+"You said: ", 'red')),
            # default color black for text
            print str(chat.message)