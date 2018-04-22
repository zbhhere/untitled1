# import json
# import os
# from multiprocessing import Process, Pool
#
# xs=list()
#
# def a(x):
#     global xs
#     print("this is a start")
#     xs.append(x)
#     # print(xs)
#     print("this is a stop")
#
#
# def b(num,i):
#     # print(num)
#     filenames='VOA2/'+num
#     # print(filenames)
#     f=open(filenames,'r',encoding='utf-8')
#     content=f.read()
#     # print(content)
#     f.close()
#     return ([num,i])
#
#
# if __name__ == '__main__':
#     # global xs
#     p = Pool(10)
#     i=0
#     for parent, dirnames, filenames in os.walk('VOA2/'):
#         for x in filenames:
#         # 这里表示，当b函数执行完成之后就会调用a函数，并且把b函数的返回值传给a函数。
#           p.apply_async(b, args=(x,i,), callback=a)
#           i+=1
#         # print(xs)
#     p.close()
#     p.join()
#     f=open('zbh.txt','w',encoding='utf-8')
#     f.write(json.dumps(xs))
#     f.close()
    # filelens=True
    # out_filename='encryp_files/' + in_filename
    #加密后的文件名，也是使用跟加密文件内容的密钥相同    文件的名字长度不能超过256位，超过会报错，因此要限制文件名字的长度
    # in_filename='African American History Month Ends with Renewed Debates Over the Usefulness of the 80-year-old US Tradition.txt'
    #     while filelens == True:
    # out_encry_filename = align(in_filename)
    #     out_encry_filename = out_encry_filename.encode('utf-8')
    #     aes1 = pyaes.AESModeOfOperationCTR(key)
    #     out_encry_filename_ciphertext = b2a_hex(aes1.encrypt(out_encry_filename)).decode("ASCII")
    #
    #     if len(out_encry_filename_ciphertext)>=180:
    #         filelens=True
    #         in_changelength_filename=in_filename[math.ceil(0.2*len(in_filename)):]
    #         os.rename('VOA2/'+in_filename,'VOA2/'+in_changelength_filename)
    #         in_filename=in_changelength_filename
    #
    #     else:
    #         filelens=False
    #


