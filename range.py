# range 范围
# python 自带功能：清单产生器
#例如

range(5) #代表[0，1，2，3，4]
range(3) #代表[0,1,2,3]
import random

for i in range(100):# 90%以上，我们写这种for i in range 的for loop 只是为了让他的内容重复“某个固定次数“
	r = random.randint (1 , 1000)
	print('第' , i + 1,'次是' ,r )


