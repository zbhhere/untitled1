import json
import re
import os
from multiprocessing.pool import Pool
import Numpy
import EncrypFile

pattern=re.compile(r'[\u4e00-\u9fa5\/\\‘’！？，。“”…—\(\)–;*#‐%$&:?：!(.txt).,\-\'|\\\"\[\]\n]+',re.S)
collection_words=list()
title_words=list()
files=list()
i=0

##去重词汇
def delete_re_word(stop_words_tokens):
    # print(len(set(stop_words_tokens)))
    collection_words = [word for word in set(stop_words_tokens)]
    return collection_words


def dealD_results(stop_words_tokens_and_refilename):
    global collection_words
    global title_words
    global files
    global i
    filename=str(i)+'.txt'
    i=i+1
    title_words.append(stop_words_tokens_and_refilename[0])
    ##词汇去重
    collection_words += sorted(delete_re_word(stop_words_tokens_and_refilename[0]))
    # print(stop_words_tokens_and_count[2])
    print(stop_words_tokens_and_refilename[1])
    os.rename('VOA2/'+stop_words_tokens_and_refilename[1],'VOA2/'+filename)
    files.append(filename)
    EncrypFile.encryto_file(filename)


def GenerateKeywords(filename):

       sentence=re.sub(pattern,'',filename)
       ###分词
       tokens = Numpy.divide_word(sentence)
       ##计算出分词后词语总数
       count = len(tokens)
       ###词干提取
       porter_stem_tokens = Numpy.word_stem(tokens)
       ###词性归并
       wordnet_lematizer_tokens = Numpy.word_lematizer(porter_stem_tokens)
       ###去掉停用词
       stop_words_tokens = Numpy.delete_stopwords(wordnet_lematizer_tokens)

       return ([stop_words_tokens, filename])

def GenerateDictionary():
    global collection_words
    ###词干提取
    porter_stem_tokens = Numpy.word_stem(collection_words)
    ###词性归并
    wordnet_lematizer_tokens = Numpy.word_lematizer(porter_stem_tokens)

    collection_words = delete_re_word(wordnet_lematizer_tokens)

if __name__=='__main__':
    pool = Pool()

    for parents, dirnames, filenames in os.walk('VOA2/'):
        for filename in filenames:
          pool.apply_async(GenerateKeywords, args=(filename,), callback=dealD_results)

    pool.close()
    pool.join()


    f=open('FILES/files.txt','w',encoding='utf-8')
    f.write(json.dumps(files))
    f.close()

    GenerateDictionary()
    # collection_words = delete_re_word(collection_words)
    f=open('DICTIONARY/dictionary.txt','w',encoding='utf-8')
    f.write(json.dumps(collection_words))
    f.close()

    f=open('TITLEWORDS/titlewords.txt','w',encoding='utf-8')
    f.write(json.dumps(title_words))
    f.close()