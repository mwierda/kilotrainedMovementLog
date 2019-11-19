"""
wierda.mckenzie

Using:
https://github.com/burnash/gspread

"""

import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

class competitorSpreadsheet:
    
    def __init__(self):
        self.scope = ['https://spreadsheets.google.com/feeds']
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json',scope)
        self.docID = "1-jmN0QV27PLUrqbsLp7M9FeYupNLE-Nu7UGNzJ0KWaI"
        self.client = gspread.authorize(credentials)

    def getKilotrainedWeek(self, weekIndexToGet=0):
        # get the week of training @index weekIndexToGet
        competitorSpreadsheet = self.client.open_by_key(docID)
        currentWeekWS = competitorSpreadsheet.get_worksheet(weekIndexToGet)
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
    addMovementResponse = input("Do you want to add a movement to the list? y or n\n")
    if addMovementResponse == 'y':
        movementName = input("Please enter the name of the movement you'd like to add:\n")
        newMovement = Movement(movementName)
        print(newMovement.getName())
    currWeekWS = getKilotrainedCurrentWeek()
    liftingMovements = []
    for row in range(1,48):
        liftingMovements.append(currWeekWS.cell(row,1).value)
    for cellValue in liftingMovements:
        if cellValue == "":
            liftingMovements.remove(cellValue)
    print(liftingMovements)
    # print(currWeek.acell("B2").value) # works!
    #saveMovementToCSV("deadlift")
    movementList = getCurrentMovementList()
    print(movementList)

if __name__=='__main__':
    main()
