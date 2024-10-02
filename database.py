import sqlite3
conn = sqlite3.connect("epnis.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Shows
               (showName TEXT PRIMARY KEY,
               numEpisodes INTEGER,
               showStatus TEXT,
               showQuality TEXT
                   )''')
cursor.execute('''CREATE TABLE IF NOT EXISTS User
               (userName TEXT PRIMARY KEY,
               password TEXT,
               profilePictureLink TEXT,
               email TEXT,
               downloadLocation TEXT)
               ''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Episode
               (showName TEXT,
               episodeNum INTEGER,
               360downloadLink TEXT,
               480downloadLink TEXT,
               720downloadLink TEXT,
               1080downloadLink TEXT,
               IsDownloaded TEXT,
               episodeTitle TEXT,
               releaseDate DATETIME,
               episodeLength INTEGER)
               ''')