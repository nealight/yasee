# A base class for all classes that perform analysis and visualization.

from YaseeStopWords import YaseeStopWords
from YaseeReportFile import YaseeReportFile

class YaseeAnalysisClass():
    def __init__(self, path: str, stopwords: YaseeStopWords or frozenset = None):
        if stopwords == None:
            self.ysw = YaseeStopWords()
        elif type(stopwords) == YaseeStopWords:
            self.ysw = stopwords
        elif type(stopwords) == frozenset:
            self.ysw = YaseeStopWords(stopwords)

        self.report_file = YaseeReportFile(path)

    def addStopWords(self, additional_words: str or iter):
        self.ysw.addStopwords(additional_words)

    def getStopWords(self) -> frozenset:
        return self.ysw.getStopwords()