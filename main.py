# -*- coding: utf-8 -*-

# ------------------------------ IMPORTENT--SETTINGS ------------------------------

# Please specify the CSV filename and the column that contains ZINC Title here.
CSVfilename = "B_D_SP.csv"
Column = 1
# DownloadType, selectable from "SMILES", "SDF", "CSV", "XML", "JSON".
DownloadType = "SDF"
# If GetDownloadListOnly is set to True, this tool will only generate the 
# downloadList.txt, then you can download on remote or with other tools like aria2.
GetDownloadListOnly = False
# The number of threads to download. PLEASE DON'T SET TO HIGER THAN 5!!!
DownloadThread = 3

# --------------------------------- FINISH---LINE ---------------------------------

print("")
print("")
print("       .__              ________                      .__                    .___            ")
print("_______|__| ____   ____ \______ \   ______  _  ______ |  |   _________     __| _/___________ ")
print("\___   /  |/    \_/ ___\ |    |  \ /  _ \ \/ \/ /    \|  |  /  _ \__  \   / __ |/ __ \_  __ \\")
print(" /    /|  |   |  \  \___ |    `   (  <_> )     /   |  \  |_(  <_> ) __ \_/ /_/ \  ___/|  | \\/")
print("/_____ \__|___|  /\___  >_______  /\____/ \/\_/|___|  /____/\____(____  /\____ |\___  >__|   ")
print("      \/       \/     \/        \/                  \/                \/      \/    \/       ")

print("")
print("")
print("")
print("{:^95}".format("zincDownloader, An easy multithreaded zinc database downloader."))
print("{:^95}".format("Thanks: ZINC, zinc.docking.org, provided by UCSF"))
print("{:^95}".format("Author: Metaphorme, github.com/Metaphorme, in CPU"))
print("{:^95}".format("Licensed under the MIT License"))
print("")
print("{:-^95}".format(""))
print("")
print("{:<95}".format("These are the settings, please make sure they are right."))
print("")
print(f'\tCSVfilename             -->     {CSVfilename}')
print(f'\tColumn                  -->     {Column}')
print(f'\tDownloadType            -->     {DownloadType}')
print(f'\tGetDownloadListOnly     -->     {GetDownloadListOnly}')
print(f'\tDownloadThread          -->     {DownloadThread}')
print("")
print("{: <95}".format("You could change these Settings manually in main.py"))
print("{: <95}".format("The program will be activated in 5 seconds."))
print("")
print("{:-^95}".format(""))
print("")

import threading
import download
import readCSV
import time

time.sleep(5)

ZINCS = readCSV.getCSV(fileName=CSVfilename, column=Column)

# Remove duplication
ZINCS = set(ZINCS)
Jobnums = str(len(ZINCS))
print("Find " + Jobnums + " Jobs to do.")

# Wipe off illegal ZINC Title
for z in ZINCS.copy():
    if z[:4] == "ZINC":
        continue
    else:
        ZINCS.remove(z)

# Determine file type
typePool = {
    "SMILES" : "smi",
    "SDF"    : "sdf",
    "CSV"    : "csv",
    "XML"    : "xml",
    "JSON"   : "json"
}

DownloadType = typePool.get(DownloadType)
if DownloadType == None:
    print("Error: DownloadType Not in case")
    exit()

# Generate url List
if GetDownloadListOnly == True:
    with open("downloadList.txt", "w") as f:
        for z in ZINCS:
            f.write("https://zinc.docking.org/substances/" + z + "." + DownloadType + "\n")
    print("Written Finished")
    exit()

print("Begin to Download")
# Thread to downloads
class Downloader(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while len(ZINCS):
            z = ZINCS.pop()
            o = download.download(url="https://zinc.docking.org/substances/" + z + "." + DownloadType  \
                , outputName="output/" + z + "." + DownloadType)

            if o[1] != "":
                ZINCS.add(z)
                print(z + " download failed, Try again later")
            else:
                print(z + " Download Finished\t" + "[ZINCS Remain: " + str(len(ZINCS)) +"]")


        global download_thread_num
        download_thread_num -= 1

# Start Thread
download_thread_num = 0
for i in range(DownloadThread):
    Downloader().start()
    download_thread_num += 1

# wait thread done
while download_thread_num:
    pass

print("All " + Jobnums + " Jobs Finished")
