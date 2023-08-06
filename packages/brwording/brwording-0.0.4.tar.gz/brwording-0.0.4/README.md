## `BRWording` - Text Analytics for Portuguese Wordings

Create an easy Text Analytics in *`One-Line-Code`*

<hr>

![](https://img.shields.io/badge/pypi-0.0.4-blue) ![](https://img.shields.io/badge/python-4.7|4.8|4.9-lightblue) ![](https://img.shields.io/badge/Licence-MIT-lightgray) ![](https://img.shields.io/badge/status-Beta-darkgreen) ![](https://img.shields.io/badge/pipeline-passed-green) ![](https://img.shields.io/badge/testing-passing-green) ![](https://img.shields.io/badge/TheScientist-APP-brown)


**Main Features:**

- Load `Excel`, `CSV` and `TXT` file types
- Stemming
- Lemmatization
- Stopwords
- TD-IDF
- Sentimental Analysis
- Graphical interpretation
- Word Cloud

The TF-IDF was calculated by:

![img](https://github.com/TheScientistBr/BRWording/blob/main/images/tf-idf.png?raw=true)

<hr>

## How to Install

```shell
pip install BRWording
```

<BR>
<hr>
<BR>

## How to use

`sintax`:
```python
from brwording import brwording

w = brwording.wording()

w.load_file('data/example.txt',type='txt')
w.build_tf_idf(lemmatizer=True,stopwords=True)

w.tfidf

```

**Output**

![img](https://github.com/TheScientistBr/BRWording/blob/main/images/tfidf.png?raw=true)

If want to see the sentimental Graphical interpretation

`sintax`:
```python

w.sentimental_graf()

```
**output**
![img](https://github.com/TheScientistBr/BRWording/blob/main/images/graf_sentimental.png?raw=true)

if you want to create a wordcloud, just strike the folowing command, but if you want to create a cloud with your own mask, just pass you image address as `picture`

`sintax`:
```python
w.word_cloud(picture='none')

```

**output**

![img](https://github.com/TheScientistBr/BRWording/blob/main/images/wc.png?raw=true)

<hr>
<BR>

**Looking for a word into colection**

if you want to see what files on your colection has a word, run `look2word` 

`sintax`:
```python
w.look2word('bonito')

```

<BR>

New features are incoming.

<hr>
<BR>

`enjoi!`
