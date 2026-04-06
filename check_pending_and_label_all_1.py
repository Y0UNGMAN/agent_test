from pathlib import Path
import json
import shutil
file_path = Path('./traj/Qwen3-32B/traj_qwen3_32b/direct_test_workspace/')
to_path = Path('./check_pending_1_json/Qwen3-32B/')
for file in file_path.glob('*/sessions/*.json'):
    try:
        with open(file , 'r' , encoding='utf-8') as f:
            json_file = json.load(f)
        
        if (json_file["label"]==1) and (json_file["pending"]==1) :
            to_path.mkdir(parents=True , exist_ok=True)
            shutil.copy(file , to_path)
    except Exception as e:
        print(f"Skip {file} because {e}")

