from YaseeWordCloud import YaseeWordCloud
from YaseeFreqCharts import YaseeFreqCharts



def init_analysis_class(analysis_class:type) -> "type()":
    print("Where is your file?")
    target_file_path = input().strip()
    print("Which excel sheet to analyze?")
    target_sheet = input().strip()
    print("Which excel column inside that sheet to analyze?")
    target_column = input().strip()

    return analysis_class(path=target_file_path, sheet=target_sheet, column=target_column)


class Console():
    def __call__(self, *args, **kwargs):
        while True:
            user_prompt = input().strip().lower()
            if (user_prompt in frozenset(("seeya", "quit", "see you"))):
                break

            if (user_prompt == "word cloud"):
                word_cloud:YaseeWordCloud = init_analysis_class(YaseeWordCloud)

                print("What would be the name of your analysis file?")
                output_path = input().strip()
                word_cloud.store(output_path)

            if (user_prompt == "word freq chart"):
                word_freq_chart:YaseeFreqCharts = init_analysis_class(YaseeFreqCharts)

                print("What would be the name of your analysis file?")
                output_path = input().strip()
                print("How many results do you want to see?")
                result_num = int(input().strip())

                word_freq_chart.storeWordFreq(output_path, result_num)




if __name__ == "__main__":
    Console()()
