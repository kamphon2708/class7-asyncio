import time
from random import randint
import requests as requests
from flask import Flask, render_template

app = Flask(__name__)

# def get_xkcd_image():
async def get_xkcd_image(session):
    comicid = randint(0,1000)
    responce = requests.get(f'http://xkcd.com/{comicid}/info.0.json')
    return responce.json() ['img']
    

@app.get('/comic')
def hello ():
    start = time.perf_counter()
    url = get_xkcd_image()
    end = time.perf_counter()
    return render_template('index.html', end=end,start=start,urls = [url])


if __name__ == '__main__' :
    app.run(debug=True, port=5555)