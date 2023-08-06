from prophets import Isaiah
import sys
from pprint import pprint

if __name__ == "__main__":
    print(f"Abraham Version: {open('version').read().strip()}")
    darthvader = Isaiah(
        news_source="newsapi",
        api_key="3530e04f04034a85a0ebf4d925c83c69",
        splitting=False,
    )  # splitting means that it recursively splits a large text into sentences and analyzes each individually

    args = [sys.argv[1:]] if sys.argv[1:] else ["tesla"]  # default args

    scores = darthvader.sentiment(
        *args,
        window=3,  # how many days back from up_to to get news from
    )  # latest date to get news from

    pprint(scores)