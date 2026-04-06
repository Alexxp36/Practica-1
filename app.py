from flask import Flask, request, send_file
import yt_dlp
import os

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <h2>Descargar video</h2>
    <form method="POST" action="/download">
        <input type="text" name="url" placeholder="Pega el link">
        <button type="submit">Descargar</button>
    </form>
    '''

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    filename = "video.mp4"

    ydl_opts = {
        'outtmpl': filename,
        'format': 'mp4'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
