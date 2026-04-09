from pathlib import Path
import json
import shutil

dist = Path('./simulation_judge1')
dist.mkdir(parents=True , exist_ok=True)
files = Path('./simulation_traj_jsons_200_400/').glob('*.json')
total = 0
count=0
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        total += 1
        data = json.load(f)
        if data['judge'] == 1:
            shutil.copy(file, dist)
            count += 1

print(f"共处理 {total} 个文件，其中 {count} 个文件的 judge 字段为 1，并已复制到 {dist} 目录下。")