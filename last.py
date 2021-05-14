import pylast
from pypresence import Presence
import time
import variables as var

network = pylast.LastFMNetwork(api_key=var.key, api_secret=var.secret)
user = network.get_user(var.username)
RPC = Presence("748506372215275640")
RPC.connect()
t = False

def getInfo(track):
    artist = network.get_artist(track.artist)

    if not(artist):
        return "unknown genre"

    if "acoustic" in track.title.lower():
        genren = "acoustic"

    else:
        try:    
            genre = artist.get_top_tags()
        except:
            return "unknown genre"

        if genre:
            genren1 = ""
            genren2 = ""
            flag = True
            i = 0
            i2 = 0
            flag2 = False

            while flag:
                while genren1 in genren2:
                    genren1 = genre[i]
                    if genre[-1] == genre[i]:
                        genren1 = genre[0].item.get_name().lower()
                        flag = True
                        break
                    else:
                        genren1 = genre[i].item.get_name().lower()
                        flag = False
                    i += 1
                    print("genre 1: " + genren1)
    
                if flag:
                    flag = False
                    flag2 = True

                while genren2 in genren1:
                    genren2 = genre[i]
                    if genre[-1] == genre[i]:
                        genren2 = genre[0].item.get_name().lower()
                        flag = True
                        break
                    else:
                        genren2 = genre[i].item.get_name().lower()
                        flag = False
                    i += 1
                    print("genre 2: " + genren2)

                if not(flag) and not(flag2):
                    flag = True
                    flag2 = False

            genren = genren1 + ", " + genren2

        else:
            genren = "unknown genre"

    return genren

def playing(t):
    d = 60
    try:
        current_track = user.get_now_playing()
    except:
        print ("Error getting info from last.fm")
        return 5,False

    if current_track:
        try:
            d = current_track.get_duration()
        except:
            d = 60000

        try:
            album = current_track.get_album()
            album_title = "Album: "  + album.title
        except:
            album_title = "Unknown album"

        d = d / 1000
        track = str(current_track)
        print ("Playing: " + track)
        genre = getInfo(current_track)
            
        if current_track != t:
            try:
                RPC.update(state= "by " + str(current_track.artist)[:125] + "  ", details= str(current_track.title)[:125] + "  ", small_image= "small", large_text= album_title[:121], small_text= genre, large_image= "large", start= time.mktime(time.localtime()))
            except:
                print ("Discord error")
                return d, current_track
            t = current_track
        elif d and d != 60:
            time.sleep(10)
            return playing(t)

        if not(d):
            d = 60
    else:
        print ("Nothing playing on last.fm")
        if t:
            genre = getInfo(t)
            try:
                RPC.update(state= "by " + str(t.artist)[:125] + "  ", details= str(t.title)[:125] + "  ", large_image= "pause", large_text= "Paused")
                t = False
            except:
                print("Discord error")
        return d,t
    print(d)
    return d,t

while True:
    d,t = playing(t)
    time.sleep(d)
