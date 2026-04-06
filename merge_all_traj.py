from pathlib import Path
import json

path_files = Path("./finished_label_100/Qwen3-8B/").glob("*.json")
merge_datas = []
for file in path_files:
    with open(file, "r", encoding='utf-8') as f:
        data = json.load(f)
        merge_datas.append({
            'trajectories': data['trajectory'],  # 修正：trajectory -> trajectories
            'human_anno': data['label'],
            'cot': data['explain']
        })


with open("./merge_all_traj.json", "w", encoding='utf-8') as f_out:
    json.dump(merge_datas, f_out, ensure_ascii=False, indent=4)
print(f"已将所有轨迹数据合并到 merge_all_traj.json 文件中")

