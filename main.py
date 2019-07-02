from YaseeWordCloud import YaseeWordCloud
from YaseeFreqCharts import YaseeFreqCharts
from YaseeFreqCharts import NoSearchResultsFound


def init_analysis_class(analysis_class:type) -> "type()":
    print("Where is your file?")
    target_file_path = input().strip()
    return analysis_class(path=target_file_path)


class Console():
    def __call__(self, *args, **kwargs):
        while True:
            print("Hi! You have the following options\n"
                  "a) word cloud\n"
                  "b) word freq chart\n"
                  "c) specified word(root) freq in relation to a column\n"
                  "q) quit\n", end="")
            user_prompt = input().strip().lower()
            if (user_prompt in ("seeya", "see you", "quit", "q")):
                break

            elif (user_prompt in ("a", "word cloud")):
                word_cloud:YaseeWordCloud = init_analysis_class(YaseeWordCloud)

                print("Which excel sheet to analyze?")
                target_sheet = input().strip()
                print("Which excel column inside that sheet to analyze?")
                target_column = input().strip()

                print("What would be the name of your analysis file?")
                output_path = input().strip()
                word_cloud.store(target_sheet, target_column, output_path)

            elif (user_prompt in ("b", "word freq chart")):
                word_freq_chart:YaseeFreqCharts = init_analysis_class(YaseeFreqCharts)

                print("Which excel sheet to analyze?")
                target_sheet = input().strip()
                print("Which excel column inside that sheet to analyze?")
                target_column = input().strip()

                print("What would be the name of your analysis file?")
                output_path = input().strip()
                print("How many results do you want to see?")
                result_num = int(input().strip())

                word_freq_chart.storeWordFreq(target_sheet, target_column, output_path, result_num)

            elif (user_prompt in ("c", "specified word(root) freq in relation to a column")):
                freq_chart: YaseeFreqCharts = init_analysis_class(YaseeFreqCharts)
                print("Which excel sheet to analyze?")
                target_sheet = input().strip()


                print("Which excel column inside that sheet to extract words?")
                data_column = input().strip()

                print("What is the word that you want to analyze?\n"
                      "If it is a word root, append the root by *, like pre*, re*")
                target_word = input().strip()

                is_word_root = False
                if target_word[-1] == '*':
                    is_word_root = True
                    target_word = target_word[:-1]

                print("And what column to analyze in relation to that word?")
                identity_column = input().strip()


                print("What would be the name of your analysis file?")
                output_path = input().strip()
                print("How many results do you want to see?")
                top_X = int(input().strip())

                try:
                    freq_chart.storeRelatedWordFreq(target_sheet, identity_column, data_column, target_word,
                                                output_path, top_X, is_word_root)
                except NoSearchResultsFound:
                    print(f"No search result for {target_word + '*' if is_word_root else ''}")

            else:
                print("That is not a valid command.")

            print("\n", end='')



if __name__ == "__main__":
    Console()()
