data = [] #存贮reviews中共有100万条留言
count = 0 
with open ('reviews.txt','r') as f: #读取模式 
	for line in f:  #f的每一行叫做line
		data.append(line) #把line 装入date list之中
		count += 1  # count 每次按照加1 开始递增 
		if count % 1000 == 0: #  如果count 除以 1000的余数等于0  目的是打印每一千的len
			print (len(data)) #打出每1000 dete的元素
print('档案读取完毕，总共有' ,len(data))

sum_len = 0  #留言中总的字数命名  
for x in data:#把data清单中每一笔字串(留言）命名为d,
	sum_len = sum_len + len(x) # 一样sum_len+= len(x) 
#代表sum_Len 是每一条留言（字串）的长度相加的总和
print('每条留言的平均长度：', sum_len/len(data) , '字')
#每条留言的平均值 等于总的字串除以总字串（留言）的数量

new = []
for d in data:
	if len (d) < 100:
		new.append(d)
print ('一共有',len(new) , '笔留言长度小于100')
print (new[0])
print (new[1])



