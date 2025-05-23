playlist = []

song = ("Hello", "Adele", 4.5)
playlist.append(song)

print("Playlist:")
for song in playlist:
    print(f"{song[0]} — {song[1]} ({song[2]} minutes)")
