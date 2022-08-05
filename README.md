# zincDownloader
An easy multithreaded zinc database downloader.

## Usage
1. Get zincDownloader  

```bash
  $ git clone https://github.com/Metaphorme/zincDownloader.git
```

2. Install the requirements
```bash
  $ cd zincDownloader
  $ pip3 install -r requirements.txt
```

3. Remove Examples
  B_D_SP.csv, output/*.sdf, downloadList.txt are examples for you to know how to use it.
  Remove them if already proficiency in using.
```bash
  $ rm -rf output/*.sdf downloadList.txt
```

4. Edit the settings
  Please edit main.py
```python
# -------------------- IMPORTENT SETTINGS --------------------

# Please write the CSV filename and the column contains ZINC Title here
CSVfilename = "B_D_SP.csv"
Column = 1
# DownloadType, For example, "SMILES", "SDF", "CSV", "XML", "JSON"
DownloadType = "SDF"
# GetDownloadListOnly, if GetDownloadListOnly is True, output downloadList.txt only,
# then you could download on remote or download with other tools like aria2.
GetDownloadListOnly = False
# The number of threads to download. PLEASE DON'T SET HIGER THAN 5!!!
DownloadThread = 3

# -----------------------  Finish Line -----------------------
```

5. Run
```bash
  $ python3 main.py
```

## Credits
zincDownloader, An easy multithreaded zinc database downloader.  
Thanks: [ZINC](https://zinc.docking.org/), zinc.docking.org, provided by [UCSF](https://pharmchem.ucsf.edu/).  
Author: [Metaphorme](https://blog.metaphorme.net/), github.com/Metaphorme, in [CPU](https://www.cpu.edu.cn/).  
Licensed under the MIT License.  
