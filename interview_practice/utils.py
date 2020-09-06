import sys


class TextFileOrStdInOut(object):
    def __init__(self, filename: str=None, mode: str="rt"):
        self.filename = filename
        self.mode = mode
        if self.filename:
            self._file = open(self.filename, self.mode)
        else:
            self._file = sys.stdin if self.mode=="rt" else sys.stdout
    
    def __enter__(self):
        return self._file

    def __exit__(self, type, value, traceback):
        try:
            self._file.close()
        except: 
            pass


def read_integer_from_text_file(fptr):
    return int(fptr.readline())

def read_integer_list_from_text_file(fptr, sep: str = None):
    return [int(item) for item in fptr.readline().split(sep)]