import json
from pathlib import Path

json_path = Path('./traj/Qwen3-32B/traj_qwen3_32b/direct_test_workspace/')
count = 0
print('----------START----------')
for p in json_path.glob('*/sessions/*.json'):
    count += 1
    res = {}
    with open(p, 'r', encoding='utf-8') as f:
        temp = json.load(f)
        res['trajectory'] = temp
        res['label'] = 0
        res['pending'] = 0
        res['explain'] = ""

    with open(p, 'w', encoding='utf-8') as f:
        json.dump(res, f, ensure_ascii=False, indent=4)
        
print(f'----------TOTAL FINISH {count}----------')
print('----------SUCCESS----------')