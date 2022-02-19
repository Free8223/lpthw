import os # 导入os模块，模块的概念后面讲到
#x = [x for x in os.listdir('.') if os.path.isdir(x)] # os.listdir可以列出文件和目录


x=[]
for y in os.listdir('.'):
 if os.path.isdir(y):
  x.append(y)

print(x)