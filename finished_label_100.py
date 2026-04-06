from pathlib import Path
import json
import shutil
# qwen3_8b_json = Path('./traj/Qwen3-8B/traj/direct_test_workspace/')
qwen3_8b_json = Path('./traj/Qwen3-32B/traj_qwen3_32b/direct_test_workspace/')

backup_dir = Path('./finished_label_100/Qwen3-32B/')
# backup_dir = Path('./finished_label_100/Qwen3-8B/')
backup_dir.mkdir(parents=True , exist_ok=True)

for i in range(52):
    source_file = qwen3_8b_json.glob(f'direct_test_{i+1}_*/sessions/test_case_{i+1}.json')
    for file in source_file:
        shutil.copy2(file , backup_dir)
    
print("前50个文件夹的 json 文件已全部复制完毕！")


