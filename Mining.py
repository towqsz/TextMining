from textblob import TextBlob
from gensim.scripts.glove2word2vec import glove2word2vec
from FileManager import FileManager
from gensim.models import KeyedVectors
from sklearn.feature_extraction.text import CountVectorizer


class TextAnalyzer:
    def __init__(self, text):
        self._text = text


class SentimentalAnalyzer:
    def __init__(self, text):
        self._text = text

    def proccess_data(self):
        self._text['sentiment'] = self._text['tweet'].apply(
            lambda x: TextBlob(x).sentiment[0])
        return self._text[['tweet', 'sentiment']]


class WordEmbedder:
    def __init__(self, file_manager):
        self._file_manager = file_manager

    def get_model(self):
        filename = self._file_manager.file_name + '.word2vec'
        self._model = KeyedVectors.load_word2vec_format(filename, binary=False)
        return self._model

    def find_vector(self, word1, word2):
        return (self._model[word1] + self._model[word2])/2


class BagOfWords:
    def __init__(self, file_manager):
        self._file_manager = file_manager

    def find_bag_of_words(self):
        self._vector = CountVectorizer(max_features=1000, lowercase=True,
                                       ngram_range=(1, 1), analyzer="word")
        self._bow = self._vector.fit_transform(self._file_manager.file['tweet'])

    def get_names(self):
        return self._vector.get_feature_names()

    def get_similiarity_array(self):
        return self._bow.toarray()

    def find_most_smiliar_tweets(self):
        self.find_bag_of_words()

        tweet1 = None
        tweet2 = None
        max_similarity = 0
        for counter1, element1 in enumerate(self.get_similiarity_array()[:100]):
            for counter2, element2 in enumerate(
                    self.get_similiarity_array()[:100]):
                similarity = sum(element1 & element2)
                if similarity > max_similarity and self._file_manager.file['tweet'][counter1] != self._file_manager.file['tweet'][counter2]:
                    max_similarity = similarity
                    tweet1 = self._file_manager.file['tweet'][counter1]
                    tweet2 = self._file_manager.file['tweet'][counter2]
        print(max_similarity)
        return tweet1, tweet2
