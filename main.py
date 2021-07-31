import requests
import json
from functions import *

if __name__ == '__main__':
    """
    #r = requests.get('https://zcczihaozheng.zendesk.com/api/v2/requests.json',auth=('zzh523710043@tamu.edu/token','SbFNFKKUzl14OTTQCPNGt7tGXB1JTQF7te4eMFrf'))
    # tickets
    #r = requests.get('https://zcczihaozheng.zendesk.com/api/v2/tickets',auth=('zzh523710043@tamu.edu/token','SbFNFKKUzl14OTTQCPNGt7tGXB1JTQF7te4eMFrf'))
    #with wrong credential
    #r = requests.get('https://zcczihaozheng.zendesk.com/api/v2/tickets',auth=('zzh523710043@tamu.edu/token','SbFNFKKUzl14OTTQCGXB1JTQF7te4eMFrf'))

    assert r.status_code == 200
    print(r.status_code)
    
    #out_file = open("all_requests.json", "w")
    out_file = open("all_tickets.json", "w")

    json.dump(r.json(),out_file,indent=1)
    
    array = []

    for x in range(105):
        array.append(x)

    #int_a = 0
    #while int_a < len(array)/20:
    #    print(array[int_a*20:int_a*20+20])
    #    int_a += 1

    print(array[0:20])


    at = GetAllTickets()
    t_0_20 = Get20Tickets(0,at)
    #print(t_0_20[0])

    # get max single string

    data = {'id':['id'],'subject':['subject'],'Requester':['Requester'],'created at':['created at']}

    for t in t_0_20:
        data['id'].append(str(t['id']))
        data['subject'].append(str(t['subject']))
        data['Requester'].append(str(t['requester_id']))
        data['created at'].append(str(t['created_at']))
    str_len_s = []
    for key in data:
        str_len_s.append(list(map(lambda x:len(x),data[key])))

    temp_str = ''
    count = 0 #used to access str_len_s
    final_printout = []
    for i in range(len(data['id'])):
        for key in data:
            temp_str += (data[key][i] + ' '*(max(str_len_s[count]) - len(data[key][i])+5))
            count += 1
        final_printout.append(temp_str)
        temp_str = ''
        count = 0
        
    # pad all string to max string + 5

    # conconuct all string
    """
    
    
        
    


