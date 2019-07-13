import json
import time

fileLocation = "C:\\Users\\Art4es\\AppData\\Roaming\\Google Play Music Desktop Player\\json_store\\playback.json"
obsFileLocation = 'C:\\Users\\Art4es\\Desktop\\obs'
songName = ""
timeToSleep = 7

while True:
    iFile = open(fileLocation, 'r')
    decoded = json.loads(iFile.read())
    iFile.close()
    newSongName = decoded['song']['artist'] + " - " + decoded['song']['title']
    if songName != newSongName:
        songName = newSongName
        oFile = open(obsFileLocation + '\\songname.txt', 'w')
        oFile.write(songName)
        oFile.close()
        print(songName)
    time.sleep(timeToSleep)
