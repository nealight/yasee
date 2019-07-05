# This class visualizes word frequency in terms of a word cloud.

from wordcloud import WordCloud
from matplotlib import pyplot
from YaseeStopWords import YaseeStopWords
from UCIWC_DEFAULTSTOPWORDS import UCIWC_DEFAULTSTOPWORDS
from YaseeAnalysisClass import YaseeAnalysisClass

class YaseeWordCloud(YaseeAnalysisClass):
    def __init__(self, path:str, stopwords:YaseeStopWords or frozenset=None):

        if stopwords == None:
            YaseeAnalysisClass.__init__(self, path, YaseeStopWords(UCIWC_DEFAULTSTOPWORDS, True))
        elif type(stopwords) == frozenset:
            YaseeAnalysisClass.__init__(self, path, YaseeStopWords(UCIWC_DEFAULTSTOPWORDS, True))
            self._ysw.addStopwords(stopwords)
        else:
            YaseeAnalysisClass.__init__(self, path, stopwords)




    def store(self, sheet:str, column:str, name:str) -> None:
        entries = self._report_file.extractColumn(sheet=sheet, column=column)

        text = '\n'.join(entry.lower() for entry in entries).lower()

        for word in self._ysw:
            text = text.replace(word, "")

        word_cloud = WordCloud(max_font_size=50, background_color="white", max_words=50).generate(text)
        pyplot.figure()
        pyplot.imshow(word_cloud, interpolation="bilinear")
        pyplot.axis("off")
        pyplot.title("Word Cloud of Frequent Words", fontweight='bold', color='orange', fontsize=12,
                     horizontalalignment='center')

        pyplot.savefig(name)