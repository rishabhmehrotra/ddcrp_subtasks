import gensim, nltk, sklearn, pickle, sys, string, collections
from gensim.models import word2vec
from sklearn.cluster import KMeans
from ast import literal_eval
from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import numpy as np

ii = 1
queries = []
querymap = {}
#read queries
filee = "data/0.queries.txt"
with open(filee) as infile:
	for line in infile:
		query = line.split("\t")[0]
		queries.append(query)

cmap = {"":[]}
cmap1 = {"":""}
custmap = {"":[]}
c=0
filee = "data/crp_baseline.output.txt"
idx = 0
with open(filee) as infile:
	for line in infile:
		c+=1
		if c%1000==0:
			print c
		if c>1086:
			print c
			break;
		
		cl = int(line)
		idx +=1
		if cl in cmap1:
			qlist = cmap[cl]
			qliststr = cmap1[cl]
			qliststr += (str(queries[idx])+"("+str(idx)+") ")
			qlist.append(queries[idx])
			cmap[cl] = qlist
			cmap1[cl] = qliststr
		else:
			qlist = [queries[idx]]
			qliststr = str(queries[idx])+"("+str(idx)+") "
			cmap[cl] = qlist
			cmap1[cl] = qliststr

#fileout = "data/"+str(ii)+".viewCluster.txt"
fileout = "data/0.new.crp.baseline.viewCluster.txt"
oFile = open(fileout, 'w')
for (k,v) in cmap.items():
	oFile.write(str(k)+"\t"+str(cmap1[k])+"\n")
oFile.close()





