def avg_word_len(sentence):
    words = sentence.split()
    return sum(len(word) for word in words) / len(words)


class statisticsType:
    WORDS_NUMBER = "words_number"
    CHARACTERS_NUMBER = "characters_number"
    AVERAGE_WORD_LENGTH = "average_word_length"
    STOP_WORDS = "count_stop_words"
    SPECIAL_CHARS = "count_special_char"
    NUMERICS = "count_numeric"
    UPPERCASE_WORDS = "count_uppercase_words"
    MOST_COMMON_WORDS = "count_most_common_words"
    LEAST_FREQ_WORDS = "count_least_freq_words"
