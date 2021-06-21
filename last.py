import pylast
from pypresence import Presence
import time
import variables as var

network = pylast.LastFMNetwork(api_key=var.key, api_secret=var.secret)
user = network.get_user(var.username)
RPC = Presence("748506372215275640")
RPC.connect()

genre_blacklist = ["seen live", "soundtrack", "female vocalists","nsbm","instrumental","composer","video game music","robertitus global","boner inducing"]
countries = ["afghanistan","åland islands","albania","algeria","american samoa","andorra","angola","anguilla","antarctica","antigua & barbuda","argentina","armenia","aruba","australia","austria","azerbaijan","bahamas","bahrain","bangladesh","barbados","belarus","belgium","belize","benin","bermuda","bhutan","bolivia","bosnia & herzegovina","botswana","bouvet island","brazil","british indian ocean territory","british virgin islands","brunei","bulgaria","burkina faso","burundi","cambodia","cameroon","canada","cape verde","caribbean netherlands","cayman islands","central african republic","chad","chile","china","christmas island","cocos (keeling) islands","colombia","comoros","congo - brazzaville","congo - kinshasa","cook islands","costa rica","côte d’ivoire","croatia","cuba","curaçao","cyprus","czechia","denmark","djibouti","dominica","dominican republic","ecuador","egypt","el salvador","equatorial guinea","eritrea","estonia","eswatini","ethiopia","falkland islands","faroe islands","fiji","finland","france","french guiana","french polynesia","french southern territories","gabon","gambia","georgia","germany","ghana","gibraltar","greece","greenland","grenada","guadeloupe","guam","guatemala","guernsey","guinea","guinea-bissau","guyana","haiti","heard & mcdonald islands","honduras","hong kong sar china","hungary","iceland","india","indonesia","iran","iraq","ireland","isle of man","israel","italy","jamaica","japan","jersey","jordan","kazakhstan","kenya","kiribati","kuwait","kyrgyzstan","laos","latvia","lebanon","lesotho","liberia","libya","liechtenstein","lithuania","luxembourg","macao sar china","madagascar","malawi","malaysia","maldives","mali","malta","marshall islands","martinique","mauritania","mauritius","mayotte","mexico","micronesia","moldova","monaco","mongolia","montenegro","montserrat","morocco","mozambique","myanmar (burma)","namibia","nauru","nepal","netherlands","new caledonia","new zealand","nicaragua","niger","nigeria","niue","norfolk island","north korea","north macedonia","northern mariana islands","norway","oman","pakistan","palau","palestinian territories","panama","papua new guinea","paraguay","peru","philippines","pitcairn islands","poland","portugal","puerto rico","qatar","réunion","romania","russia","rwanda","samoa","san marino","são tomé & príncipe","saudi arabia","senegal","serbia","seychelles","sierra leone","singapore","sint maarten","slovakia","slovenia","solomon islands","somalia","south africa","south georgia & south sandwich islands","south korea","south sudan","spain","sri lanka","st. barthélemy","st. helena","st. kitts & nevis","st. lucia","st. martin","st. pierre & miquelon","st. vincent & grenadines","sudan","suriname","svalbard & jan mayen","sweden","switzerland","syria","taiwan","tajikistan","tanzania","thailand","timor-leste","togo","tokelau","tonga","trinidad & tobago","tunisia","turkey","turkmenistan","turks & caicos islands","tuvalu","u.s. outlying islands","u.s. virgin islands","uganda","ukraine","united arab emirates","united kingdom","united states","uruguay","uzbekistan","vanuatu","vatican city","venezuela","vietnam","wallis & futuna","western sahara","yemen","zambia","zimbabwe"]
nationalities = ['afghan', 'albanian', 'algerian', 'american', 'andorran', 'angolan', 'antiguans', 'arabic', 'argentinean', 'armenian', 'australian', 'austrian', 'azerbaijani', 'bahamian', 'bahraini', 'bangladeshi', 'barbadian', 'barbudans', 'batswana', 'belarusian', 'belgian', 'belizean', 'beninese', 'bhutanese', 'bolivian', 'bosnian', 'brazilian', 'british', 'bruneian', 'bulgarian', 'burkinabe', 'burmese', 'burundian', 'cambodian', 'cameroonian', 'canadian', 'cape verdean', 'central african', 'chadian', 'chilean', 'chinese', 'colombian', 'comoran',  'congolese', 'costa rican', 'croatian', 'cuban', 'cypriot', 'czech', 'danish', 'djibouti', 'dominican', 'dutch', 'dutchman', 'dutchwoman', 'east timorese', 'ecuadorean', 'egyptian', 'emirian', 'equatorial guinean', 'eritrean', 'estonian', 'ethiopian', 'fijian', 'filipino', 'finnish', 'french', 'gabonese', 'gambian', 'georgian', 'german', 'ghanaian', 'greek', 'grenadian', 'guatemalan', 'guinea-bissauan', 'guinean', 'guyanese', 'haitian', 'herzegovinian', 'honduran', 'hungarian', 'i-kiribati', 'icelander', 'indian', 'indonesian', 'iranian', 'iraqi', 'irish', 'israeli', 'italian', 'ivorian', 'jamaican', 'japanese', 'jordanian', 'kazakhstani', 'kenyan', 'kittian and nevisian', 'kuwaiti', 'kyrgyz', 'laotian', 'latvian', 'lebanese', 'liberian', 'libyan', 'liechtensteiner', 'lithuanian', 'luxembourger', 'macedonian', 'malagasy', 'malawian', 'malaysian', 'maldivan', 'malian', 'maltese', 'marshallese', 'mauritanian', 'mauritian', 'mexican', 'micronesian', 'moldovan', 'monacan', 'mongolian', 'moroccan', 'mosotho', 'motswana', 'mozambican', 'namibian', 'nauruan', 'nepalese', 'netherlander', 'new zealander', 'ni-vanuatu', 'nicaraguan', 'nigerian', 'nigerien', 'north korean', 'northern irish', 'norwegian', 'omani', 'pakistani', 'palauan', 'panamanian', 'papua new guinean', 'paraguayan', 'peruvian', 'polish', 'portuguese', 'qatari', 'romanian', 'russian', 'rwandan', 'saint lucian', 'salvadoran', 'samoan', 'san marinese', 'sao tomean', 'saudi', 'scottish', 'senegalese', 'serbian', 'seychellois', 'sierra leonean', 'singaporean', 'slovakian', 'slovenian', 'solomon islander', 'somali', 'south african', 'south korean', 'spanish', 'sri lankan', 'sudanese', 'surinamer', 'swazi', 'swedish', 'swiss', 'syrian', 'taiwanese', 'tajik', 'tanzanian', 'thai', 'togolese', 'tongan', 'trinidadian or tobagonian', 'tunisian', 'turkish', 'tuvaluan', 'ugandan', 'ukrainian', 'uruguayan', 'uzbekistani', 'venezuelan', 'vietnamese', 'welsh', 'yemenite', 'zambian', 'zimbabwean']
genre_blacklist += countries + nationalities

