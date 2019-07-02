from YaseeStopWords import YaseeStopWords
from YaseeAnalysisClass import YaseeAnalysisClass
from collections import defaultdict
from matplotlib import pyplot


class YaseeFreqCharts(YaseeAnalysisClass):
    def storeWordFreq(self, sheet_name:str, column_name:str, file_name:str, top_X:int=10) -> None:
        entries = self.report_file.extractColumn(sheet=sheet_name, column=column_name)
        ranked_word_freq = YaseeFreqCharts.calcWordFreq(entries, self.ysw)[:top_X]
        YaseeFreqCharts.storeChart(file_name=file_name,
                                   chart_name="Frequent Words",
                                   ranked_freq=ranked_word_freq)


    @staticmethod
    def storeChart(file_name:str, chart_name:str, ranked_freq: [tuple, ...]) -> None:
        xAxis_widths = [len(word) for word, freq in ranked_freq]
        indexes = [xAxis_widths[0], ]
        for i in range(1, len(xAxis_widths)):
            indexes.append(indexes[i - 1] + xAxis_widths[i - 1] * 0.5 + xAxis_widths[i] * 0.5)

        canvas_width: int = indexes[-1] * 0.2
        canvas_length: int = canvas_width

        pyplot.figure(figsize=(canvas_width, canvas_length))
        pyplot.bar(indexes, [x[1] for x in ranked_freq], 2)
        pyplot.xticks(indexes, [x[0] for x in ranked_freq])
        pyplot.xlabel(chart_name, fontweight='bold', color='orange', fontsize='15', horizontalalignment='center')

        pyplot.savefig(file_name)


    @staticmethod
    def calcWordFreq(entries: (str, ...), ysw: YaseeStopWords) -> [tuple, ...]:
        word_freq_dict = defaultdict(int)
        for entry in entries:
            words = str(entry).split()
            for word in words:
                if word.lower() not in ysw:
                    word_freq_dict[word] += 1
        ranked_word_freq = sorted(word_freq_dict.items(), key=lambda x: -x[1])
        return ranked_word_freq

    @staticmethod
    def calcRelatedWordFreq():
        pass