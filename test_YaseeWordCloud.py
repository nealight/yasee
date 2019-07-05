import unittest
from YaseeWordCloud import YaseeWordCloud
import os

class YaseeWordCloudTest(unittest.TestCase):
    def setUp(self):
        self.yasee_word_cloud = YaseeWordCloud("test/report.xlsx")

    def test_store(self):
        self.yasee_word_cloud.store("FQ18", "VisitNotes", "test/WordCloud.png")
        self.assertTrue(os.path.exists("test/WordCloud.png"))

