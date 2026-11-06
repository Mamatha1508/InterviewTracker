import requests
import json
from dataclasses import dataclass
import html
import re


def fetch_jobs(search)->dict:
    try:
        data= requests.get(search)
        data1= data.json()["jobs"]
        with open("jobs.json","w",encoding='utf-8') as file:
            json.dump(data1,file,indent=4)
        return data1
    except requests.exceptions.HTTPError:
        print(f"error has occured")

            
jsondatareturned=fetch_jobs('https://remotive.com/api/remote-jobs')
#print(f'returnd data {jsondatareturned}')
# dataclass
@dataclass
class Job:
    title:str
    company:str
    url:str
    location : str
    description: str

def parseJob(raw:dict)-> Job:
    return Job(
        title= raw['title'],
        company=raw['company_name'],
            url= raw['url'],
            location=raw['candidate_required_location'],
            description=raw['description'])
dictreturnrd=parseJob(jsondatareturned[0])
dictreturnrd.description= html.unescape(dictreturnrd.description)
dictreturnrd.description=re.sub(r"<[^>]+>","",dictreturnrd.description)
dictreturnrd.description=re.sub(r"\\n", "\n",dictreturnrd.description)
                                

print(dictreturnrd)