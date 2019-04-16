from flask import Flask, jsonify, render_template
import os
import sys
import math
import json as j


from flask_cors import CORS

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)

from config import Config

config = Config()

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

CORS(app)

@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Access-Control-Allow-Headers, Origin, X-Requested-With, Content-Type, Accept, Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS, HEAD'
    return response

@app.route('/api/test')
def emotion():
    return jsonify(hello='world')


@app.route('/api/read_data')
def read_data():
    if not os.path.exists(config.origin_data):
        return jsonify({'error': 'origin data is not exist'})

    state_json = {'state': 0}

    if not os.path.exists(config.data_state):
        with open(config.data_state, 'w') as state_file:
            j.dump(state_json, state_file, ensure_ascii=False)

    with open(config.data_state, 'r') as state_file:
        state_json = j.load(state_file)

    with open(config.origin_data, 'r', encoding='utf-8') as origin_data:
        datas = origin_data.readlines()

    data_size = len(datas)
    state = state_json['state']
    data = datas[state].strip('\n')

    state_json = {'state': state + 1}

    if state+1 < data_size:
        with open(config.data_state, 'w') as state_file:
            j.dump(state_json, state_file, ensure_ascii=False)

    return jsonify(data=data)


@app.route('/api/data_size')
def read_data_size():
    if not os.path.exists(config.origin_data):
        return jsonify({'error': 'origin data is not exist'})

    with open(config.origin_data, 'r', encoding='utf-8') as origin_data:
        datas = origin_data.readlines()

    return jsonify(size=len(datas))


@app.route('/api/read_data/<int:row>')
def read_data_by_row(row):
    if not os.path.exists(config.origin_data):
        return jsonify({'error': 'origin data is not exist'})

    with open(config.origin_data, 'r', encoding='utf-8') as origin_data:
        datas = origin_data.readlines()

    data = ''
    if row > len(datas):
        data = datas.pop().strip('\n')
    else:
        data = datas[row].strip('\n')
    return jsonify(data=data)


@app.route('/api/read_datas/<int:page>')
def read_data_by_page(page):
    if not os.path.exists(config.origin_data):
        return jsonify({'error': 'origin data is not exist'})

    with open(config.origin_data, 'r', encoding='utf-8') as origin_data:
        datas = origin_data.readlines()

    pages = len(datas) / config.page_limit
    pages = math.ceil(pages)

    if page > pages:
        page = pages

    start = (config.page_limit * (page - 1))
    end = start + config.page_limit

    data = datas[start:end]
    data = [d.strip('\n') for d in data]

    items = range(start, end)
    data = {items[index]: item for index, item in enumerate(data)}

    return jsonify(data=data, pages=pages)


if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=8000)
    app.run(host='localhost', port=8000)
