

"""
import pandas
ser = pandas.Series(["soo", 200], ["Nancy", "Boo"])
ser = ser * 2
print(ser.__str__().split())


d = {"one": pandas.Series([100., 200.], ["apple", "ball"]),
     "two": pandas.Series([200., 400.], ["apple", "ball"])}

df = pandas.DataFrame(d)
print(df)

"""
"""
import pandas
intermediate = pandas.ExcelFile("../reports/report.xlsx")
file = intermediate.parse(intermediate.sheet_names[0])

columns = file
"""

import YaseeReportFile
from collections import defaultdict
from wordcloud import WordCloud
from matplotlib import pyplot
import numpy
from YaseeStopWords import YaseeStopWords


ysw = YaseeStopWords()

words_toStrip = {
    "nan", "to", "the", "and", "a", "of", "her", "we", "she", "for", "about", "him", "his", "want",
    "wanted", "so", "student", "in", "on", "had", "an", "some", "as", "be", "what", "through", "make",
    "with", "not", "at", "is", "it", "from", "also", "out", "would", "which", "where", "for", "those",
    "this", "how", "that", "was", "he", "could", "them"
}

report_file = YaseeReportFile.YaseeReportFile("../test/report.xlsx")
entries = report_file.extractColumn("WQ19", "VisitNotes")

phrase_freq_dict = defaultdict(int)
word_freq_dict = defaultdict(int)
for entry in entries:
    words = str(entry).split()
    for word in words:
        if word.lower() not in ysw:
            word_freq_dict[word] += 1
    for index in range(len(words) - 1):
        phrase = words[index] + '_' + words[index + 1]
        phrase_freq_dict[phrase] += 1

ranked_phrase_freq = sorted(phrase_freq_dict.items(), key=lambda x: -x[1])
ranked_word_freq = sorted(word_freq_dict.items(), key=lambda x: -x[1])

print(ranked_phrase_freq)
print(ranked_word_freq)


"""
word_cloud = WordCloud(max_font_size=50, background_color="white", max_words=50).generate(text)
pyplot.figure()
pyplot.imshow(word_cloud, interpolation="bilinear")
pyplot.axis("off")

pyplot.savefig("word frequency.png")
"""

top_X = 20
widths = [len(word) for word, freq in ranked_word_freq[:top_X]]
indexes = [widths[0],]
for i in range(1, len(widths)):
    indexes.append(indexes[i-1] + widths[i-1] * 0.5 + widths[i] * 0.5)
print(indexes)

pyplot.figure(figsize=(indexes[-1] * 0.1, 5))
pyplot.bar(indexes, [x[1] for x in ranked_word_freq[:top_X]], 2)
pyplot.xticks(indexes, [x[0] for x in ranked_word_freq[:top_X]])
pyplot.xlabel('Frequent words', fontweight='bold', color = 'orange', fontsize='15', horizontalalignment='center')

pyplot.show()