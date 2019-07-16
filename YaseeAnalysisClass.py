# A base class for all classes that perform analysis and visualization.

from YaseeStopWords import YaseeStopWords
from YaseeReportFile import YaseeReportFile

class YaseeAnalysisClass():
    combine_as_lines = lambda x, y: f"{x}\n{y}"
    combine_as_entry = lambda x, y: f"{x}: {y}"

    def __init__(self, path: str, stopwords: YaseeStopWords or frozenset = None):
        if stopwords == None:
            self._ysw = YaseeStopWords()
        elif type(stopwords) == YaseeStopWords:
            self._ysw = stopwords
        elif type(stopwords) == frozenset:
            self._ysw = YaseeStopWords(stopwords)

        self._report_file = YaseeReportFile(path)


    def addStopWords(self, additional_words: str or iter):
        self._ysw.addStopwords(additional_words)

    def getStopWords(self) -> frozenset:
        return self._ysw.getStopwords()

    def getReportFile(self) -> YaseeReportFile:
        return self._report_file