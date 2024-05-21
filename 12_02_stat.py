import re
from collections import Counter


def main():
    with open('Pumas.txt', 'r', encoding='utf-8') as file:
        content = file.read()

    paragraphs = re.split(r'\n+', content.strip())
    num_paragraphs = len(paragraphs)

    sentences = re.split(r'[.!?]', content)
    sentences = [s for s in sentences if s.strip()]
    num_sentences = len(sentences)

    words = re.findall(r'\b\w+\b', content.lower())
    num_words = len(words)

    word_freq = Counter(words)
    most_common_words = word_freq.most_common(10)

    print(f"段落数: {num_paragraphs}")
    print(f"句数: {num_sentences}")
    print(f"单词数: {num_words}")
    print("\n前 10 个单词频率:")
    for word, freq in most_common_words:
        print(f"{word}: {freq}")


if __name__ == "__main__":
    main()
