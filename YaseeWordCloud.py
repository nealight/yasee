import ReportFile
from wordcloud import WordCloud
from matplotlib import pyplot
from YaseeStopWords import YaseeStopWords
from UCIWC_DEFAULTSTOPWORDS import UCIWC_DEFAULTSTOPWORDS
import re

class YaseeWordCloud:

    def __init__(self, path:str, stopwords:YaseeStopWords=None):

        if stopwords == None:
            self.stopwords = YaseeStopWords(UCIWC_DEFAULTSTOPWORDS, True)
        else:
            self.stopwords = stopwords

        self.report_file =  ReportFile.ReportFile(path)



    def store(self, sheet:str, column:str, name:str) -> None:
        entries = self.report_file.extractColumn(sheet=sheet, column=column)

        text = '\n'.join(entry.lower() for entry in entries).lower()

        for word in self.stopwords:
            text = text.replace(word, "")

        word_cloud = WordCloud(max_font_size=50, background_color="white", max_words=50).generate(text)
        pyplot.figure()
        pyplot.imshow(word_cloud, interpolation="bilinear")
        pyplot.axis("off")
        pyplot.savefig(name)