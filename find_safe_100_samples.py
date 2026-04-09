from pathlib import Path
import json
import shutil

files = list(Path('./traj/direct_test_workspace/').glob('*/sessions/*.json'))
dst = Path('./simulation_traj_jsons_200_400/')
dst.mkdir(exist_ok=True)
for file in files[200:400]:
    shutil.copy(file, dst)
