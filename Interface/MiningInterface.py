from FileManager import FileManager
from Mining import BagOfWords, SentimentalAnalyzer, WordEmbedder
from Statistics.StatisticsManager import StatisticsManager
from Statistics.Statistics import Counter
from Libraries.statistics_lib import statisticsType
from Preprocessing.PreprocessingDirector import PreprocessingDirector
from Preprocessing.TextClearer import TextClearer


class MiningInterface:
    def __init__(self, file_name):
        self.file_manager = FileManager(file_name)
        self.file = self.file_manager.file

    def get_available_actions(self):
        pass

    def get_statistics(self, st_type):
        self.statistics = StatisticsManager(Counter(self.file))
        return statistics.get_statistics(st_type)

    def get_all_statistics(self):
        self.statistics = StatisticsManager(Counter(self.file))
        action_types = [
            a for a in dir(statisticsType) if not a.startswith('__')]
        for st_type in action_types:
            yield self.statistics.get_statistics(
                getattr(statisticsType, st_type))

    def prepare_file(self):
        preprocesed = PreprocessingDirector().process(TextClearer())
        return preprocesed

    def get_sentimental(self):
        return SentimentalAnalyzer(self.file).proccess_data()

    def bow(self):
        self._bow = BagOfWords(self.file_manager)
        self._bow.find_bag_of_words()

    def get_bow_names(self):
        self.bow()
        return self._bow.get_names()

    def get_similiarity_array(self):
        self.bow()
        return self._bow.get_similiarity_array()

    def get_most_similiar_tweets(self):
        self.bow()
        return self._bow.find_most_smiliar_tweets()

    def restore(self):
        self.file_manager.restore()
