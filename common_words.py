from collections import Counter
import re
import argparse


def load_data(file_path="king.txt"):
    with open(file_path, "r", encoding='utf-8', newline='') as file_obj:
        text = file_obj.read()
    return text


def createParser():
    parser = argparse.ArgumentParser(description="serching_most_common_words")
    parser.add_argument("data_file_path", type=str, nargs="?")

    return parser


if __name__ == '__main__':

    parser = createParser()
    namespace = parser.parse_args()
    text = load_data(file_path=namespace.data_file_path)
    print(namespace)

    word = re.findall(r"\w+", text)
    most_common_words = Counter(word).most_common(50)
    print(most_common_words)
