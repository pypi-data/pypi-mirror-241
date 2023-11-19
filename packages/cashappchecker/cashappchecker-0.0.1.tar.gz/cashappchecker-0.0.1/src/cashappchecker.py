import requests
import json
import re

def amount(id):
    i = requests.get(f"https://cash.app/receipt-json/f/{id}")
    amt = i.json()["detail_rows"][0]["value"]
    return amt

def note(id):
    i = requests.get(f"https://cash.app/receipt-json/f/{id}")
    note = i.json()["threaded_title"]
    return note

def cashtag(id):
    i = requests.get(f"https://cash.app/receipt-json/f/{id}")
    cashtag = None
    cashtag_match = re.search(r"Payment to ([^/]+)", i.json()["header_subtext"])
    if cashtag_match:
        cashtag = cashtag_match.group(1)
    return cashtag

v = False
idd = None

def id(l):
    global idd
    match = re.search(r"/payments/([^/]+)/receipt", l)
    if match:
        idd = match.group(1)
        return idd
    else:
        global v
        v = False
        print("Link is invalid... aborting")
