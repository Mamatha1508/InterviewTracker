import csv
from collections import Counter
import json

contacts=[ {"name": "swati", "company": "  MoEngage", "channel": "LinkedIn", "status": "Sent"},
           {"name": "Alice", "company": "Spotdraft", "channel": "LinkedIn", "status": "Sent"},]

def add_contacts(contacts):
     contacts.extend([{"name": "Amrita", "company": "  Credera", "channel": "LinkedIn", "status": "Yet to message"},
              {"name": "Akshay", "company": "Deloitte", "channel": "LinkedIn", "status": "Yet to message"}])



def show_contacts(contacts):
    for contact in contacts:
        print(f"{contact['name']} | {contact['company']} | { contact['channel']} | {contact['status']}")
        if contact['company']=='Credera':
            contact['status']='Rejected'



def showcontacts_length(contacts):
    print(f"number of contacts = {len(contacts)}")




for contact in contacts:
    contact['company']=contact['company'].upper().strip()


for contact in contacts:
    if contact['status']=='Sent':
        print(f"appln sent to {contact['company']}")
    else:
        print(f"status of {contact['company']} is {contact['status']}")

status_dict=Counter(contact['status'] for contact in contacts) 

print(f"status dictionary = {status_dict}")
   
allowed_status=('Sent', 'Yet to message')

for contact in contacts:
    follow_up_date=input("Please enter follow up date :")
    contact['follow_up_date']= follow_up_date


headers= contacts[0].keys()
with open('interviewsList.csv','w',newline="",encoding='utf-8') as file:
    writer=csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(contacts)

def contacts_tojson(contacts):
    with open("contactList.json","w",encoding="utf-8") as file:
        json.dump(contacts,file,indent=4)



if __name__== "__main__":
    add_contacts(contacts)
    show_contacts(contacts)
    showcontacts_length(contacts)
    contacts_tojson(contacts)

