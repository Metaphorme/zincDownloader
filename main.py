# -*- coding: utf-8 -*-

# -------------------- IMPORTENT SETTINGS --------------------

# Please write the CSV filename and the column contains ZINC Title here
CSVfilename = "B_D_SP.csv"
column = 1
# DownloadType, For example, "SMILES", "SDF", "CSV", "XML", "JSON"
downloadType = "SDF"
# GetDownloadListOnly, if GetDownloadListOnly is True, output downloadList.txt only,
# then you could download on remote or download with other tools like aria2.
GetDownloadListOnly = False
# The number of threads to download. PLEASE DON'T SET HIGER THAN 5!!!
downloadThread = 3

# -----------------------  Finish Line -----------------------

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
print(f'\tcolumn                  -->     {column}')
print(f'\tdownloadType            -->     {downloadType}')
print(f'\tGetDownloadListOnly     -->     {GetDownloadListOnly}')
print(f'\tdownloadThread          -->     {downloadThread}')
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

ZINCS = readCSV.getCSV(fileName=CSVfilename, column=column)

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
if downloadType == "SMILES":
    downloadType = "smi"
elif downloadType == "SDF":
    downloadType = "sdf"
elif downloadType == "CSV":
    downloadType = "csv"
elif downloadType == "XML":
    downloadType = "xml"
elif downloadType == "JSON":
    downloadType = "json"
else:
    print("Error: downloadType Not in case")
    exit()

# Generate url List
if GetDownloadListOnly == True:
    with open("downloadList.txt", "w") as f:
        for z in ZINCS:
            f.write("https://zinc.docking.org/substances/" + z + "." + downloadType + "\n")
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
            o = download.download(url="https://zinc.docking.org/substances/" + z + "." + downloadType  \
                , outputName="output/" + z + "." + downloadType)

            if o[1] != "":
                ZINCS.add(z)
                print(z + " download failed, Try again later")
            else:
                print(z + " Download Finished\t" + "[ZINCS Remain: " + str(len(ZINCS)) +"]")


        global download_thread_num
        download_thread_num -= 1

# Start Thread
download_thread_num = 0
for i in range(downloadThread):
    Downloader().start()
    download_thread_num += 1

# wait thread done
while download_thread_num:
    pass

print("All " + Jobnums + " Jobs Finished")
