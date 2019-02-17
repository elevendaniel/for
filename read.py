#读取档案 
date = []
with open ('food.txt', 'r') as f:#打开文件的固定语法，with是python中特有的语法
#打开 food.txt的名称文件， r 代表读取，w代表写， as f：f是一个代号
#with +open 就不需要加close了 
	for line in f:
		# for in 是一个loop , line是代号 意思是每一行取名为line，每一次拿出来称作line
		# for loop的意思是 把清单中的东西一个一个拿出来 
		date.append(line.strip())
		#append只能给list添加内容 strip.()代表清除换行符号的功能，只能针对字串 ；如果是整数或者复数就不可以使用，这是语法问题
print(date)