# import json
# import re
# import os
# from multiprocessing.pool import Pool
#
# from nltk import word_tokenize
# from nltk.corpus import stopwords
#
# import Numpy
# import EncrypFile
#
# pattern=re.compile(r'[\u4e00-\u9fa5\/\\‘’！？，。“”…—\(\)–;*#‐%$&:?：!(.txt).,\-\'|\\\"\[\]\n]+',re.S)
# # english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%','\\','\\\\n']
#
# def GenerateKeywords(filename):
#     f=open('VOA2/'+filename,'r',encoding='utf-8')
#     sentence=f.read()
#     sentence = re.sub(pattern, '', sentence)
#     sentence=[word.lower() for word in word_tokenize(sentence)]
#     print(sentence)
#     ##计算出分词后词语总数
#     # count = tokens.count()
#     ###词干提取
#     porter_stem_tokens = [word for word in Numpy.word_stem(sentence)]
#     ###词性归并
#     wordnet_lematizer_tokens = Numpy.word_lematizer(porter_stem_tokens)
#     print(wordnet_lematizer_tokens)
#     ###去掉停用词
#     stop_words_tokens =[word for word in wordnet_lematizer_tokens if not word in stopwords.words('english')]
#
#     return (stop_words_tokens)
#
# if __name__=='__main__':
#     for parents,dirnames,filenames in os.walk('DICTIONARY/'):
#         for filename in filenames:
#             f=open('DICTIONARY/'+filename,'r',encoding='utf-8')
#             t=json.loads(f.read())
#             print(len(t))  #5886     #2205  #2212

            #
            # import json
            # import re
            # import os
            # from multiprocessing.pool import Pool
            # import Numpy
            # import EncrypFile
            #
            # pattern = re.compile(r'[\u4e00-\u9fa5\/\\‘’！？，。“”…—\(\)–;*#‐%$&:?：!(.txt).,\-\'|\\\"\[\]\n]+', re.S)
            # collection_words = list()
            # title_words = list()
            # files = list()
            # i = 0
            #
            #
            # ##去重词汇
            # def delete_re_word(stop_words_tokens):
            #     # print(len(set(stop_words_tokens)))
            #     collection_words = [word for word in set(stop_words_tokens)]
            #     return collection_words
            #
            #
            # def dealD_results(stop_words_tokens_and_refilename):
            #     global collection_words
            #     global title_words
            #     global files
            #     global i
            #     filename = str(i) + '.txt'
            #     i = i + 1
            #     title_words.append(stop_words_tokens_and_refilename[0])
            #     ##词汇去重
            #     collection_words += sorted(delete_re_word(stop_words_tokens_and_refilename[0]))
            #     # print(stop_words_tokens_and_count[2])
            #     print(stop_words_tokens_and_refilename[1])
            #     os.rename('VOA2/' + stop_words_tokens_and_refilename[1], 'VOA2/' + filename)
            #     files.append(filename)
            #     EncrypFile.encryto_file(filename)
            #
            #
            # def GenerateKeywords(filename):
            #
            #     sentence = re.sub(pattern, '', filename)
            #     ###分词
            #     tokens = Numpy.divide_word(sentence)
            #     ##计算出分词后词语总数
            #     count = len(tokens)
            #     ###词干提取
            #     porter_stem_tokens = Numpy.word_stem(tokens)
            #     ###词性归并
            #     wordnet_lematizer_tokens = Numpy.word_lematizer(porter_stem_tokens)
            #     ###去掉停用词
            #     stop_words_tokens = Numpy.delete_stopwords(wordnet_lematizer_tokens)
            #
            #     return ([stop_words_tokens, filename])
            #
            #
            # def generateDictionary():
            #     global collection_words
            #     ###词干提取
            #     porter_stem_tokens = Numpy.word_stem(collection_words)
            #     ###词性归并
            #     wordnet_lematizer_tokens = Numpy.word_lematizer(porter_stem_tokens)
            #
            #     collection_words = delete_re_word(wordnet_lematizer_tokens)
            #
            #
            # if __name__ == '__main__':
            #     pool = Pool()
            #
            #     for parents, dirnames, filenames in os.walk('VOA2/'):
            #         for filename in filenames:
            #             pool.apply_async(GenerateKeywords, args=(filename,), callback=dealD_results)
            #
            #     pool.close()
            #     pool.join()
            #
            #     f = open('FILES/files.txt', 'w', encoding='utf-8')
            #     f.write(json.dumps(files))
            #     f.close()
            #
            #     generateDictionary()
            #     f = open('DICTIONARY/dictionary.txt', 'w', encoding='utf-8')
            #     f.write(json.dumps(collection_words))
            #     f.close()
            #
            #     f = open('TITLEWORDS/titlewords.txt', 'w', encoding='utf-8')
            #     f.write(json.dumps(title_words))
            #     f.close()
# import os
# #
# import nltk
#
#
# def getsentence(filename):
#     f=open('VOA3/'+filename,'r',encoding='utf-8')
#
#     return f.read()
#
# for parents,dirnames,filenames in os.walk('VOA3/'):
#     content = list()
#     for sentence in filenames:
#         # print(sentence)
#         content.append(getsentence(sentence))
#
#     # print(content)
# test=nltk.text.TextCollection(content)
# print(content)
# print(test.idf('economy'))
# print(filenames[0])
# print(test.tf('economy',content[4]))

# D_ALL=list(dict())
#
# for i in range(10):   ##文件数
#                        ####里面有一个dictionary的循环
#     D = dict()
#     D[str(i)] = 'zbh' + str(i)
#     D[str(i+1)]='hehe'+str(i+2)
#     D_ALL.append(D)
#
# print(D_ALL)
# import os
# from multiprocessing.pool import Pool
#
#
# def InsertTitle(filename):
#     f=open('VOA2/'+filename,'a',encoding='utf-8')
#     f.write(filename)
#
# if __name__=='__main__':
#     pool = Pool(10)
#     for parents, dirnames, filenames in os.walk('VOA2/'):
#         filename = [x for x in filenames]
#         pool.map(InsertTitle, filename)
#         pool.close()
#         pool.join()