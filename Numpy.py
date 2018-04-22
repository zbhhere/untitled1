import jieba
import nltk
import re
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import collections
import os
import time
import math
import numpy


# from provider.generate_invertible_matrix import get_encrpy_T_I

###文件读取
def read_file(file_path):
    fs = open(file_path, 'r', encoding='utf-8')
    sentences = fs.read()
    return sentences


##  去掉标点符号
def delete_dot(sentences):
    r = '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+'
    sentence_sub_dots = re.sub(r, '', sentences)
    return sentence_sub_dots
##分词
def divide_word(sentence_sub_dots):
    tokens = nltk.word_tokenize(sentence_sub_dots)
    return tokens

##词干提取
def word_stem(tokens):
    porter_stem = PorterStemmer()
    porter_stem_tokens = [porter_stem.stem(token) for token in tokens]
    return porter_stem_tokens

##词性归并
def word_lematizer(porter_stem_tokens):
    wordnet_lematizer = WordNetLemmatizer()
    wordnet_lematizer_tokens = [wordnet_lematizer.lemmatize(porter_stem_token) for porter_stem_token in
                                porter_stem_tokens]
    return wordnet_lematizer_tokens

# 去掉停用词
def delete_stopwords(wordnet_lematizer_tokens):
    # stop_words=stopwords()
    stop_words_tokens = [wordnet_lematizer_token for wordnet_lematizer_token in wordnet_lematizer_tokens if
                         wordnet_lematizer_token not in stopwords.words('english')]
    # Rfiltered = nltk.pos_tag(stop_words_tokens)
    return stop_words_tokens


##词频计算

def word_frequent(stop_words_tokens,count):
    results = collections.Counter(stop_words_tokens).most_common()
    dictionary =dict()
    for result in results:
        dictionary[result[0]]=result[1]/count

    return dictionary


##去重词汇
def delete_re_word(stop_words_tokens):
    collection_words = [word for word in set(stop_words_tokens)]
    return collection_words

