import os
import sys

from sanic import Sanic
from sanic.exceptions import abort
from sanic.response import json

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)

from config import Config

config = Config()

app = Sanic()

@app.route('/api/test')
async def emotion(request):
    return json({'hello': 'world'})

@app.route('/api/read_data')
async def read_data(request):
    if not os.path.exists(config.origin_data):
        return json({'error':'origin data is not exist'}) 
    return json({'hello': 'world'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

