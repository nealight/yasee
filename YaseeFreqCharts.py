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
        entries = self._report_file.extractColumn(sheet=sheet_name, column=column_name)
        ranked_word_freq = YaseeFreqCharts.calcWordFreq(entries, self._ysw)[:top_X]
        YaseeFreqCharts.storeChart(file_name=file_name,
                                   chart_name="Frequent Words",
                                   ranked_freq=ranked_word_freq,
                                   categories="Words")

    def storeRelatedWordFreq(self, sheet_name: str, identity_column: str, data_column: str, target_expr: str,
                             file_name: str, top_X: int = 5, is_related_freq: bool = False) -> None:
        correlation_data = self._report_file.extractRelatedColumns(sheet_name, identity_column,
                                                                   data_column)
        ranked_freq = YaseeFreqCharts.calcRelatedWordFreq(correlation_data, target_expr.lower(), is_related_freq)[:top_X]



        YaseeFreqCharts.storeChart(file_name, f"\"{target_expr.upper()}\" "
        f"{'Relative Frequency(%)' if is_related_freq else 'Absolute Frequency'} "
        f"in Relation to {identity_column}", ranked_freq, identity_column)

    @staticmethod
    def calcRelatedWordFreq(correlation_data: ((str)), target_expr: str, is_relative_freq: bool = False) -> [tuple]:

        word_freq_dict = defaultdict(int)
        identity_dict = defaultdict(int)
        relative_word_freq_dict = defaultdict(int)

        verification: Callable

        if target_expr[:6] != "regex:":
            verification = gen_verification(target_expr)
        else:
            verification = re.compile(target_expr[6:]).match

        for identity, entry in correlation_data:
            if identity != "nan":
                identity_dict[identity] += 1
                words = str(entry).split()
                for word in words:
                    if verification(word.lower()):
                        word_freq_dict[identity] += 1

        for key, value in word_freq_dict.items():
            relative_word_freq_dict[key] = value / identity_dict[key] * 100

        if is_relative_freq:
            return sorted(relative_word_freq_dict.items(), key=lambda x: -x[1])
        else:
            return sorted(word_freq_dict.items(), key=lambda x: -x[1])

    @staticmethod
    def storeChart(file_name: str, chart_name: str, ranked_freq: [tuple], categories:str) -> None:
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
        pyplot.xticks(indexes,
                      [(lambda x: (x[:17] + "...") if (len(x) >= 20) else (x))(x[0]) for x in ranked_freq],
                      fontsize=canvas_width * 0.7)
        pyplot.yticks(fontsize=canvas_length * 1)
        pyplot.xlabel(categories, fontweight='bold', fontsize=canvas_width * 1.25, horizontalalignment='center')
        pyplot.ylabel("Frequency", fontweight='bold', fontsize=canvas_length * 1.25, horizontalalignment='center')

        pyplot.title(chart_name, fontweight='bold', color='orange', fontsize=canvas_width * 1.5,
                     horizontalalignment='center')


        for x_axis, y_axis in zip(indexes, (freq for x, freq in ranked_freq)):
            pyplot.text((lambda x, y: x - len(str(y)[:5]) * 0.5 + (0.3 if '.' in str(y) else 0))(x_axis, y_axis),
                        y_axis, str(y_axis)[:5],
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
