def avg_word_len(sentence):
    words = sentence.split()
    return sum(len(word) for word in words) / len(words)
