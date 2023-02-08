import os
import glob
import numpy as np

def get_total_size(folder_path:str)-> float:
    total_size = 0
    for filename in glob.glob(os.path.join(folder_path, '*.wav')):
        total_size += os.path.getsize(filename)
    return round(total_size / 1024 / 1024, 2)



