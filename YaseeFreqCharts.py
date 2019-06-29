from typing import Tuple

from YaseeStopWords import YaseeStopWords
from ReportFile import ReportFile
from collections import defaultdict
from matplotlib import pyplot


def calcWordFreq(entries: Tuple[str, ...], ysw:YaseeStopWords) -> [tuple, ...]:
    word_freq_dict = defaultdict(int)
    for entry in entries:
        words = str(entry).split()
        for word in words:
            if word.lower() not in ysw:
                word_freq_dict[word] += 1
    ranked_word_freq = sorted(word_freq_dict.items(), key=lambda x: -x[1])
    return ranked_word_freq

class YaseeFreqCharts():
    def __init__(self, path: str, sheet: str, column: str, stopwords: YaseeStopWords = None):
        if stopwords == None:
            self.ysw = YaseeStopWords()
        else:
            self.ysw = stopwords

        report_file = ReportFile(path)
        self.entries = report_file.extract_column(sheet=sheet, column=column)

    def addStopWords(self, additional_words: str or iter):
        self.ysw.add_stopwords(additional_words)


    def storeWordFreq(self, name:str, top_X:int=10) -> None:
        ranked_word_freq = calcWordFreq(self.entries, self.ysw)
        xAxis_widths = [len(word) for word, freq in ranked_word_freq[:top_X]]
        indexes = [xAxis_widths[0], ]
        for i in range(1, len(xAxis_widths)):
            indexes.append(indexes[i - 1] + xAxis_widths[i - 1] * 0.5 + xAxis_widths[i] * 0.5)

        canvas_width:int = indexes[-1] * 0.2
        canvas_length:int = canvas_width

        pyplot.figure(figsize=(canvas_width, canvas_length))
        pyplot.bar(indexes, [x[1] for x in ranked_word_freq[:top_X]], 2)
        pyplot.xticks(indexes, [x[0] for x in ranked_word_freq[:top_X]])
        pyplot.xlabel('Frequent Words', fontweight='bold', color='orange', fontsize='15', horizontalalignment='center')

        pyplot.savefig(name)




