from Preprocessing.AbstractTextClearer import AbstractTextClearer


class PreprocessingDirector:
    def process(self, builder: AbstractTextClearer):
        return builder\
            .remove_common_words()\
            .remove_rare_words()\
            .correct_spelling()()
