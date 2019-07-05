# This class visualizes word frequency in terms of bar charts.

from YaseeStopWords import YaseeStopWords
from YaseeAnalysisClass import YaseeAnalysisClass
from collections import defaultdict
from matplotlib import pyplot
from typing import Callable
import re

class YaseeFreqChartsError(Exception):
    pass

class NoSearchResultsFound(YaseeFreqChartsError):
    pass


def gen_verification(str_expr: str) -> Callable:
    f = lambda x: True if x == str_expr else False

    if str_expr[-1] == '*':
        def f(words: str) -> bool:
            begin_words = str_expr[:-1]
            return words[:begin_words.__len__()] == begin_words

    elif str_expr[0] == '*':
        def f(words: str) -> bool:
            end_words = str_expr[1:]
            return words[-end_words.__len__():] == end_words

    return f

class YaseeFreqCharts(YaseeAnalysisClass):
    def storeWordFreq(self, sheet_name: str, column_name: str, file_name: str, top_X: int = 10) -> None:
        entries = self.report_file.extractColumn(sheet=sheet_name, column=column_name)
        ranked_word_freq = YaseeFreqCharts.calcWordFreq(entries, self.ysw)[:top_X]
        YaseeFreqCharts.storeChart(file_name=file_name,
                                   chart_name="Frequent Words",
                                   ranked_freq=ranked_word_freq)

    def storeRelatedWordFreq(self, sheet_name: str, identity_column: str, data_column: str, target_expr: str,
                             file_name: str, top_X: int = 5) -> None:
        correlation_data = self.report_file.extractRelatedColumns(sheet_name, identity_column,
                                                                 data_column)
        ranked_freq = YaseeFreqCharts.calcRelatedWordFreq(correlation_data, target_expr.lower())[:top_X]
        YaseeFreqCharts.storeChart(file_name, f"{target_expr.upper()} "
        f"Frequency in Relation to {identity_column}", ranked_freq)



    @staticmethod
    def calcRelatedWordFreq(correlation_data:((str)), target_expr:str)  -> [tuple]:

        word_freq_dict = defaultdict(int)

        verification:Callable

        if target_expr[:6] != "regex:":
            verification = gen_verification(target_expr)
        else:
            verification = re.compile(target_expr[6:]).match


        for identity, entry in correlation_data:
            if identity != "nan":
                words = str(entry).split()
                for word in words:
                    if verification(word.lower()):
                        word_freq_dict[identity] += 1


        return sorted(word_freq_dict.items(), key=lambda x: -x[1])



    @staticmethod
    def storeChart(file_name: str, chart_name: str, ranked_freq: [tuple]) -> None:
        if len(ranked_freq) == 0:
            raise NoSearchResultsFound

        xAxis_widths = [len(word) for word, freq in ranked_freq]
        indexes = [xAxis_widths[0], ]
        for i in range(1, len(xAxis_widths)):
            indexes.append(indexes[i - 1] + xAxis_widths[i - 1] * 0.5 + xAxis_widths[i] * 0.5)

        canvas_width: int = indexes[-1] * 0.2
        canvas_length: int = canvas_width

        pyplot.figure(figsize=(canvas_width, canvas_length))
        pyplot.bar(indexes, [x[1] for x in ranked_freq], 2)
        pyplot.xticks(indexes, [x[0] for x in ranked_freq])
        pyplot.yticks(fontsize = canvas_length * 1)
        pyplot.ylabel("Frequency", fontweight='bold', fontsize=canvas_length * 1.25, horizontalalignment='center')
        pyplot.title(chart_name, fontweight='bold', color='orange', fontsize= canvas_width * 1.5,
                     horizontalalignment='center')

        for x_axis, y_axis in zip(indexes, (freq for x, freq in ranked_freq)):
            pyplot.text((lambda x, y: x - len(str(y)) * 0.5)(x_axis, y_axis),
                        y_axis + canvas_length * 0.002, str(y_axis),
                        color='blue', fontweight='bold', fontsize=canvas_width)


        pyplot.savefig(file_name)

    @staticmethod
    def calcWordFreq(entries: (str, ...), ysw: YaseeStopWords) -> [tuple]:
        word_freq_dict = defaultdict(int)
        for entry in entries:
            words = str(entry).split()
            for word in words:
                if word.lower() not in ysw:
                    word_freq_dict[word] += 1
        return sorted(word_freq_dict.items(), key=lambda x: -x[1])
