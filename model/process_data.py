from pytorch_pretrained_bert import BertTokenizer
import json
import os
import sys

import torch
from keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from torch.utils.data import (DataLoader, RandomSampler, SequentialSampler,
                              TensorDataset)

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from config import Config

config = Config()

tokenizer = BertTokenizer.from_pretrained(
    config.vocab_name_or_path, do_lower_case=True)
# print(tokenizer.tokenize('你是个傻子'))


def id2Mask(ids=[]):
    return [float(id > 0) for id in ids]


def processData():
    with open(config.data, 'r', encoding='utf-8') as file:
        data = json.load(file)

    targets = []
    labels = []

    for x in data['nlu_data']:
        intent = x['intent']
        text = x['text']
        label = ['O'] * len(text)
        slots = x['slots']

        for slot in slots:
            start = slot['start']
            end = slot['end']
            for i in range(len(text)):
                label[start] = 'B-' + slot['slot']
                if start is not end and i > start and i <= end:
                    label[i] = 'I-' + slot['slot']

        targets.append(tokenizer.tokenize(text))
        labels.append(label)

    return targets, labels


def toJson(labels=[], target=[]):
    slots = []
    slot = {}
    state = False

    for key, item in enumerate(labels):
        if item[0] is 'B' and key+1 is len(labels):
            slot['start'] = key
            slot['end'] = key
            slots.append(slot.copy())
        elif item[0] is 'B' and d[key-1][0] is 'I':
            slot['end'] = key - 1
            slots.append(slot.copy())
            slot = {}
            slot['start'] = key
        elif item[0] is "B":
            state = True
            slot['start'] = key
        elif item[0] is 'O' and state is True:
            state = False
            slot['end'] = key - 1
            slots.append(slot.copy())
            slot = {}

    new_slots = []

    for s in slots:
        start = s['start']
        end = s['end']
        if start is end:
            new_slots.append({
                'start': start,
                'end': end,
                'value': ''.join(target[start]),
                'slot': labels[start][2:]
            })
        else:
            new_slots.append({
                'start': start,
                'end': end,
                'value': ''.join(target[start:end+1]),
                'slot': labels[start][2:]
            })

    # print(d[2:4])
    return new_slots


def getSlot2Id():
    if os.path.exists(config.slot2id) is True:
        with open(config.slot2id, 'r', encoding='utf-8') as file:
            slot2id = json.load(file)
        return slot2id
    else:
        slot2id = {'O': 0}
        with open(config.data, 'r', encoding='utf-8') as file:
            data = json.load(file)
        for x in data['nlu_data']:
            slots = x['slots']
            for slot in slots:
                if 'B-' + slot['slot'] not in slot2id:
                    index = len(slot2id)
                    slot2id['B-' + slot['slot']] = index
                    slot2id['I-' + slot['slot']] = index + 1
        with open(config.slot2id, 'w') as file:
            json.dump(slot2id, file, ensure_ascii=False)

        return slot2id


def data2Id(x=[], y=[]):
    slot2Id = getSlot2Id()
    x = [tokenizer.convert_tokens_to_ids(
        tokenized_text) for tokenized_text in x]
    x = pad_sequences(x, maxlen=config.max_length,
                      dtype="long", truncating="post", padding="post")

    y = [[slot2Id.get(lab) for lab in label] for label in y]
    y = pad_sequences(y, maxlen=config.max_length,
                      dtype="long", truncating="post", padding="post")

    masks = [id2Mask(ids) for ids in x]

    return x, y, masks


def _getSplitData(x=[], y=[], masks=[]):
    train_x, val_x, train_y, val_y = train_test_split(
        x, y, random_state=2333, test_size=0.1)
    train_masks, val_masks, _, _ = train_test_split(
        masks, x, random_state=2018, test_size=0.1)

    train_x = torch.tensor(train_x)
    val_x = torch.tensor(val_x)
    train_masks = torch.tensor(train_masks)
    train_y = torch.tensor(train_y)
    val_y = torch.tensor(val_y)
    val_masks = torch.tensor(val_masks)

    return train_x, val_x, train_masks, train_y, val_y, train_masks


def getDataLoader(x=[], y=[]):
    x, y, masks = data2Id(x, y)
    train_x, val_x, train_masks, train_y, val_y, val_masks = _getSplitData(
        x, y, masks)

    train_data = TensorDataset(train_x, train_masks, train_y)
    train_sampler = RandomSampler(train_data)
    train_dataloader = DataLoader(
        train_data, sampler=train_sampler, batch_size=config.batch_size)

    val_data = TensorDataset(val_x, val_masks, val_y)
    val_sampler = SequentialSampler(val_data)
    val_dataloader = DataLoader(
        val_data, sampler=val_sampler, batch_size=config.batch_size)

    return train_dataloader, val_dataloader
# # d = ['O', 'O', 'B-address', 'I-address',
# #      'B-date-time', 'I-date-time', 'O', 'O', 'O']

# # t = '我要上海明天的天气'

# # print(toJson(d, tokenizer.tokenize(t)))
# # print(processData())
# # print()
# # print(getSlot2Id())


# x, y = processData()
# # x, y, masks = data2Id(x, y)

# # t_x, v_x, t_masks, t_y, v_y, v_masks =  getSplitData(x, y, masks)

# # print(v_masks)
# train_dataloader, val_dataloader = getDataLoader(x, y)
# t_data_length = list(train_dataloader)[0][0].size()[0]
# v_data_length = list(val_dataloader)[0][0].size()[0]
# print(t_data_length + v_data_length)
