import pytest
import json
from functions import *

def test_GetCredential():
    print("Test retrieving credential")
    credential = GetCredential()
    assert 'email' in credential
    assert 'api_token' in credential

def test_GetAllTickets():
    print("Test getting ticket via API")
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
    print("making sure function return None when status code is not 200")
    assert apifault == None

def test_Get20Tickets():
    print("confriming Get20Tickets working in different corner cases")
    AllTickets = []
    for x in range(87):
        AllTickets.append(x)
    tickets_idx_1 = Get20Tickets(1,AllTickets)
    tickets_idx_4 = Get20Tickets(4,AllTickets)
    assert tickets_idx_1 == AllTickets[20:40]
    assert tickets_idx_4 == AllTickets[80:87]

def test_GetTicketsPrintout():
    assert True