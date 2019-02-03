from nltk.corpus import stopwords
from textblob import TextBlob
from textblob import Word

from Preprocessing.AbstractTextClearer import AbstractTextClearer
from Statistics.Statistics import Counter


class TextClearer(AbstractTextClearer):
    def remove_stop_words(self):
        stop = stopwords.words('english')
        self._text['tweet'] = self._text['tweet'].apply(
            lambda x: " ".join(x for x in x.split() if x not in stop))
        return self

    def remove_common_words(self):
        freq = list(Counter(self._text).count_most_common_words().index)
        self._text['tweet'] = self._text['tweet'].apply(
            lambda x: " ".join(x for x in x.split() if x not in freq))
        return self

    def remove_rare_words(self):
        freq = list(Counter(self._text).count_least_freq_words())
        self._text['tweet'] = self._text['tweet'].apply(
            lambda x: " ".join(x for x in x.split() if x not in freq))
        return self

    def correct_spelling(self):
        self._text['tweet'][:5].apply(
            lambda x: str(TextBlob(x).correct()))
        return self

    def tokenize(self):
        self._text = TextBlob(self._text['tweet']).words
        return self

    def lemmatize(self):
        self._text['tweet'] = self._text['tweet'].apply(
            lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))
        return self
