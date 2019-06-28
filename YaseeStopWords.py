from wordcloud import STOPWORDS

UCIWC_DEFAULTSTOPWORDS = {"nan", "student", "wanted", "talked", "discussed",
                          "want", "talk", "discussed", "paper", "write",
                          "wrote", "writing", "will", "would", "make",
                          "made"}


class YaseeStopWords():
    DEFAULT_STOPWORDS = STOPWORDS.union(UCIWC_DEFAULTSTOPWORDS)



    def __init__(self, stopwords:frozenset=None, replace:bool=False):
        if (stopwords == None):
            self.stopwords = YaseeStopWords.DEFAULT_STOPWORDS
        else:
            if replace:
                self.stopwords = set(stopwords.__iter__())
            else:

                self.stopwords = YaseeStopWords.DEFAULT_STOPWORDS
                for x in stopwords:
                    self.stopwords.add(x)

    def get_stopwords(self) -> frozenset:
        return frozenset(self.stopwords.__iter__())

    def add_stopwords(self, item:str or iter=None):
        if item == None:
            return
        elif type(item) == str:
            self.stopwords.add(item)
        else:
            for x in item:
                self.stopwords.add(x)

    def __contains__(self, item):
        return item in self.stopwords

    def __iter__(self):
        return self.stopwords.__iter__()


