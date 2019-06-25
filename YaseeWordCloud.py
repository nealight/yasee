import ReportFile
from wordcloud import WordCloud
from matplotlib import pyplot

WORDS_TO_STRIP = frozenset({
    "student", "nan", "to", "the", "and", "a", "of", "her", "we", "she", "for", "about", "him", "his",
    "wanted", "so", "in", "on", "had", "an", "some", "as", "be", "what", "through", "make",
    "with", "not", "at", "is", "it", "from", "also", "out", "would", "which", "where", "for", "those",
    "this", "how", "that", "was", "he", "could", "them", "want"})

class YaseeWordCloud:
    def __init__(self, path:str, sheet:str, column:str, words_toStrip:dict=WORDS_TO_STRIP):
        report_file =  ReportFile.ReportFile(path)
        entries = report_file.extract_column(sheet=sheet, column=column)
        self.text = '\n'.join(str(entry).lower() for entry in entries if str(entry).lower() not in words_toStrip)

    def display_wordcloud(self) -> None:
        word_cloud = WordCloud(max_font_size=50, background_color="white", max_words=50).generate(self.text)
        pyplot.figure()
        pyplot.imshow(word_cloud, interpolation="bilinear")
        pyplot.axis("off")
        pyplot.show()

    def store_wordcloud(self,name:str) -> None:
        word_cloud = WordCloud(max_font_size=50, background_color="white", max_words=50).generate(self.text)
        pyplot.figure()
        pyplot.imshow(word_cloud, interpolation="bilinear")
        pyplot.axis("off")
        pyplot.savefig(name)