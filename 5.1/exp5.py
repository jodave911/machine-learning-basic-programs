count =0
word=" "
maxcount = 0
words = []
with open("data.txt","r") as file:
	for line in  file:
		string = line.lower().replace('.',' ').replace('.',' ').split(" ")
		for s in string:
			words.append(s)
for i in range(0,len(words)):
	count = 1
	for j in range(i+1,len(words)):
		if words[i]==words[j]:
			count=count+1
	if count>maxcount:
		maxcount=count
		word=words[i]
print("most replied word:"+word)
 
