st='w3resource'
dic={}
for ch in st:
    if ch in dic:
        dic[ch]+=1
    else:
        dic[ch]=1
for key in dic:
    print(key,':',dic[key],end=" ")