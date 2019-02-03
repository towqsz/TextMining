from Statistics.AbstractStatistics import AbstractCounter
from Libraries.statistics_lib import avg_word_len
from Libraries.decorators import stopwords
import pandas as pd
import copy


class Counter(AbstractCounter):
    def __init__(self, text):
        self._text = text
        self._text_copy = copy.deepcopy(text)

    def refresh_text(self):
        self._text_copy = copy.deepcopy(self._text)

    def words_number(self):
        self.refresh_text()
        self._text_copy['word_count'] = self._text_copy['tweet'].apply(
            lambda x: len(str(x).split(" ")))
        return self._text_copy[['tweet', 'word_count']]

    def characters_number(self):
        self.refresh_text()
        self._text_copy['char_count'] = self._text_copy[
            'tweet'].str.len()
        return self._text_copy[['tweet', 'char_count']]

    def average_word_length(self):
        self.refresh_text()
        self._text_copy['avg_word'] = self._text_copy['tweet'].apply(
            lambda x: avg_word_len(x))
        return self._text_copy[['tweet', 'avg_word']]

    @stopwords
    def add_stop_word(self, word):
        self.refresh_text()
        self._stop = stopwords.words(word)

    def stop_words(self, words):
        self.refresh_text()
        self._text_copy['stopwords'] = self._text_copy['tweet'].apply(
            lambda x: len([x for x in x.split() if x in words]))
        return self._text_copy[['tweet', 'stopwords']]

    def count_stop_words(self, word=None):
        self.refresh_text()
        if word is not None:
            return self.stop_words([word])
        else:
            return self.stop_words("the")

    def count_special_char(self):
        self.refresh_text()
        self._text_copy['hashtags'] = self._text_copy['tweet'].apply(
            lambda x: len([x for x in x.split() if x.startswith('#')]))
        return self._text_copy[['tweet', 'hashtags']]

    def count_numeric(self):
        self.refresh_text()
        self._text_copy['numerics'] = self._text_copy['tweet'].apply(
            lambda x: len([x for x in x.split() if x.isdigit()]))
        return self._text_copy[['tweet', 'numerics']]

    def count_uppercase_words(self):
        self.refresh_text()
        self._text_copy['upper'] = self._text_copy['tweet'].apply(
            lambda x: len([x for x in x.split() if x.isupper()]))
        return self._text_copy[['tweet', 'upper']]

    def count_most_common_words(self):
        self.refresh_text()
        freq = pd.Series(
            ' '.join(self._text_copy['tweet']).split()).value_counts()[:10]
        return freq

    def count_least_freq_words(self):
        self.refresh_text()
        freq = pd.Series(
            ' '.join(self._text_copy['tweet']).split()).value_counts()[-10:]
        return freq

    def show(self):
        print(self.words_number().head())
        print(self.characters_number().head())
        print(self.average_word_length().head())
        print(self.count_stop_words("the").head())
        print(self.count_special_char().head())
        print(self.count_numeric().head())
        print(self.count_uppercase_words().head())
        print(self.count_most_common_words())
        print(self.count_least_freq_words())
