import json
from pathlib import Path

json_path = Path('./finished_label_100/Qwen3-32B/')
total = 0
count = 0
for file in json_path.glob('*.json'):
    total += 1
    with open(file , 'r' , encoding='utf-8') as f:
       data = json.load(f)
    
    if data['label'] == data['judge']:
        count += 1


print(f'总数: {total}, 正确数: {count}, 准确率: {count/total:.2%}')