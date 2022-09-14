# MrScraper
 A simple manager for yt-dlp. 
 
# Prerequisites
 - Make sure you download the latest yt-dlp exe release and put it in the same folder as MrScraper.py
 - Make sure to download and install the latest version of python if you do not have it already.
 
# Setup
 Put channels or videos in the DownloadList.csf file, and run MrScraper using the `python MrScraper.py` command in powershell or CMD
 
 Entries in the CSV file represent:

  name,audioonly,blockupdate,extraargs,url

  - name is the channel or playlist name
  - audioonly can be TRUE or FALSE: If TRUE, this converts the channel/playlist to a audio format
  - blockupdate can be TRUE or FALSE: If TRUE, this blocks the channel/playlist from updating
  - extraargs should be left blank, but can theoritically be used to append extra commands to the download
  - url is the URL of the channel/playlist

  The format of the entries in the csv file should thus be as follows:
  <File / Channel Name>,<TRUE/FALSE>,<TRUE/FALSE>,"<ARGS APPENDED TO DL COMMAND, CAN BE BLANK>",<URL OF CHANNEL/ PLAYLIST>
