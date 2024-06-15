from collections import Counter

import jieba
import re


def main():
    with open('红楼梦.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    text = re.sub(r'[^\w\s]', '', text)
    words = jieba.lcut(text)

    # stopwords = set(open('stopwords.txt', encoding='utf-8').read().split('\n'))
    # words = [w for w in words if w not in stopwords]

    word_freq = Counter(words)
    word_freq = dict((key, value) for key, value in word_freq.items() if len(key.strip()) > 1)
    print(f"《红楼梦》总词汇量为: {len(word_freq)}")
    word_freq_sorted = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

    with open('红楼梦词频统计.txt', 'w', encoding='utf-8') as f:
        f.write(f"词汇,词频\n")
        for w, freq in word_freq_sorted:
            f.write(f"{w},{freq}\n")

    print("词频统计结果已保存到 红楼梦词频统计.txt")


if __name__ == '__main__':
    main()
