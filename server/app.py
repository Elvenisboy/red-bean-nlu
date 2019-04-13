import os
import sys
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

    state = 0        

    if not os.path.exists(config.data_state):
        with open(config.data_state, 'w') as state_file:
            state_file.write('0')

    state_file =  open(config.data_state, 'w+')
    print('data:', state_file.read())  
    
    print('-1:', state_file.read())
    print('-2:', state_file.readlines())

    if state_file.read() is '':
        state_file.write('0')
    else:
        state = int(state_file.read())
        print('0:', state)

    with open(config.origin_data, 'r', encoding='utf-8') as data_file:
        datas = data_file.readlines()
        print(datas)

        data = datas[state].strip('\n')
        state = int(state) + 1
        print('1:', state)
        state_file.seek(0)
        state_file.truncate()
        state_file.write(str(state))
        state_file.close()
        return json({'hello': data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

