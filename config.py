import os

config_path = os.path.dirname(os.path.abspath(__file__))


class Config:
    def __init__(self):
        self.data = os.path.join(config_path, 'data', 'data.json')
        self.origin_data = os.path.join(config_path, 'data', 'origin_data.txt')
        self.slot2id = os.path.join(config_path, 'data', 'slot2id.json')
        self.data_state = os.path.join(config_path, 'data', 'data_state.json')
        # vocab name: bert-base-uncased, bert-large-uncased, bert-base-cased, bert-large-cased, bert-base-multilingual-uncased, bert-base-multilingual-cased, bert-base-chinese
        self.vocab_name_or_path = os.path.join(config_path, 'data', 'bert-base-chinese-vocab.txt')
        # model name: bert-base-uncased, bert-large-uncased, bert-base-cased, bert-large-cased, bert-base-multilingual-uncased, bert-base-multilingual-cased, bert-base-chinese
        self.pretrained_model_name_or_path = os.path.join(config_path, 'data', 'bert-base-chinese.tar.gz')
        self.max_length = 32
        self.batch_size = 32
        self.epochs = 3
        self.max_grad_norm = 1.0
