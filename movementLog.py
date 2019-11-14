"""
wierda.mckenzie

Use for help:
https://gspread.readthedocs.io/en/latest/oauth2.html
https://github.com/burnash/gspread # this one has the basics
"""

import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def getKilotrainedCurrentWeek():
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json',scope)
    #docName = "Competitor"
    docID = "1-jmN0QV27PLUrqbsLp7M9FeYupNLE-Nu7UGNzJ0KWaI"

    client = gspread.authorize(credentials)
    competitorSpreadsheet = client.open_by_key(docID)
    currentWeekWS = competitorSpreadsheet.get_worksheet(0)
    # # these should work
    # valA1 = currentWeekWS.acell("B2").value
    # row1 = currentWeekWS.row_values(1)
    # print(valA1)
    # print(row1)
    # # this stopped working for some reason; idk why
    # for row in range(1,10):
    #     print(currentWeekWS.row_values(row))
    return currentWeekWS

def saveMovementToCSV(movement):
    with open("movementList.csv", 'a', newline='') as movementRowsCSV:
        csvWriter = csv.writer(movementListCSV)
        csvWriter.writerow([movement])

def getCurrentMovementList():
    movementList = []
    with open("movementList.csv", 'r', newline='') as movementRowsCSV:
        csvReader = csv.reader(movementRowsCSV)
        for row in csvReader:
            movementList += row
    return movementList

class Movement:
    def __init__(self, name, sets = None, reps = None):
        self.name = name
        self.sets = sets
        self.reps = reps

    def getName(self):
        return self.name # return string name of Movement

def main():
    backSquat = Movement('Back Squat')
    print(backSquat.getName())
    currWeek = getKilotrainedCurrentWeek()
    # print(currWeek.acell("B2").value) # works!
    #saveMovementToCSV("deadlift")
    movementList = getCurrentMovementList()
    print(movementList)

if __name__=='__main__':
    main()
