import pandas as pd
import string
from pathlib import Path
from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.models import KeyedVectors

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args,
                                                                 **kwargs)
        return cls._instances[cls]


class FileManager(metaclass=Singleton):
    def __init__(self, file_name: string):
        self.mypath = Path().absolute()
        self._file = pd.read_csv(file_name)
        self._file_name = file_name

    @property
    def file(self):
        return self._file

    @property
    def file_name(self):
        return self._file_name

    def convert_to_word2vec(self):
        glove_input_file = self._file_name
        word2vec_output_file = glove_input_file + '.word2vec'
        glove2word2vec(glove_input_file, word2vec_output_file)
        self._file = word2vec_output_file


