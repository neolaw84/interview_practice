import os
import tempfile

def remove_file_silently(filename: str):
    try:
        os.remove(filename)    
    except:
        pass

def write_text_to_temp_file(text_data:str = None):
    with tempfile.NamedTemporaryFile(mode="w+t", delete=False) as tf:
        tf.write(text_data)
    return tf.name
    

class TestTextFile(object):
    def __init__(self, test_data):
        self.filename = write_text_to_temp_file(test_data)
    
    def __enter__(self):
        return self.filename

    def __exit__(self, type, value, traceback):
        remove_file_silently(self.filename)