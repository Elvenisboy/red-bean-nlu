import os
import sys
import math
import json as j

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

    state_json = {'state': 0}        

    if not os.path.exists(config.data_state):
        with open(config.data_state, 'w') as state_file:
            j.dump(state_json, state_file, ensure_ascii=False)

    with open(config.data_state, 'r') as state_file:
        state_json = j.load(state_file)

    with open(config.origin_data, 'r', encoding='utf-8') as origin_data:
        datas =  origin_data.readlines()         

    data_size = len(datas)
    state = state_json['state']
    data = datas[state].strip('\n')
    
    state_json = {'state': state + 1}

    if state+1 < data_size: 
        with open(config.data_state, 'w') as state_file:
            j.dump(state_json, state_file, ensure_ascii=False)

    return json({'data': data}, ensure_ascii=False)

@app.route('/api/data_size')
async def read_data_size(request):
    if not os.path.exists(config.origin_data):
        return json({'error':'origin data is not exist'})

    with open(config.origin_data, 'r', encoding='utf-8') as origin_data:
        datas =  origin_data.readlines()     

    return json({'size': len(datas)})                

@app.route('/api/read_data/<row:int>')
async def read_data_by_row(request, row):
    if not os.path.exists(config.origin_data):
        return json({'error':'origin data is not exist'})

    with open(config.origin_data, 'r', encoding='utf-8') as origin_data:
        datas =  origin_data.readlines() 

    data = ''
    if row > len(datas):
        data = datas.pop().strip('\n')
    else:
        data = datas[row-1].strip('\n')
    return json({'data': data}, ensure_ascii=False)

@app.route('/api/read_datas/<page:int>')
async def read_data_by_page(request, page):
    if not os.path.exists(config.origin_data):
        return json({'error':'origin data is not exist'})

    with open(config.origin_data, 'r', encoding='utf-8') as origin_data:
        datas =  origin_data.readlines() 

    pages = len(datas) / config.page_limit
    pages = math.ceil(pages)

    if page > pages:
        page = pages

    start = (config.page_limit * (page - 1))
    end = start + config.page_limit

    data = datas[start:end]
    data = [d.strip('\n') for d in data]

    return json({'data': data, 'pages': pages}, ensure_ascii=False)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
