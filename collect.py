#!/bin/env python3
import os
import json
import shutil
from os.path import join, splitext
from collections import defaultdict

datasets_dir = "datasets"
img_dir = "img"

name2path = defaultdict(list)

for folder, subs, files in os.walk(datasets_dir):
    for file_name in files:
        file_path = join(folder, file_name)
        name2path[file_name].append(file_path)


with open("data.json") as f:
    data = json.load(f)
        
for key, value in data.items():
    ext = splitext(value['name'])[1]
    dst_path = join(img_dir, f"{key}{ext}")
    src_path_options = name2path[value['name']]
    for src_path in src_path_options:
        if value['dataset'] in src_path:
            print(f"{src_path} -> {dst_path}")
            shutil.copy2(src_path, dst_path)
            break
