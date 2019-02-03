from abc import ABC, abstractmethod
from Preprocessing.Data import Data


class AbstractTextClearer(ABC):

    def __init__(self):
        self.data = Data()
        self._text = self.data._text
        self.method = None

    def __call__(self):
        return self._text

    @abstractmethod
    def remove_stop_words(self):
        pass

    @abstractmethod
    def remove_common_words(self):
        pass

    @abstractmethod
    def remove_rare_words(self):
        pass

    @abstractmethod
    def correct_spelling(self):
        pass

    @abstractmethod
    def tokenize(self):
        pass

    @abstractmethod
    def lemmatize(self):
        pass

