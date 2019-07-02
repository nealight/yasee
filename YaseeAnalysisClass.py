from YaseeStopWords import YaseeStopWords
from YaseeReportFile import YaseeReportFile

class YaseeAnalysisClass():
    def __init__(self, path: str, stopwords: YaseeStopWords = None):
        if stopwords == None:
            self.ysw = YaseeStopWords()
        else:
            self.ysw = stopwords

        self.report_file = YaseeReportFile(path)

    def addStopWords(self, additional_words: str or iter):
        self.ysw.addStopwords(additional_words)