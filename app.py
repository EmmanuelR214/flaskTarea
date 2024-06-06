from flask import Flask, render_template, request, redirect, url_for
from youtubesearchpython import VideosSearch

app = Flask(__name__)

library = {
    "Dolido": "https://youtu.be/9lYO2xJBtJM?si=Hdbgn38YBlDfIevs",
    "Proyecto x": "https://youtu.be/Y61v8iXbxvA?si=BKM5nRQmwsV1BaDi",
    "Lady gaga": "https://youtu.be/3Wnso2A4PZE?si=yHJFWv8X3gvA1kFI"
}
playlists = {}

@app.route('/')
def index():
    return render_template('index.html', library=library, playlists=playlists)

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    search = VideosSearch(query, limit=10)
    results = search.result()
    songs = results['result']
    return render_template('index.html', songs=songs, library=library, playlists=playlists)

@app.route('/add_to_library', methods=['POST'])
def add_to_library():
    song_url = request.form['song_url']
    song_title = request.form['song_title']
    if song_title not in library:
        library[song_title] = song_url
    return redirect(url_for('index'))

@app.route('/create_playlist', methods=['POST'])
def create_playlist():
    playlist_name = request.form['playlist_name']
    if playlist_name not in playlists:
        playlists[playlist_name] = []
    return redirect(url_for('index'))

@app.route('/add_to_playlist', methods=['POST'])
def add_to_playlist():
    playlist_name = request.form['playlist_name']
    song_url = request.form['song_url']
    if playlist_name in playlists:
        playlists[playlist_name].append(song_url)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
