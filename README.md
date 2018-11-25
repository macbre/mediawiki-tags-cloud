# mediawiki-tags-cloud
Generates tags cloud using [MediaWiki XML content dump](https://github.com/macbre/mediawiki-dump) and [wordcloud module](https://github.com/amueller/word_cloud).

### Gallery

#### [The Muppet Wiki](http://muppet.wikia.com)
![](https://github.com/macbre/mediawiki-tags-cloud/raw/master/cloud.png)

#### [Poznańska Wiki](http://poznan.wikia.com)
![](https://github.com/macbre/mediawiki-tags-cloud/raw/master/cloud-poznan.png)

#### [GTA Wiki](http://gta.wikia.com)
![](https://github.com/macbre/mediawiki-tags-cloud/raw/master/cloud-gta.png)

### [Polish Wikipedia](https://pl.wikipedia.org)

![](https://github.com/macbre/mediawiki-tags-cloud/raw/master/cloud-wikipedia-pl.png)

### Install

```
pip install pipenv
pipenv install
```

### Example

Generate tags cloud for [The Muppet Wiki](http://muppet.wikia.com):

```
python frequencies_from_dump.py  | tee muppet.json
python cloud_from_frequencies.py muppet.json
```

## Troubelshooting

If you get `AttributeError: python: undefined symbol: archive_errno` please refer to [`mediawiki-dump` package README](https://github.com/macbre/mediawiki-dump#dependencies).
