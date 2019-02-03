import abc


class AbstractCounter(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def refresh_text(self):
        pass

    @abc.abstractmethod
    def words_number(self):
        pass

    @abc.abstractmethod
    def characters_number(self):
        pass

    @abc.abstractmethod
    def average_word_length(self):
        pass

    @abc.abstractmethod
    def add_stop_word(self, word):
        pass

    @abc.abstractmethod
    def count_stop_words(self, word=None):
        pass

    @abc.abstractmethod
    def count_special_char(self):
        pass

    @abc.abstractmethod
    def count_numeric(self):
        pass

    @abc.abstractmethod
    def count_uppercase_words(self):
        pass

    @abc.abstractmethod
    def count_most_common_words(self):
        pass

    @abc.abstractmethod
    def count_least_freq_words(self):
        pass

    def show(self):
        pass
