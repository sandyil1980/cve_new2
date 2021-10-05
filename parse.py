import csv
import pandas as pd
import shutil
import baseLoader

def parse():
    filename = 'vullist.csv'
    fieldnames = ['Name', 'Status', 'Description', 'References', 'Phase', 'Votes', 'Comments']
    file_reader = csv.DictReader(filename, fieldnames=fieldnames)

    with open(filename) as fr, open("new.csv", "w", newline='') as fw:
        cr = csv.reader(fr)
        cw = csv.writer(fw)
        cw.writerow(['Name', 'Status', 'Description', 'References', 'Phase', 'Votes', 'Comments'])
        cw.writerows(cr)

