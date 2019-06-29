import ReportFile
from wordcloud import WordCloud
from matplotlib import pyplot
from YaseeStopWords import YaseeStopWords
from UCIWC_DEFAULTSTOPWORDS import UCIWC_DEFAULTSTOPWORDS
import re

class YaseeWordCloud:
    #static variable
    DEFAULT_YSW = YaseeStopWords(UCIWC_DEFAULTSTOPWORDS, True)


    def __init__(self, path:str, sheet:str, column:str, stopwords:YaseeStopWords=None):

        if stopwords == None:
            stopwords = YaseeWordCloud.DEFAULT_YSW


        report_file =  ReportFile.ReportFile(path)
        entries = report_file.extract_column(sheet=sheet, column=column)

        self.text = '\n'.join(entry.lower() for entry in entries).lower()

        for word in stopwords:
           self.text = self.text.replace(word, "")


    def store(self, name:str) -> None:
        word_cloud = WordCloud(max_font_size=50, background_color="white", max_words=50).generate(self.text)
        pyplot.figure()
        pyplot.imshow(word_cloud, interpolation="bilinear")
        pyplot.axis("off")
        pyplot.savefig(name)