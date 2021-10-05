"""
Refactored baseLoader
"""

import requests
from openpyxl import Workbook
import csv

def requrl():
    url = 'https://cve.mitre.org/data/downloads/allitems.csv'
    r = requests.get(url, stream=True, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'})
    answer = '<Response [200]>'
    if answer == str(r):
        print('CVE Mitre is available, file with information about vulnerabilities is coping.........')
        file_name = 'vullist.csv'
        with open(file_name, 'wb') as f:
            f.write(r.content)
    else:
        print("CVE Mitre is not available")



