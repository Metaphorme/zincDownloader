# -*- coding: utf-8 -*-

import requests

headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
        }

def download(url, outputName):
    r = requests.get(url=url, headers=headers, timeout=120)
    
    try:
        with open(outputName, "wb") as outputFile:
            outputFile.write(r.content)
        return ("ok", "")
    except:
        return (r.raw.reason, url)
        