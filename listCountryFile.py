f=open("countries.txt","r")

listCount=[]
for line in f:
   line=line.strip()
   listCount.append(line)
   print(line)
   
print(listCount)
f.close()