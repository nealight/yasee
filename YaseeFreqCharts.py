# This class visualizes word frequency in terms of bar charts.

from YaseeStopWords import YaseeStopWords
from YaseeAnalysisClass import YaseeAnalysisClass
from collections import defaultdict
from matplotlib import pyplot

class YaseeFreqChartsError(Exception):
    pass

class NoSearchResultsFound(YaseeFreqChartsError):
    pass


class YaseeFreqCharts(YaseeAnalysisClass):
    def storeWordFreq(self, sheet_name: str, column_name: str, file_name: str, top_X: int = 10) -> None:
        entries = self.report_file.extractColumn(sheet=sheet_name, column=column_name)
        ranked_word_freq = YaseeFreqCharts.calcWordFreq(entries, self.ysw)[:top_X]
        YaseeFreqCharts.storeChart(file_name=file_name,
                                   chart_name="Frequent Words",
                                   ranked_freq=ranked_word_freq)

    def storeRelatedWordFreq(self, sheet_name: str, identity_column: str, data_column: str, target_word: str,
                             file_name: str, top_X: int = 5, is_word_root: bool = False) -> None:
        correlation_data = self.report_file.extractRelatedColumns(sheet_name, identity_column,
                                                                 data_column)
        ranked_freq = YaseeFreqCharts.calcRelatedWordFreq(correlation_data, target_word.lower(), is_word_root)[:top_X]
        YaseeFreqCharts.storeChart(file_name, f"{target_word.upper() + ('*' if is_word_root else '')} "
        f"Frequency in Relation to {identity_column}", ranked_freq)



    @staticmethod
    def calcRelatedWordFreq(correlation_data:((str, ...), ...), target_word:str, is_word_root: bool = False) \
        -> [tuple, ...]:

        word_freq_dict = defaultdict(int)

        if is_word_root:
            for identity, entry in correlation_data:
                if identity != "nan":
                    words = str(entry).split()
                    for word in words:
                        if word.lower()[:len(target_word)] == target_word:
                            word_freq_dict[identity] += 1

        else:
            for identity, entry in correlation_data:
                if identity != "nan":
                    words = str(entry).split()
                    for word in words:
                        if word.lower() == target_word:
                            word_freq_dict[identity] += 1


        return sorted(word_freq_dict.items(), key=lambda x: -x[1])



    @staticmethod
    def storeChart(file_name: str, chart_name: str, ranked_freq: [tuple, ...]) -> None:
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
        pyplot.ylabel("Frequency", fontweight='bold', fontsize=canvas_length, horizontalalignment='center')
        pyplot.title(chart_name, fontweight='bold', color='orange', fontsize= canvas_width * 1.7,
                     horizontalalignment='center')

        for x_axis, y_axis in zip(indexes, (freq for x, freq in ranked_freq)):
            pyplot.text((lambda x, y: x - len(str(y)) * 0.5)(x_axis, y_axis),
                        y_axis + canvas_length * 0.002, str(y_axis),
                        color='blue', fontweight='bold', fontsize=canvas_width)


        pyplot.savefig(file_name)

    @staticmethod
    def calcWordFreq(entries: (str, ...), ysw: YaseeStopWords) -> [tuple, ...]:
        word_freq_dict = defaultdict(int)
        for entry in entries:
            words = str(entry).split()
            for word in words:
                if word.lower() not in ysw:
                    word_freq_dict[word] += 1
        return sorted(word_freq_dict.items(), key=lambda x: -x[1])
