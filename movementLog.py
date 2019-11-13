"""
wierda.mckenzie

Use for help:
https://gspread.readthedocs.io/en/latest/oauth2.html
https://github.com/burnash/gspread # this one has the basics
"""

import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def downloadFile():
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json',scope)
    # docName = "Competitor"
    docID = "1-jmN0QV27PLUrqbsLp7M9FeYupNLE-Nu7UGNzJ0KWaI"

    client = gspread.authorize(credentials)
    competitorSpreadsheet = client.open_by_key(docID)

    currentWeekWS = competitorSpreadsheet.get_worksheet(0)
    for rowVal in range(1,10):
        print("current row: {}".format(rowVal))
        (currentWeekWS.row_values(rowVal))

class Movement:
    def __init__(self, name, sets = None, reps = None):
        self.name = name
        self.sets = sets
        self.reps = reps

    def getName(self):
        return self.name # return string name of Movement

def main():
    print('wtf')
    backSquat = Movement('Back Squat')
    print(backSquat.getName())
    #print(lift)
    downloadFile()

if __name__=='__main__':
    main()
