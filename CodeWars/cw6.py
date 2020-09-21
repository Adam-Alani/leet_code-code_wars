def song_decoder(song):
    badchars = "WUB"
    song = song.replace("WUB", ' ')
    song = " ".join(song.split())
    print(song)









print((song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")))
