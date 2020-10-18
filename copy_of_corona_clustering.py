# -*- coding: utf-8 -*-
"""Copy of corona_clustering

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18JXpwuxGqUIs8qQBoDkfAzNWIDmt3i7p
"""

from google.colab import drive
drive.mount('/content/gdrive')

from sklearn.feature_extraction.text import TfidfVectorizer
from pickle import load,dump  
import pandas as pd
import numpy as np
from copy import deepcopy

from sklearn.metrics.pairwise import cosine_similarity
from scipy.cluster.hierarchy import fcluster
from scipy.cluster.hierarchy import dendrogram, linkage

from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
from nltk.stem.snowball import SnowballStemmer

from copy import deepcopy
import re

import string


l_sw=stopwords.words("english")
tk=TweetTokenizer()
snow=SnowballStemmer("english")


def clean(st):

  #Lowercase
  temp=deepcopy(st)
  temp=temp.lower()

  #Remove whitespace
  temp=temp.replace("\n"," ").replace("\r"," ")

  #Remove URL
  temp = re.sub(r"http\S+", "", temp)

  #Tokenise
  tokens=tk.tokenize(temp)

  #remove punctuations, hashtags and stopwords
  cl_1=[]
  for i in tokens:
    if i not in string.punctuation and i not in l_sw and i!="...":
      if i[0]=='#':
        cl_1.append(i[1:])
      else:
        cl_1.append(i)
  
  #Stem - Snowball
  cl_2=[snow.stem(i) for i in cl_1]

  #Remove emojis and serialise
  final=''

  ff=open("/content/gdrive/My Drive/Colab Notebooks/Corona_Clusters/single/to_be_deleted1.txt","w")

  for i in cl_2:
    try:
      ff.write(i)
      final+=(i+" ")
    except:
      pass
  
  ff.close()

  return final[:-1]

f=open("/content/gdrive/My Drive/Colab Notebooks/corona_news_10mins.pickle","rb")
d_d=load(f)
f.close()

d_d[0][0][0]

d_d[0].keys()

nnff=open("/content/gdrive/My Drive/Colab Notebooks/corona_news_unpacked.pickle","rb")
unpack=load(nnff)
nnff.close()



####TD-IDF and File TextFile 


#Modified cleanup
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
from nltk.stem.snowball import SnowballStemmer

from copy import deepcopy
import re

import string


l_sw=stopwords.words("english")
tk=TweetTokenizer()
snow=SnowballStemmer("english")


def clean_without(st):

  #Lowercase
  temp=deepcopy(st)
  temp=temp.lower()

  #Remove whitespace
  temp=temp.replace("\n"," ").replace("\r"," ")

  #Remove URL
  temp = re.sub(r"http\S+", "", temp)

  #Tokenise
  tokens=tk.tokenize(temp)

  #remove punctuations, hashtags and stopwords
  cl_1=[]
  for i in tokens:
    if i not in string.punctuation and i not in l_sw and i!="...":
      if i[0]=='#':
        cl_1.append(i[1:])
      else:
        cl_1.append(i)
  
  #Remove emojis and serialise
  final=''

  ff=open("/content/gdrive/My Drive/Colab Notebooks/Corona_Clusters/single/to_be_deleted1.txt","w")

  for i in cl_1:
    try:
      ff.write(i)
      final+=(i+" ")
    except:
      pass
  
  ff.close()

  return final[:-1]


def file_write(cluster_labels,l_id,nm):
  temp={}
  
  for i in range(len(cluster_labels)):
    if int(cluster_labels[i]) not in temp:
      temp[int(cluster_labels[i])]=[l_id[i]]
    else:
      temp[int(cluster_labels[i])].append(l_id[i])
    
  nnnfff=open("/content/gdrive/My Drive/Colab Notebooks/Corona_Clusters/news/"+nm+"single_tp.txt","w",encoding="utf-8")
  print("Inside Here")


  for i in temp:
    qq=nnnfff.write("\n\n\nCluster "+str(i)+"\n")
    tw=[unpack[k]["tweet_text"] for k in temp[i]]
    nnnfff.write(str(len(tw))+"\n")


    try:
      vec=TfidfVectorizer(ngram_range=(2,3),min_df=2,max_features=10,preprocessor=clean_without)
      vec_f=vec.fit_transform(tw).toarray()
    except:
      vec=TfidfVectorizer(ngram_range=(2,3),max_features=10,preprocessor=clean_without)
      vec_f=vec.fit_transform(tw).toarray()

    fn_n = np.array(vec.get_feature_names())

    for j in fn_n:
      nnnfff.write(j+"\t")
    nnnfff.write("\n\n")

    for j in temp[i]:
      nnnfff.write(unpack[j]["tweet_text"].replace("\n"," ").replace("\r"," ")+"\n")

  nnnfff.close()

def cluster(l_id,nm):

  #l_proc=[unpack[k]["proc"] for k in l_id]
  l_proc=[clean(unpack[k]["tweet_text"]) for k in l_id]


  vec=TfidfVectorizer(ngram_range=(2,3),min_df=2)
  vec_f=vec.fit_transform(l_proc).toarray()

  print("TF-IDF Done for ",nm)

  #Cosine Similarity
  sm=cosine_similarity(vec_f)
  sm=1-sm

  v=pd.DataFrame(sm,columns=l_id, index=l_id)

  print("\nCosine Similarity done for ",nm)

  #HCA
  lk=linkage(sm,"average")
  print("\nLinkage Done")

  dist,mn,mx=0,0,0

  b=list(lk)

  for q in range(len(b[:-1])):
    if b[q+1][-2]-b[q][-2]>dist:
      dist=b[q+1][-2]-b[q][-2]
      mn=b[q][-2]
      mx=deepcopy(b[q+1])
      mn=deepcopy(b[q])

  cluster_labels = fcluster(lk, int(mn[-2]), criterion='distance')
  cluster_labels1 = pd.DataFrame(cluster_labels, columns=['ClusterLabel'],index=l_id)
  print(set(cluster_labels))

  nnff=open("/content/gdrive/My Drive/Colab Notebooks/Corona_Clusters/news/"+nm+"_single.pickle","wb")
  dump([nm,cluster_labels,l_id],nnff)
  nnff.close()
  print("\nPickling Done")

  file_write(cluster_labels,l_id,nm)

  print("\nText File Writing Done")

  print("\nClustering Done!")
  print("\n\n")

for i in d_d:
  for j in d_d[i]:
    if d_d[i][j]!=[]:
      l_id=[k["tweet_id"] for k in d_d[i][j]]
      cluster(l_id,str(i)+"-"+str(j))
      print(i," ",j)

l_id=[k["tweet_id"] for k in d_d[4][3]]

len(l_id)

l_id=[]
l_proc=[]

for j in d_d[0]:
  l_id.append(j["tweet_id"])
  l_proc.append(clean(j["tweet_text"]))

len(l_proc)

cluster(l_id,"4-3")

for i in d_d:

  l_id=[k["tweet_id"] for k in d_d[i]]
  l_proc=[clean(k["tweet_text"]) for k in d_d[i]]

  cluster(l_id,l_proc,str(i))