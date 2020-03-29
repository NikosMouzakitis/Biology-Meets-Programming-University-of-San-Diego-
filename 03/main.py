import operator

# returns a list with the most frequent k-mers in a genome string.
def frequencyMap(Text, k):
	freq={}
	n = len(Text)
	# list to contain most frequent k-mers.
	l = [] 

	for i in range(n-k+1):
		Pattern = Text[i:i+k]
		freq[Pattern] = 0

	print("Detected %d different %d-mers"%(len(freq), k))
	
	for i in range(n-k+1):
		Pattern = Text[i:i+k]
		if(Pattern == Text[i:i+k]):
			freq[Pattern] += 1	

	#descending order.
	freq_sorted = sorted(freq.items(), key=operator.itemgetter(1), reverse=True)
	
	maxval = freq_sorted[0][1]
	
	for i in range(n-k+1):
		if(freq_sorted[i][1] == maxval):
			l.append(freq_sorted[i][0]) ## append k-mer		
		else:
			break
	print("Most frequent occurance: %d"%(maxval))

	return l

ori="ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"

#used for testing our function
simple_text = "AGAGATCACGTCAAGATCAAGAGATCACGATCA"

most_frequent_kmers = frequencyMap(ori, 9)
print(most_frequent_kmers)
