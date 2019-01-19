from nltk.corpus import stopwords
from Statistics import Counter
from textblob import TextBlob
from nltk.stem import PorterStemmer
from textblob import Word

class TextClearer:
    def __init__(self, text):
        self._text = text

    def remove_stop_words(self):
        stop = stopwords.words('english')
        self._text['tweet'] = self._text['tweet'].apply(
            lambda x: " ".join(x for x in x.split() if x not in stop))
        return self._text['tweet']

    def remove_common_words(self):
        freq = list(Counter(self._text).count_most_common_words().index)
        self._text['tweet'] = self._text['tweet'].apply(
            lambda x: " ".join(x for x in x.split() if x not in freq))
        return self._text['tweet']

    def remove_rare_words(self):
        freq = list(Counter(self._text).count_least_freq_words())
        self._text['tweet'] = self._text['tweet'].apply(
            lambda x: " ".join(x for x in x.split() if x not in freq))
        return self._text['tweet']

    def correct_spelling(self):
        return self._text['tweet'][:5].apply(
            lambda x: str(TextBlob(x).correct()))

    def tokenize(self):
        return TextBlob(self._text['tweet']).words

    def lemmatize(self):

        self._text['tweet'] = self._text['tweet'].apply(
            lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))
        return self._text['tweet']
