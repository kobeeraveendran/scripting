import os
import shutil
import schedule
import time

directory = 'D:/Downloads'

def clearDirectory():
    for this_file in os.listdir(directory):
        file_path = os.path.join(directory, this_file)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
            
        except Exception as e:
            print(e)

schedule.every(7).days.at("19:00").do(clearDirectory())

while True:
    schedule.run_pending()
    time.sleep(3600)
