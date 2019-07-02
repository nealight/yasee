from wordcloud import WordCloud
from matplotlib import pyplot
from YaseeStopWords import YaseeStopWords
from UCIWC_DEFAULTSTOPWORDS import UCIWC_DEFAULTSTOPWORDS
from YaseeAnalysisClass import YaseeAnalysisClass
import re

class YaseeWordCloud(YaseeAnalysisClass):
    def __init__(self, path:str, stopwords:YaseeStopWords=None):

        if stopwords == None:
            YaseeAnalysisClass.__init__(self, path, YaseeStopWords(UCIWC_DEFAULTSTOPWORDS, True))
        else:
            YaseeAnalysisClass.__init__(self, path, stopwords)




    def store(self, sheet:str, column:str, name:str) -> None:
        entries = self.report_file.extractColumn(sheet=sheet, column=column)

        text = '\n'.join(entry.lower() for entry in entries).lower()

        for word in self.ysw:
            text = text.replace(word, "")

        word_cloud = WordCloud(max_font_size=50, background_color="white", max_words=50).generate(text)
        pyplot.figure()
        pyplot.imshow(word_cloud, interpolation="bilinear")
        pyplot.axis("off")
        pyplot.savefig(name)