t = False

def get_info(track):
    artist = network.get_artist(track.artist)

    if not(artist):
        return "unknown genre"

    if "acoustic" in track.title.lower():
        genren = "acoustic"
        print("Genres: acoustic")

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
            blacklist_flag = False
            while flag:
                for term in genre_blacklist:
                    if term in genren1:
                        blacklist_flag = True
                while genren1 in genren2 or blacklist_flag or genren1 in genre_blacklist:
                    genren1 = genre[i]
                    if genre[-1] == genre[i]:
                        genren1 = genre[0].item.get_name().lower()
                        flag = True
                        break
                    else:
                        genren1 = genre[i].item.get_name().lower()
                        flag = False
                    i += 1
                    blacklist_flag = False
    
                if flag:
                    flag = False
                    flag2 = True

                for term in genre_blacklist:
                    if term in genren2:
                        blacklist_flag = True
                while genren2 in genren1 or blacklist_flag or genren2 in genre_blacklist:
                    genren2 = genre[i]
                    if genre[-1] == genre[i]:
                        genren2 = genre[0].item.get_name().lower()
                        flag = True
                        break
                    else:
                        genren2 = genre[i].item.get_name().lower()
                        flag = False
                    i += 1
                    blacklist_flag = False

                if not(flag) and not(flag2):
                    flag = True
                    flag2 = False

            genren = genren1 + ", " + genren2
            print("Genres:",genren)
        else:
            genren = "unknown genre"

    return genren

def playing(t):
    d = 60
    try:
        current_track = user.get_now_playing()
    except:
        print ("Error getting info from last.fm")
        return 5,t

    if current_track:
        try:
            d = current_track.get_duration()
            d = int(d / 1000)
        except:
            d = 60

        try:
            album = current_track.get_album()
            album_title = "Album: "  + album.title
        except:
            album_title = "Unknown album"

        track = str(current_track)
        print ("Currently playing:", track)
        genre = get_info(current_track)
            
        if current_track != t:
            try:
                RPC.update(state= "by " + str(current_track.artist)[:125] + "  ", details= str(current_track.title)[:125] + "  ", small_image= "small", large_text= album_title[:121], small_text= genre, large_image= "large", start= time.mktime(time.localtime()))
            except:
                print ("Discord error")
                t = False
                return d, current_track
            t = current_track
        elif d and d != 60:
            time.sleep(10)
            return playing(t)

        if not(d):
            d = 60
    else:
        try:
            last_tracks = user.get_recent_tracks(limit=1, cacheable=False)
        except:
            print ("Error getting info about the most recently played track.")
            last_tracks = False
            return 5,False
        
        last_track = last_tracks[0].track
        try:
            d = current_track.get_duration()
            d = int(d / 1000)
        except:
            d = 60

        if t and last_track != t:
            print ("No track currently playing.\nLast played track:",last_track)
            try:
                RPC.update(state= "by " + str(last_track.artist)[:125] + "  ", details= str(last_track.title)[:125] + "  ", large_image= "pause", large_text= "Paused")
                t = False
            except:
                print("Discord error.")
        elif t:
            print ("No track currently playing.\nLast played track:",t)
            try:
                RPC.update(state= "by " + str(t.artist)[:125] + "  ", details= str(t.title)[:125] + "  ", large_image= "pause", large_text= "Paused")
                t = False
            except:
                print("Discord error")
        return d,last_track

    print("Track length:",d,"seconds")
    return d,t

while True:
    print("\n")
    d,t = playing(t)
    time.sleep(d)