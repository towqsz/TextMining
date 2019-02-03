def stopwords(func):
    def wrapper():
        try:
            from nltk.corpus import stopwords
            func()
        except:
            print("Could not import module. Stopwords not supported.")
            return False
    return wrapper
