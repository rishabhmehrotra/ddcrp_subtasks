#!/usr/bin/python
import sys,json
import pickle


print "hello"
vocab = {"":0}
wordid = {"":0}
i = 0
while i>=0:
	#filestr = "data/"+str(i)+".allQueries.freq.nUsers.txt"
	filestr = "data/allTasks.queries.freq.nUsers.txt"
	wid = 1
	with open(filestr) as infile:
		for line in infile:
			line1 = line.split('\t')[0]
			words = line1.split(' ')
			for w in words:
				if len(w)<2:
					continue
				if w in vocab:
					c = vocab[w]
					c+=1
					vocab[w] = c
				else:
					vocab[w] = 1
					wordid[w] = wid
					wid+=1
	#fileout = "data/"+str(i)+".wordIds.txt"
	fileout = "data/allTasks.wordIds.txt"
	oFile = open(fileout, 'w')
	for (k,v) in wordid.items():
		if len(k)>15:
			continue
		oFile.write(k+"\t"+str(v)+"\n")
	oFile.close()

	#fileout = "data/"+str(i)+".corpus.txt"
	fileout = "data/allTasks.corpus.txt"
	oFile = open(fileout, 'w')
	with open(filestr) as infile:
		for line in infile:
			line1 = line.split('\t')[0]
			words = line1.split(' ')
			querymap = {0:0}
			for w in words:
				if len(w)<2:
					continue
				wid = wordid[w]
				if wid in querymap:
					t = querymap[wid]
					t+=1
					querymap[wid]=t
				else:
					querymap[wid] = 1
			oFile.write(str(len(querymap)-1)+"\t")
			for (k,v) in querymap.items():
				if k==0:
					continue
				oFile.write(str(k)+":"+str(v)+" ")
			oFile.write("\n")
	oFile.close()
	i-=1
	vocab.clear()
