import csv
from collections import Counter
import json
import requests
from dataclasses import dataclass
import html
import re


contacts=[ {"name": "swati", "company": "  MoEngage", "channel": "LinkedIn", "status": "Sent"},
           {"name": "Alice", "company": "Spotdraft", "channel": "LinkedIn", "status": "Sent"},]

def add_contacts(contacts):
     contacts.extend([{"name": "Amrita", "company": "  Credera", "channel": "LinkedIn", "status": "Yet to message"},
              {"name": "Akshay", "company": "Deloitte", "channel": "LinkedIn", "status": "Yet to message"}])
     for contact in contacts:
         contact['company'].upper().strip();



def show_contacts(contacts):
    for contact in contacts:
        print(f"{contact['name']} | {contact['company']} | { contact['channel']} | {contact['status']}")


def showcontacts_length(contacts):
    print(f"number of contacts = {len(contacts)}")

def set_status(contact,status):
    contact.status=status
    

def show_status(contact):
    for contact in contacts:
        print(f"status of {contact['company']} is {contact['status']} ")

def status_count(contacts)->dict:
    status_dict=Counter(contact['status'] for contact in contacts)
    return status_dict

allowed_status=('Sent', 'Yet to message', 'Rejected', 'In Progress')

def add_field(contacts:list):
    for contact in contacts:
        contact['follow_up_date']=input('Enter Follow up date')

def contacts_csv(contacts):
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
    show_status(contacts)
    status_count(contacts)
    add_field(contacts)
    contacts_csv(contacts)
    contacts_tojson(contacts)


