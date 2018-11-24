"""
Generates frequencies json file using provided dump
"""
import json
import logging

from collections import Counter

from mediawiki_dump.dumps import WikiaDump, WikipediaDump
from mediawiki_dump.reader import DumpReaderArticles
from mediawiki_dump.tokenizer import clean, tokenize

from stop_words import get_stop_words

logging.basicConfig(level=logging.INFO)


def get_frequencies(wikia_name, limit=100, min_length=3):
    """
    :type wikia_name str|None
    :type limit int
    :type min_length int
    :rtype: Counter
    """
    logger = logging.getLogger('get_frequencies')
    dump = WikiaDump(wiki=wikia_name)

    # read the dump
    stats = Counter()
    reader = DumpReaderArticles()
    pages = reader.read(dump)

    for page in pages:
        # get stopwords
        stop_words = get_stop_words(reader.get_dump_language())

        tokens = tokenize(clean(page.content.lower()))
        tokens = [
            token for token in tokens
            if len(token) >= min_length and token not in stop_words
        ]

        stats.update(tokens)

    logger.info('Tokens counted: %d' % len(stats))

    return stats.most_common(limit)


if __name__ == "__main__":
    # freq = get_frequencies(wikia_name='plnordycka', min_length=5)
    freq = get_frequencies(wikia_name='muppet', min_length=4)

    print(json.dumps(freq))
