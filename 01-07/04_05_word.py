import re

from wordcloud import WordCloud, ImageColorGenerator
import jieba
from collections import Counter
from PIL import Image
import numpy as np


def main():
    image_path = "04_05__chrome.png"
    font_path = "04_05__AaWoYouDianFang-2.ttf"
    output_path = "04_05__output_wordcloud.png"
    text_path = '04_05__text.txt'
    stopwords = ["的", "了", "是", "在", "和", "与", "或", "，", "。", "、"]

    with open(text_path, 'r', encoding='utf-8') as f:
        text = f.read()

    text = re.sub(r'[^\w\s]', '', text)
    words = jieba.lcut(text)
    filtered_words = [word for word in words if word.strip() and word not in stopwords]
    word_counts = Counter(filtered_words)

    mask_image = Image.open(image_path).convert("RGBA")
    mask = np.array(mask_image)
    mask = 255 - mask[:, :, 3]

    wordcloud = WordCloud(
        font_path=font_path,
        mask=mask,
        background_color="white",
        max_words=200
    ).generate_from_frequencies(word_counts)

    image_colors = ImageColorGenerator(np.array(mask_image))
    wordcloud.recolor(color_func=image_colors)

    wordcloud.to_file(output_path)
