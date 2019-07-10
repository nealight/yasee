# Local Console

from YaseeWordCloud import YaseeWordCloud
from YaseeFreqCharts import YaseeFreqCharts
from YaseeFreqCharts import NoSearchResultsFound
from YaseeAnalysisClass import YaseeAnalysisClass



def init_analysis_class(analysis_class:type) -> "type()":
    print("Where is your file?")
    target_file_path = input().strip()

    print("Enter any additional stopwords you want to implement.")
    return analysis_class(path=target_file_path, stopwords=frozenset(x for x in input().strip().split()))


class Console():
    def __call__(self, *args, **kwargs):
        while True:
            print("Hi! You have the following options\n"
                  "a) word cloud\n"
                  "b) word freq chart\n"
                  "c) specified expression freq in relation to a column\n"
                  "q) quit\n", end="")
            user_prompt = input().strip().lower()

            ### Terminate Console
            if (user_prompt in ("seeya", "see you", "quit", "q")):
                break
            ###

            if (user_prompt in ("a", "word cloud")):
                analysis: YaseeWordCloud= init_analysis_class(YaseeWordCloud)

                print("Which excel sheet to analyze?")
                print(f"You have the following options:\n"
                      f"{analysis.getReportFile().getSheetNames()}")
                target_sheet = input().strip()
                print("Which excel column inside that sheet to analyze?")
                print(f"You have the following options:\n"
                      f"{analysis.getReportFile().getColumnNames(target_sheet)}")
                target_column = input().strip()

                print("What would be the name of your analysis file?")
                output_path = input().strip()
                analysis.store(target_sheet, target_column, output_path)

            elif (user_prompt in ("b", "word freq chart")):
                analysis:YaseeFreqCharts = init_analysis_class(YaseeFreqCharts)

                print("Which excel sheet to analyze?")
                print(f"You have the following options:\n"
                      f"{analysis.getReportFile().getSheetNames()}")
                target_sheet = input().strip()
                print("Which excel column inside that sheet to analyze?")
                print(f"You have the following options:\n"
                      f"{analysis.getReportFile().getColumnNames(target_sheet)}")
                target_column = input().strip()

                print("What would be the name of your analysis file?")
                output_path = input().strip()
                print("How many results do you want to see?")
                result_num = int(input().strip())

                analysis.storeWordFreq(target_sheet, target_column, output_path, result_num)

            elif (user_prompt in ("c", )):
                analysis:YaseeFreqCharts = init_analysis_class(YaseeFreqCharts)
                print("Which excel sheet to analyze?")
                print(f"You have the following options:\n"
                      f"{analysis.getReportFile().getSheetNames()}")
                target_sheet = input().strip()


                print("Which excel column inside that sheet to extract words?")
                print(f"You have the following options:\n"
                      f"{analysis.getReportFile().getColumnNames(target_sheet)}")
                data_column = input().strip()
                print("And what column to analyze in relation to the previously chosen column?")
                print(f"You have the following options:\n"
                      f"{analysis.getReportFile().getColumnNames(target_sheet)}")
                identity_column = input().strip()


                print("What is your specified expression?\n"
                      "Examples: pre*, *ation, research, ...")
                target_expression = input().strip()


                print("What would be the name of your analysis file?")
                output_path = input().strip()
                print("How many results do you want to see?")
                top_X = int(input().strip())

                try:
                    analysis.storeRelatedWordFreq(target_sheet, identity_column, data_column, target_expression,
                                                  output_path + " Absolute", top_X)
                except NoSearchResultsFound:
                    print(f"\nNo search result found for {target_expression}!\n")

            else:
                print("That is not a valid command.")

            print("\n", end='')



if __name__ == "__main__":
    Console()()
