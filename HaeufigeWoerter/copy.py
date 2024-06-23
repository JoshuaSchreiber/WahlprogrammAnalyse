import re
from collections import Counter
from itertools import islice

stopwords = None

def read_and_clean_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()
    text = re.sub(r'[^a-zäöüß\s]', '', text)
    return text

def count_ngrams(text, n):
    words = text.split()
    ngrams = zip(*(islice(words, i, None) for i in range(n)))
    return Counter(ngrams)

def read_stopwords(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        stopwords = set(file.read().split())
    return stopwords

def filter_stopwords(counter, stopwords):
    return Counter({word: count for word, count in counter.items() if word not in stopwords})

def main(file_path):
    text = read_and_clean_text(file_path)

    word_counts = count_words(text)
    filtered_word_counts = filter_stopwords(word_counts, stopwords)
    print("Häufigste Wörter (ohne Füllwörter):")
    for word, count in filtered_word_counts.most_common(100):  # Die 10 häufigsten Wörter
        print(f"{word}: {count}")

    for n in range(2, 6):
        ngram_counts = count_ngrams(text, n)
        filtered_ngram_counts = filter_stopwords(ngram_counts, stopwords)
        print(f"\nHäufigste {n}-Gramme (ohne Füllwörter):")
        for ngram, count in filtered_ngram_counts.most_common(10):  # Die 10 häufigsten n-Gramme
            print(f"{' '.join(ngram)}: {count}")


file_path = '../Data/Wahlprogramme/CDUCSU.txt'
stopwords_file_path = '../Data/FuellWoerter.txt'

stopwords = read_stopwords(stopwords_file_path)
main(file_path)
