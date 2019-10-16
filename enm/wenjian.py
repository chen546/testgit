#!/usr/bin/python
#-*-coding:utf-8-*-

# txt=open(r'c:\Users\chen\Desktop\111.txt',mode='r',encoding='utf-8')
# a=txt.read()
# print(a)

# txt=open(r'111.txt','w',encoding='utf-8')
# a=''
# for i in range(1,10):
#         for j in range(1,i+1):
#             txt.write(" %d*%d=%d "%(j,i,i*j))
#         txt.write('\n')
# txt.write(a)
# txt.close()

# txt=open(r'111.txt','a',encoding='utf-8')
# txt.write('\n'+'nihao')
# txt.close()


# a=open('111.txt','r',encoding='utf-8')
# for i in range(1,10):
#     for j in range(1,i+1):
#         a.write(" %d*%d=%d "%(j,i,i*j))
#     a.write('\n')
# b=a.readline()
# d=a.readline()
# a=[]
# for i in b:
#     c=i.rstrip('\n')
#     a.append(c)
# print(b,d)



# a=open('111.txt','r+',encoding='utf-8')
# a.write('nihao')
# c=a.read()
# print(a)
# a.close()

# a=open(r'C:\Users\chen\Desktop\{5~SFH3QD)M@VFMU`X(B_DU.png',mode='rb')
# c=a.read()
# print(c)

# a='sds{}fd%sfsdf'
# print(a.upper())
# print(a.lower())
# print(a.swapcase())
# print(a.split('s'))
# print(a.title())
# print(a.replace('fd','dsf'))
# print(a.count('s'))
# print(a.index('s'))
# print(a.strip('s'))
# print(a.format(12))
# print(a%(12))

# a=input('name:')
# b=a.startswith('c')
# c=a.endswith('n')
# print(a,b)
# print(a,c)


# import copy
# a=[12,45,78,64,654]
# a.append(545)
# print(a)
# print(a.index(64))
# a.pop(3)
# print(a)
# a.remove(12)
# print(a)
# a.insert(4,46)
# print(a)
# a.sort()
# print(a)
# a.reverse()
# print(a)
# b=a.count(12)
# print(b)
# a.copy()
# print(a)
#
# a=copy.deepcopy(a)
# print(a)
#
# print(a.clear())


with open('111.txt','r',encoding='ansi')as a:  #_enter_
    print(a.read())    #_exit_

# a=open(r'111.txt',mode='r+',encoding='utf-8')
# a.write('今天晚上,妈妈带我到油田的外婆家玩。'
# '到了外婆家,妈妈就一直在和外婆谈话。我觉得很无聊，于是，我就叫了几个小伙伴拿着瓶子一起去附近的田野里捉蛐蛐。'
# '走近田野，我们就听见了蛐蛐的“大合唱”。于是，我们拿着各自的瓶子，轻手轻脚地寻找着蛐蛐的下落。'
# '过了一会儿，我发现，在前方一米处，有一只乌黑油亮的蛐蛐正在忘我地高声歌唱着。我高兴极了，就蹑手蹑脚地走了过去。但是，那只蛐蛐似乎察觉到了我的存在，还没等我迈开第一步，它就轻轻地跳了好几下，眨眼间，它就从我的视野里消失了。“唉！它干嘛要这么机灵呢？”我自言自语道。'
# '忽然，有一个小伙伴大叫道：“我抓到了！我抓到了！”我们往他的瓶子里一看，果然，他的瓶子里有一只乌黑油亮的大蛐蛐。我羡慕极了，心想：我一定也要抓一只更大的蛐蛐。于是，我就继续去寻找蛐蛐。'
# '突然，我发现有一只特别大的蛐蛐正在悠闲地唱着歌。我怕它再逃跑了，于是，我不管三七二十一，猛地扑上去，抓住了它。'
# '时间不早了，我才恋恋不舍地离开了田野。'
# '捉蛐蛐真有趣啊！'
# '文| 李梓铭')
# count = len(a.readlines())
# a=a.read()
# print(count)
#
# def hanshu(a,b):
#     c = a + b
#     print(c)
#
#
# def hanshu1():
#     pass
#
# def hanshu2():
#     pass

# def hans():
#     if __name__ == '__main__':
#         print('hello')
#     else:
#         print('en')
# hans()
if __name__ == '__main__':
        print('hello')