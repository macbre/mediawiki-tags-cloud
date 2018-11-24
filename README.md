# mediawiki-tags-cloud
Generates tags cloud using MediaWiki XML content dump and [wordcloud module](https://github.com/amueller/word_cloud).

### Install

```
pip install pipenv
pipenv install
```


### Example

Generate tags cloud for []The Muppet Wiki](http://muppet.wikia.com):

```
python frequencies_from_dump.py  | tee muppet.json
python cloud_from_frequencies.py muppet.json
```

#### Result

