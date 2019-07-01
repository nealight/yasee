# UnitTest Module

import unittest
from ReportFile import ReportFile


class ReportFileTest(unittest.TestCase):
    def setUp(self):
        self.report_file = ReportFile("test/report.xlsx")

    def test_canInstantiate(self):
        pass

    def test_getitem(self):
        self.assertEqual("Cours", str(self.report_file["FQ18"].iloc[0])[:5])

    def test_extractColumn(self):
        self.assertEqual("Student had a number of supplemental essays - wanted to know how much cross over she should "
                         "have between PS, SOP, and supplementals.",
                         self.report_file.extractColumn("FQ18", "VisitNotes")[0])

    def test_extractRelatedColumns(self):
        self.assertEqual(("BIOLOGICAL SCIENCES", "Student had a number of supplemental essays - wanted to know how "
                          "much cross over she should have between PS, SOP, and supplementals."),
                         self.report_file.extractRelatedColumns("FQ18", "MajorID1", "VisitNotes")[0])
