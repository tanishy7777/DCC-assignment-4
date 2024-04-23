import fitz
from pprint import pprint
import csv

doc = fitz.open("political_party.pdf") # open document

isPage0 = True

for i in range(len(doc)):
    page = doc[i] # get the 1st page of the document
    tabs = page.find_tables() # locate and extract any tables on page
    print(f"{len(tabs.tables)} found on {page}") # display number of found tables

    if tabs.tables:  
        tab0 = tabs[0].extract()
        print(tab0)
        political_csv = open('political_csv',"a+")
        political_writer = csv.writer(political_csv)

        if isPage0:
            political_writer.writerows(tab0)
        else:
            political_writer.writerows(tab0[1:])

    isPage0 = False


doc1 = fitz.open("companies.pdf") # open document

isPage0 = True

for i in range(len(doc1)):
    page = doc1[i] # get the 1st page of the document
    tabs = page.find_tables() # locate and extract any tables on page
    print(f"{len(tabs.tables)} found on {page}") # display number of found tables

    if tabs.tables:  
        tab0 = tabs[0].extract()
        print(tab0)
        companies_csv = open('companies_csv',"a+")
        companies_writer = csv.writer(companies_csv)

        if isPage0:
            companies_writer.writerows(tab0)
        else:
            companies_writer.writerows(tab0[1:])

    isPage0 = False