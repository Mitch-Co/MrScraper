import os
import sys
import csv
# Import time. All of it.
import time
import threading

# List of download names to force download when run
manualDownload = []

# Global variables
channelPath = "./DownloadList.csv"
ytdlpPath = "./yt-dlp.exe"
archiveFilename = "record.txt"
storagePath = "./"
maxParallel = 1

# Stop spinning threads after exitAfter seconds
autoAborter = False
exitAfter = 10 * 3600
startTime = time.time()

# Can use cookies from browser
useBrowserCookies = False
browserName = "firefox"

# Global video cap - sets max height of video globally
globalVideoCapFlag = False
globalVideoCap = 1080

# Safe mode settings
safeMode = False
safeStopEvery = 1
safeStopTime = 1


downloadQueue = []

def abort(errorMsg):
    print(errorMsg)
    sys.exit(1)


# Add download tasks to queue
with open(channelPath, newline ='') as toDownload:
    reader = csv.DictReader(toDownload)
    try:
        for row in reader:
            row["name"] = row["name"].strip()
            if (("url" not in row)):
                raise AttributeError
            if(row["blockupdate"].lower() != "true"):
                downloadQueue.append(row)
    except Exception as e:
        abort("Hey dingus the CSV file is messed up" + str(e))


# Yeah, I define functions right before I need them... 
# Sue me
def downloadToFolder(name, urlToDownload, audioonly = "", videolimiter= "", extraargs = ""):
    
    addSlash = ""
    if(storagePath[-1] != "/"):
        addSlash = "/"

    downloadFolder = (storagePath + addSlash +name).strip()

    audioFlag = False
    if(audioonly.lower() == "true"):
        audioFlag = True

    videoLimiterString = ""
    
    if (videolimiter != ""):
        try:
            temp = int(videolimiter)
            
            if(globalVideoCapFlag == True and globalVideoCap > temp):
                temp = globalVideoCap   
    
            videoLimiterString = '[height<=?' + str(temp) +']'
        
        except Exception as e:
            pass


    if(not os.path.exists(downloadFolder)):
        os.makedirs(downloadFolder)

    # Form YT-DLP Command
    # All commands have space at the end of them
    dlpCommand = ""
    
    # I should be using some sort of stringbuilder to not add strings together like this
    # Sue me
    if(audioFlag):
        dlpCommand += '-o "' + downloadFolder + '/%(title)s [%(id)s].%(ext)s" '
        dlpCommand += '--extract-audio --audio-format mp3 '
    else:
        dlpCommand += '-o "' + downloadFolder + '/%(title)s [%(id)s]" '
        dlpCommand += '-f "bestvideo' + videoLimiterString + '+bestaudio'
        if(videoLimiterString != ""):
            dlpCommand += '/bestvideo+bestaudio'
        dlpCommand += '" '
        
    dlpCommand += '--download-archive "' + (downloadFolder + "/" + archiveFilename) +  '" '
    dlpCommand += '--no-overwrites '
    if(useBrowserCookies):
        dlpCommand += '--cookies-from-browser ' + browserName.lower() + ' '
    dlpCommand += extraargs + ' '
    dlpCommand += urlToDownload

    print("----------- DOWNLOADING -----------\n" + "Folder Name: " + name + "\n" + "URL: " + urlToDownload + "\n" + "Audio Only: " + str(audioFlag) + "\n" + "Max Video Height: " + videoLimiterString + "\n"  + "Extra Args: " + extraargs + "\n" + "Full Command: yt-dlp.exe " + dlpCommand + "\n\n")

    os.system("start /wait cmd /MIN /c yt-dlp.exe " + dlpCommand)

safeModeCount = 0
while len(downloadQueue) > 0:
    if(autoAborter and ((time.time() - startTime) > exitAfter)):
        break

    if(threading.active_count() - 1 >= maxParallel):
        time.sleep(0.3)
        continue
    threading.Thread(target=downloadToFolder, args=(downloadQueue[-1]["name"], downloadQueue[-1]["url"], downloadQueue[-1]["audioonly"], downloadQueue[-1]["videolimiter"], downloadQueue[-1]["extraargs"])).start()
    downloadQueue.pop()
    

    if(safeMode):
        safeModeCount += 1

    if(safeMode and safeModeCount >= safeStopEvery):
        safeModeCount = 0
        time.sleep(safeStopTime)


# Wait for all threads to stop (not too sure if nessisary?)
while (threading.active_count() > 1):
    time.sleep(0.3)