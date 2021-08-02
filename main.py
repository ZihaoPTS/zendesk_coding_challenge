import time
from functions import *

if __name__ == '__main__':
    print('Thank you for using Ticket Reader by Zihao Zheng for Zendesk Engineering Co-op coding challenge!\n' + \
    'Please wait while the code work really really hard to retrieve all the tickets')
    credential = GetCredential()
    AllTickets = GetAllTickets(credential['email'],credential['api_token'])
    if not AllTickets:
        print("Terminating Program")
        exit()
    pg = paging(AllTickets,25)
    option = ''
    time.sleep(3)
    clear()

    def print_current_page(): #helper function, no test needed
        print('You are currently at page {}'.format(pg.getpage()))
        tickets = Get25Tickets(pg.getpage(),AllTickets)
        printout = GetTicketsPrintout(tickets)
        for l in printout:
            print(l)
    print_current_page()
    option = get_option()
    while True:
        try:
            # Convert it into integer
            option_val = int(option)
            t = list(filter(lambda ticket: ticket['id'] == option_val, AllTickets))[0]
            print('Detail of ticket [id:{}]'.format(t[id]))
            print(t.sub)
        except:
            if option == 'N' or option == 'n':
                pg.next()
            elif option == 'P' or option == 'p':
                pg.previous()
            elif option == 'Q' or option == 'q':
                break
            else:
                print('Invalid Commend, try another')
            print_current_page()
        option = get_option()