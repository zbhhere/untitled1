import json
import re
import os
from multiprocessing.pool import Pool
import Numpy
import EncrypFile

pattern=re.compile(r'[\u4e00-\u9fa5\/\\‘’！？，。“”…—\(\)–;*#‐%$&:?：!(.txt).,\-\'|\\\"\[\]\n]+',re.S)


def GenerateKeywords(filename):
    f = open('VOA2/' + filename, 'r',encoding='utf-8')
    print(filename)
    sentence=f.read()
    f.close()
    print(sentence)
    sentence = re.sub(pattern, '', sentence)
    ###分词
    tokens = Numpy.divide_word(sentence)

    ###词干提取
    porter_stem_tokens = Numpy.word_stem(tokens)
    ###词性归并
    wordnet_lematizer_tokens = Numpy.word_lematizer(porter_stem_tokens)
    ###去掉停用词
    stop_words_tokens = Numpy.delete_stopwords(wordnet_lematizer_tokens)
    # print(stop_words_tokens)
    f=open('VOA3/'+filename,'w',encoding='utf-8')
    f.write(json.dumps(stop_words_tokens))
    f.close()

if __name__=='__main__':
    pool=Pool(10)

    for parents,dirnames,filenames in os.walk('VOA2/'):
        filename=[x for x in filenames]
        pool.map(GenerateKeywords,filename)
        pool.close()
        pool.join()
