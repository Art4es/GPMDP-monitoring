import json
import time

file_location = "C:\\Users\\Art4es\\AppData\\Roaming\\Google Play Music Desktop Player\\json_store\\playback.json"
obs_file_location = 'C:\\Users\\Art4es\\Desktop\\obs\\songname.txt'
song_name = ""
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
        new_song_name = decoded['song']['artist'] + " - " + decoded['song']['title']

    if song_name != new_song_name:
        song_name = new_song_name
        write_to_file(obs_file_location, song_name)

    time.sleep(timeToSleep)
