import requests
import json
import os

def GetCredential():
    with open('credential.json') as json_file:
        data = json.load(json_file)
    return data
    

def GetAllTickets(email,authtoken):
    api_end_point = 'https://zcczihaozheng.zendesk.com/api/v2/tickets'
    r = requests.get(api_end_point,auth=(email+'/token',authtoken))

    if r.status_code != 200:
        print("Error connecting to API gate way.")
        print("Error message:",r.text)
        return None

    return r.json()['tickets']

def Get25Tickets(page_idx,AllTickets):
    return AllTickets[page_idx*25:page_idx*25+25]

def GetTicketsPrintout(Tickets):
    data = {'id':['id'],'subject':['subject'],'Requester':['Requester'],'created at':['created at']}

    for t in Tickets:
        data['id'].append(str(t['id']))
        data['subject'].append(str(t['subject']))
        data['Requester'].append(str(t['requester_id']))
        data['created at'].append(str(t['created_at']))
    str_len_s = []
    for key in data:
        #get the longest string len for padding purpose
        str_len_s.append(list(map(lambda x:len(x),data[key])))

    temp_str = ''
    count = 0 #used to access str_len_s
    final_printout = []
    for i in range(len(data['id'])):
        for key in data:
            #padding
            temp_str += (data[key][i] + ' '*(max(str_len_s[count]) - len(data[key][i])+5))
            count += 1
        final_printout.append(temp_str)
        temp_str = ''
        count = 0
    return final_printout

#paging system
class paging:
    def __init__(self,iteratable,display_per_page):
        self.iteratable_len = len(iteratable)
        self.current_page = 0
        self.display_per_page = display_per_page
    
    def next(self):
        if (self.current_page + 1) * self.display_per_page < self.iteratable_len:
            self.current_page += 1
        else:
            print("This is the last page, You saw this because you tried to go to next page")
    
    def previous(self):
        if self.current_page > 0:
            self.current_page -= 1
        else:
            print("This is the first page, You saw this because you tried to go to previous page")
    
    def getpage(self):
        return self.current_page

def clear():

    # for windows
    if os.name == 'nt':
        os.system('cls')
    # for linux
    else:
        os.system('clear')