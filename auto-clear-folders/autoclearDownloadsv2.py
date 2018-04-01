import os
import shutil

directory = 'D:/Downloads'

for this_file in os.listdir(directory):
    file_path = os.path.join(directory, this_file)
    try:
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    
    except Exception as e:
        print(e)