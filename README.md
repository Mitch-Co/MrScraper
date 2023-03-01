# MrScraper
 A simple manager for yt-dlp. 
 
# Prerequisites
 - Make sure you download the latest yt-dlp exe release and put it in the same folder as MrScraper.py
 - Make sure to download and install the latest version of python if you do not have it already.
 
# Setup
 Put channels or videos in the DownloadList.csf file, and run MrScraper using the `python MrScraper.py` command in powershell or CMD
 
 Entries in the CSV file represent:

  name,audioonly,blockupdate,videolimiter,extraargs,url

  - name is the channel or playlist name
  - audioonly can be TRUE or FALSE: If TRUE, this converts the channel/playlist to a audio format
  - blockupdate can be TRUE or FALSE: If TRUE, this blocks the channel/playlist from updating
  - videolimiter limits the videos downloaded by the current channel/playlist to a maximum pixel height
  - extraargs should be left blank, but can theoritically be used to append extra commands to the download
  - url is the URL of the channel/playlist

# Examples
  The format of the entries in the csv file should thus be as follows:
  `<File / Channel Name>,<TRUE/FALSE/BLANK>,<TRUE/FALSE/BLANK>,<Integer/BLANK>, "<ARGS APPENDED TO DL COMMAND/BLANK>",<URL OF CHANNEL/ PLAYLIST>`
  
  Some examples of CSV entries include:
  `Captain Disillusion,,,,,https://www.youtube.com/user/captaindisillusion`
  `How to Drink,,TRUE,,1080,https://www.youtube.com/c/howtodrink`
  `valoulette,TRUE,,,,https://www.youtube.com/c/valouletteasmr`

   Do note that the headers in the CSV file included that indicate the field name are nessisary. It is reccomended that you edit the included template file to start.
  
	
	
  
