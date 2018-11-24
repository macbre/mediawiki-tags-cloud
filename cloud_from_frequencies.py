"""
Generates tag cloud image from frequencies json file

Usage:

    python cloud_from_frequencies.py muppet.json
    cat muppet.json | python cloud_from_frequencies.py -

"""
import fileinput
import logging
import json

# @see https://github.com/amueller/word_cloud/blob/master/examples/masked.py
# import numpy as np
# from PIL import Image
from wordcloud import WordCloud

logging.basicConfig(level=logging.INFO)


def generate_cloud(frequencies, width=900, height=450):
    """
    :type frequencies dict 
    :type width int
    :type height int
    """
    logger = logging.getLogger('get_frequencies')
    logger.info('Reading %d words from frequencies json' % len(frequencies))

    # @see http://amueller.github.io/word_cloud/generated/wordcloud.WordCloud.html#wordcloud.WordCloud
    wc = WordCloud(mode='RGBA', background_color='white', width=width, height=height,
                   max_words=1000, relative_scaling=0.2, prefer_horizontal=0.5)

    wc.generate_from_frequencies(frequencies)

    wc.to_file('cloud.png')


if __name__ == "__main__":
    buf = ''

    for line in fileinput.input():
        buf += line

    # map from [word, count] to word: count key-value dictionary
    freq = dict()

    for item in json.loads(buf):
        freq[item[0]] = int(item[1])

    generate_cloud(freq)
