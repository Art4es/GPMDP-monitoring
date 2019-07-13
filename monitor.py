from pathlib import Path
import json
import time

# Edit this IF you have NOT DEFAULT path, where gpmdp stores song information
file_location = str(Path.home()) + "\\AppData\\Roaming\\Google Play Music Desktop Player\\json_store\\playback.json"

# EDIT THIS ANYWAY
obs_file_location = 'C:\\Users\\Art4es\\Desktop\\obs\\songname.txt'

song_name = ""

# Edit if you want (update period)
timeToSleep = 7


def write_to_file(location, song):
    o_file = open(location, 'w')
    o_file.write(song)
    o_file.close()
    print(song)


while True:
    i_file = open(file_location, 'r')
    decoded = json.loads(i_file.read())
    i_file.close()

    new_song_name = "Playing in silence"
    if decoded['playing']:
        new_song_name = decoded['song']['artist'] + " - " + decoded['song']['title'] + '      '

    if song_name != new_song_name:
        song_name = new_song_name
        write_to_file(obs_file_location, song_name)

    time.sleep(timeToSleep)
