playlist = []

song = ("Hello", "Adele", 4.5)
playlist.append(song)

print("Playlist:")
for name, artist, duration in playlist:
    print(f"{name} — {artist} ({duration} minutes)")
