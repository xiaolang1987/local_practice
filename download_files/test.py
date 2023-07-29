import yaml

with open("download_info.yml", "r", encoding="utf-8") as f:
    print(yaml.load(f, Loader=yaml.FullLoader))
