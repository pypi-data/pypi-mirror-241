# Tagcounter

html-tag-counter is a program for counting html tags of a webpage.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install html-tag-counter.

```bash
pip install html-tag-counter
```

## Usage

```bash

html-tag-counter --get yandex.ru  # downloads webpage, returns html tags and their counts, creates a new database, saves tags and counts into database
html-tag-counter --get ydx        # checks for synonyms of the urls in synonyms.yaml, feel free to add your own synonyms
html-tag-counter --view yandex.ru # returns html tags and their counts saved in database
html-tag-counter                  # starts GUI version: enter url or synonym (e.g. yandex.ru or ydx), press [Show From DB] or [Download From Internet] button
```

Thank you for reading this. Good luck!
