
import unittest
from YaseeWordCloud import YaseeWordCloud

class YaseeWordCloudTest(unittest.TestCase):
    def setUp(self):
        self.yasee_word_cloud = YaseeWordCloud("test/report.xlsx", "FQ18", "VisitNotes")

    def test_store(self):
        self.yasee_word_cloud.store("test/wordfreq.png")
        self.assertTrue(os.path.exists("test/wordfreq.png"))
