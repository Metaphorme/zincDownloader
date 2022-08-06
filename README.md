# zincDownloader  
An easy multithreaded zinc database downloader.

## Usage
1. Get zincDownloader  
    ```bash
    git clone https://github.com/Metaphorme/zincDownloader.git
    ```

2. Install dependencies  
    ```bash
    cd zincDownloader
    pip3 install -r requirements.txt
    ```

3. Remove examples  
    `B_D_SP.csv, output/*.sdf`, `downloadList.txt` are examples for demonstration.  
    Remove them if you are already proficient with this tool.
    ```bash
    rm -f output/*.sdf downloadList.txt
    ```

4. Edit the settings  
    Please edit main.py
    ```python
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
    ```

5. Run  
    ```bash
    python3 main.py
    ```

## Credits
```
       .__              ________                      .__                    .___            
_______|__| ____   ____ \______ \   ______  _  ______ |  |   _________     __| _/___________  
\___   /  |/    \_/ ___\ |    |  \ /  _ \ \/ \/ /    \|  |  /  _ \__  \   / __ |/ __ \_  __ \  
 /    /|  |   |  \  \___ |    `   (  <_> )     /   |  \  |_(  <_> ) __ \_/ /_/ \  ___/|  | \\  
/_____ \__|___|  /\___  >_______  /\____/ \/\_/|___|  /____/\____(____  /\____ |\___  >__|  
      \/       \/     \/        \/                  \/                \/      \/    \/   
```
zincDownloader, An easy multithreaded zinc database downloader.  
Thanks: [ZINC](https://zinc.docking.org/), zinc.docking.org, provided by [UCSF](https://pharmchem.ucsf.edu/).  
Author: [Metaphorme](https://blog.metaphorme.net/), github.com/Metaphorme, in [CPU](https://www.cpu.edu.cn/).  
Licensed under the MIT License.  
