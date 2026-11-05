contacts=[ {"name": "swati", "company": "  MoEngage", "channel": "LinkedIn", "status": "sent"},
    {"name": "Alice", "company": "Spotdraft", "channel": "Linkedin", "status": "sent"},]
contacts.extend([{"name": "Amrita", "company": "  Credera", "channel": "LinkedIn", "status": "Yet to message"},
              {"name": "Akshay", "company": "Deloitte", "channel": "LinkedIn", "status": "Yet to message"}])

#print(contacts)
for contact in contacts:
    print(f"{contact['name']} | {contact['company']} | { contact['channel']} | {contact['status']}")
    if contact['name']=='Amrita':
        contact['status']='Rejected'

#print(contacts)
print(f"number of contacts = {len(contacts)}")

for contact in contacts:
    contact['company']=contact['company'].upper().strip()

print(contacts)

for contact in contacts:
    if(contact['status']!='Rejected'):
        print(f"appln sent to {contact['company']}")
    else:
        print(f"status of {contact['company']} is {contact['status']}")

statusDict={}
for contact in contacts:
    status=contact['status']
    statusDict[status]=statusDict.get(status,0)+1

print(f"status dictionary = {statusDict}")
   
statusTuple=[]
for contact in contacts:
    statusTuple.append(contact['status'])

statusTuple=tuple(statusTuple)
print(f"status tuple {statusTuple}")

follow_up_date=input("Please enter follow up date :")
for contact in contacts:
   contact['follow_up_date']= follow_up_date

print(f" contacts list {contacts}")

import csv
headers= contacts[0].keys()
with open('interviewsList.csv','w',newline="",encoding='utf-8') as file:
    writer=csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(contacts)