""" Module for the ReportFile class """

import pandas

class ReportFile:
    def __init__(self, file_path: str):
        inter_file = pandas.ExcelFile(file_path)

        try:

            self.sheets = dict()
            for name in inter_file.sheet_names:
                self.sheets[name] = inter_file.parse(name)

        finally:
            inter_file.close()

    def __getitem__(self, item):
        return self.sheets[item]

