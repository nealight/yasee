import unittest
from YaseeWordCloud import YaseeWordCloud
import os

class YaseeWordCloudTest(unittest.TestCase):
    def setUp(self):
        self.yasee_word_cloud = YaseeWordCloud("test/report.xlsx", "FQ18", "VisitNotes")

    def test_store(self):
        self.yasee_word_cloud.store("test/wordcloud.png")
        self.assertTrue(os.path.exists("test/wordcloud.png"))

