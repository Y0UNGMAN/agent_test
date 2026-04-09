from pathlib import Path


for file in Path('./simulation_traj_jsons_200_400/').glob('*.json'):
    new_name = f"simulation_{file.stem}.json"
    file.rename(file.with_name(new_name))