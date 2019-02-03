import pandas as pd
import string
from pathlib import Path
from gensim.scripts.glove2word2vec import glove2word2vec
from Designs.Restore import memento
from Designs.Borg import Borg


class FileManager(Borg):
    def __init__(self, file_name=""):
        super(FileManager, self).__init__()
        if not hasattr(self, "_file"):
            self.read_file(file_name)
            self.restore = memento(self)

    def read_file(self, file_name: string):
        self.mypath = Path().absolute()
        self._file = pd.read_csv(file_name)
        self._file_name = file_name

    @property
    def file(self):
        return self._file

    def set_file(self, file):
        self._file = file

    @property
    def file_name(self):
        return self._file_name

    def convert_to_word2vec(self):
        glove_input_file = self._file_name
        word2vec_output_file = glove_input_file + '.word2vec'
        glove2word2vec(glove_input_file, word2vec_output_file)
        self._file = word2vec_output_file


