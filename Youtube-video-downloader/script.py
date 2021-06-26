import youtube_dl

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['link here'])

# Download video of high quality, type the following in commandline
# youtube-dl -F "link address"

# It will lists all the available quality from which choose the index number and type:
# youtube-dl -f <index> "link address"
