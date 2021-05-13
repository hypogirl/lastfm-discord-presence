# lastfm-discord-presence
Python script to show the last.fm song you're currently playing on your discord rich presence.

![song with album title](https://imgur.com/zV3M83m.png "song with album title") ![song with genres](https://i.imgur.com/7TA58Es.png "song with genres")
![song paused](https://i.imgur.com/jmsnOLm.png "song paused")

## Requirements:
### pylast
```
pip install pylast
```

### pypresence
```
pip install pypresence
```
### variables.py
(Check variables_example.py on this repo)

## Features:
- Shows song title, artist, album, top two artist genres and the time the song has been playing for.
- Tries to retrieve song length and only tries to look for a new song playing after that length has passed (if there's no song length available, the default length is 60 seconds).
- If there are no songs playing, it shows the information for the last song played but states that it's paused.
- If song has "acoustic" in the title, it automatically changes the genre to "acoustic".
- If the two top genres belong to same genre branch (e.g. black metal -> ambient black metal) it will look for a third genre to replace the broadest one of the two (e.g. replacing black metal with atmospheric black metal). This does not apply to different subgenres (e.g. indie pop vs electropop)
![same genre ignored](https://i.imgur.com/Mf1eStZ.png "same genre ignored")
