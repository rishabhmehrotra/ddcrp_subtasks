#!/usr/bin/python
import sys,json
import pickle


print "hello"
vocab = {"":0}
i = 0
while i>=0:
	#filestr = "data/"+str(i)+".allQueries.freq.nUsers.txt"
	#filestr = "data/allTasks.queries.freq.nUsers.txt"
	filestr = "data/0.queries.txt"
	with open(filestr) as infile:
		for line in infile:
			line1 = line.split('\t')[0]
			#print "line:_%s_"%line1
			words = line1.split(' ')
			for w in words:
				if len(w)<2:
					continue
				#print w
				if w in vocab:
					c = vocab[w]
					c+=1
					vocab[w] = c
				else:
					#vocab.update({w: 1})
					vocab[w] = 1
	print "vocab size: %d"%len(vocab)
	#fileout = "data/"+str(i)+".vocab.txt"
	#fileout = "data/allTasks.vocab.txt"
	fileout = "data/0.new.vocab.txt"
	oFile = open(fileout, 'w')
	for (k,v) in vocab.items():
		if len(k)>15:
			continue
		#oFile.write(k+"\t"+str(vocab[k])+"\n")
		oFile.write(k+"\n")
	oFile.close()
	i-=1
	vocab.clear()
