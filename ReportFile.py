""" Module for the ReportFile class """

import pandas

class ReportFile:
    def __init__(self, file_path: str):
        self.file = pandas.ExcelFile(file_path)

    def print_sheet_names(self):
        print(self.file.sheet_names)



