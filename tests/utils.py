import os

def remove_file_silently(filename: str):
    try:
        os.remove(filename)    
    except:
        pass