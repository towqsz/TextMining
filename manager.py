from Statistics import Counter
from FileManager import FileManager
from Mining import BagOfWords, SentimentalAnalyzer, WordEmbedder
from Preprocessing import TextClearer


def print_header(header):
    print("\n\n")
    print("_" * 100)
    print(header)


def main():
    file_manager = FileManager("train_tweets.csv")
    file = file_manager.file
    #print(file)

    print_header("Wyświetl statystyki:")
    cntr = Counter(file)
    cntr.show()

    print_header("Popraw tekst:")
    text_clearer = TextClearer(file)


    text_clearer.remove_common_words()
    text_clearer.remove_rare_words()
    text_clearer.correct_spelling()
    #file = text_clearer.lemmatize()
    #print(file)

    print(SentimentalAnalyzer(file).proccess_data())

    # embedder = WordEmbedder(file_manager)
    # print(embedder.get_model())
    # print(embedder.find_vector("go", "away"))


    bow = BagOfWords(file_manager)
    bow.find_bag_of_words()
    print(bow.get_names())
    print(bow.get_similiarity_array())
    print(bow.find_most_smiliar_tweets())




if __name__ == "__main__":
    main()