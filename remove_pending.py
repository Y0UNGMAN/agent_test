from pathlib import Path
import json

file_path = Path('./traj/Qwen3-8B/traj/direct_test_workspace/')
count = 0
for file in file_path.glob('*/sessions/*.json'):
    with open(file , 'r' , encoding='utf-8') as f:
        json_file = json.load(f)
    
    del json_file["pending"]

    with open(file, 'w', encoding='utf-8') as f:
        json.dump(json_file, f, ensure_ascii=False, indent=4)