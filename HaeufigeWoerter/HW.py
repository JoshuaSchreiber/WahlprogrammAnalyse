import re
from collections import Counter
from itertools import islice
from partei import Partei

def read_stopwords(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        stopwords = set(file.read().split())
    return stopwords

def read_and_clean_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()
    text = re.sub(r'[^a-zäöüß\s]', '', text)
    return text

def count_words(text):
    words = text.split()
    return Counter(words)

def count_ngrams(text, n):
    words = text.split()
    ngrams = zip(*(islice(words, i, None) for i in range(n)))
    return Counter(ngrams)

def filter_stopwords(counter, stopwords):
    return Counter({word: count for word, count in counter.items() if word not in stopwords})

stopwordsFilePath = 'Data/FuellWoerter.txt'
stopwords = read_stopwords(stopwordsFilePath)

def main(partei):
    text = read_and_clean_text(partei.wahlprogrammLoc)

    word_counts = count_words(text)
    partei.wordCount = sum(word_counts.values())
    filtered_word_counts = filter_stopwords(word_counts, stopwords)

    partei.haeufigsteWoerter = [(word, count) for word, count in filtered_word_counts.most_common(10)]

    for n in range(2, 6):
        ngram_counts = count_ngrams(text, n)
        filtered_ngram_counts = filter_stopwords(ngram_counts, stopwords)

        attribute_name = f'_{n}Gramme'
        attribute_value = [(ngram, count) for ngram, count in filtered_ngram_counts.most_common(10)]

        setattr(partei, attribute_name, attribute_value)

    # Save data to JSON file
    partei.save_Data_to_json(f"HaeufigeWoerter/Results/{partei.name}.json")

