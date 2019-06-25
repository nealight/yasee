

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

import ReportFile
from collections import defaultdict

words_toStrip = {
    "nan", "to", "the", "and", "a", "of", "her", "we", "she", "for", "about", "him", "his", "want",
    "wanted", "so", "student", "in", "on", "had", "an", "some", "as", "be", "what", "through", "make",
    "with", "not", "at", "is", "it", "from", "also", "out", "would", "which", "where", "for", "those",
    "this", "how", "that", "was", "he", "could", "them"
}

report_file = ReportFile.ReportFile("../../reports/report.xlsx")
entries = report_file.get_visitNotes(report_file.get_sheet_names()[0])

phrase_freq_dict = defaultdict(int)
word_freq_dict = defaultdict(int)
for entry in entries:
    words = str(entry).split()
    for word in words:
        if word.lower() not in words_toStrip:
            word_freq_dict[word] += 1
    for index in range(len(words) - 1):
        phrase = words[index] + ' ' + words[index + 1]
        phrase_freq_dict[phrase] += 1

ranked_phrase_freq = sorted(phrase_freq_dict.items(), key=lambda x: -x[1])
ranked_word_freq = sorted(word_freq_dict.items(), key=lambda x: -x[1])

print(ranked_phrase_freq)
print(ranked_word_freq)