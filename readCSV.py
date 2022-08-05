# -*- coding: utf-8 -*-

import csv

def getCSV(fileName, column):
    with open(fileName, "r") as csvfile:
        reader = csv.reader(csvfile)
        content = [row[column] for row in reader]

    return content
    