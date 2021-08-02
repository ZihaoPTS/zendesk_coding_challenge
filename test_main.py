from functions import *

def test_GetCredential():
    credential = GetCredential()
    assert 'email' in credential
    assert 'api_token' in credential

def test_GetAllTickets():
    #Test getting ticket via API
    credential = GetCredential()
    AllTickets = GetAllTickets(credential['email'],credential['api_token'])
    assert len(AllTickets) > 0 
    assert 'url' in AllTickets[0]
    assert 'id' in AllTickets[0]
    assert 'status' in AllTickets[0]
    assert 'priority' in AllTickets[0]
    assert 'subject' in AllTickets[0]
    assert 'description' in AllTickets[0]
    assert 'organization_id' in AllTickets[0]
    assert 'via' in AllTickets[0]
    assert 'custom_fields' in AllTickets[0]
    assert 'requester_id' in AllTickets[0]
    assert 'created_at' in AllTickets[0]
    assert 'updated_at' in AllTickets[0]
    apifault = GetAllTickets('','')
    #making sure function return None when status code is not 200
    assert apifault == None

def test_Get25Tickets():
    #confriming Get25Tickets working in different corner cases
    AllTickets = []
    for x in range(107):
        AllTickets.append(x)
    tickets_idx_1 = Get25Tickets(1,AllTickets)
    tickets_idx_4 = Get25Tickets(4,AllTickets)
    assert tickets_idx_1 == AllTickets[25:50]
    assert tickets_idx_4 == AllTickets[100:107]
    #test for less then 25 tickets
    sometickets = []
    for x in range(13):
        AllTickets.append(x)
    st = Get25Tickets(0,sometickets)
    assert st == sometickets


def test_GetTicketsPrintout():
    credential = GetCredential()
    AllTickets = GetAllTickets(credential['email'],credential['api_token'])
    t_0_25 = Get25Tickets(0,AllTickets)
    t_printout = GetTicketsPrintout(t_0_25)
    assert 'id' in t_printout[0]
    assert len(t_printout[0]) == len(t_printout[1])

def test_paging():
    empty_list = ['']*101
    pg = paging(empty_list,25) #should have 5 page
    pg.next()
    assert pg.current_page == 1
    for x in range(7): #run next page 6 time
        pg.next()
    assert pg.current_page == 4
    pg.previous()
    assert pg.current_page == 3
    for x in range(7): #run next page 6 time
        pg.previous()
    assert pg.current_page == 0
    
