import os
import sys

from pytorch_pretrained_bert import BertAdam, BertForTokenClassification
import torch
from tqdm import tqdm
import numpy as np

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from config import Config

config = Config()

from process_data import getSlot2Id, processData, getDataLoader

def getOptim(model):
    FULL_FINETUNING = True
    if FULL_FINETUNING:
        param_optimizer = list(model.named_parameters())
        no_decay = ['bias', 'gamma', 'beta']
        optimizer_grouped_parameters = [
            {
                'params': [p for n, p in param_optimizer if not any(nd in n for nd in no_decay)],
                'weight_decay_rate': 0.01
            },
            {
                'params': [p for n, p in param_optimizer if any(nd in n for nd in no_decay)],
                'weight_decay_rate': 0.0
            }
        ]
    else:
        param_optimizer = list(mode.classifier.named_parameters())
        optimizer_grouped_parameters = [{"params": [p for n,p in param_optimizer]}]

    optimizer = BertAdam(optimizer_grouped_parameters, lr=3e-5)      

    return optimizer

def _flat_accuracy(preds, labels):
  pred_flat = np.argmax(preds, axis=2).flatten()
  labels_flat = labels.flatten()
  return np.sum(pred_flat == labels_flat) / len(labels_flat)

def train(model, device,  train_data, val_data, epochs, max_grad_norm):
    optimizer = getOptim(model) # 获取优化器

    train_batch_data_num = list(train_data)[0][0].size()[0] # 获取每个batch中的数据个数（不一定等于batch_size）
    val_batch_data_num = list(val_data)[0][0].size()[0]

    i, j = 0, 0

    for _ in train_data:
        i = i + 1

    for _ in val_data:
        j = j + 1         

    data_length = train_batch_data_num * i + val_batch_data_num * j # 计算数据的总数

    for epoch in range(epochs):
        print("Epoch", epoch)
        model.train()
        tr_loss = 0
        nb_tr_steps = 0

        pbar = tqdm(total=data_length, ascii=True)
        for step, batch in enumerate(train_data):
            batch = tuple(t.to(device) for t in batch)
            x, mask, y = batch
            
            loss = model(x, token_type_ids=None,
                        attention_mask=mask, labels=y)
            
            loss.backward()
            
            tr_loss += loss.item()
            nb_tr_steps += 1
            
            torch.nn.utils.clip_grad_norm_(parameters=model.parameters(), max_norm=max_grad_norm)
            
            optimizer.step()
            model.zero_grad()

            pbar.set_description("Train loss: {}".format(tr_loss/nb_tr_steps))
            pbar.update(x.size(0))

        pbar.set_description("Train loss: {}".format(tr_loss/nb_tr_steps)) 
        model.eval()
        eval_accuracy = 0
        nb_eval_steps = 0
        predictions, true_labels = [], []  

        for batch in valid_dataloader:
            batch = tuple(t.to(device) for t in batch)
            x, mask, y = batch       

            with torch.no_grad():
                logits = model(x, token_type_ids=None,
                                    attention_mask=mask)
                logits = logits.detach().cpu().numpy()
                y_ids = y.to('cpu').numpy()
                
                predictions.extend([list(p) for p in np.argmax(logits, axis=2)])
                true_labels.append(label_ids)
                
                tmp_eval_accuracy = _flat_accuracy(logits, y_ids)
                
                eval_accuracy += tmp_eval_accuracy

                nb_eval_steps += 1

                pbar.update(x.size(0))

        pbar.set_description("Train loss: {} , Validation Accuracy: {}".format(tr_loss/nb_tr_steps, eval_accuracy/nb_eval_steps)) 
        pbar.close()

def main():
    slot2Id = getSlot2Id()

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = BertForTokenClassification.from_pretrained(
        config.pretrained_model_name_or_path, num_labels=len(slot2Id))
    model.to(device)

    x, y = processData()
    train_dataloader, val_dataloader = getDataLoader(x, y)

    train(model, device, train_dataloader, val_dataloader, config.epochs, config.max_grad_norm)