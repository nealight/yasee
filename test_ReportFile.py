import unittest

from ReportFile import ReportFile


class ReportFileTest(unittest.TestCase):
    def setUp(self):
        self.report_file = ReportFile("reports/report.xlsx")

    def test_canInstantiate(self):
        pass

    def test_getitem(self):
        self.assertEqual("Cours", str(self.report_file["FQ18"].iloc[0])[:5])




