#!/usr/bin/python3

import os
import sys

if len(sys.argv) == 1:
    print('错误！请传入 xml 文件')
elif len(sys.argv) > 2:
    print('错误！传入参数太多')
else:
    print('传入的文件是 %s' % sys.argv[1])

newfilestr = ''
    
with open(sys.argv[1], 'r') as fin:
    while True:
        linestr = fin.readline()
        if linestr == '':       #表示文件结束
            break
        #print(linestr)
        linestr = linestr[:len(linestr)-1]      # 去除行尾
        #下面开始对本行内容分析
        if (('name=' in linestr) or ('name =' in linestr)) and (('project' in linestr) or ('path' in linestr)):   #本行内容含有name信息，进行处理
            #print(linestr)
            newstr = linestr
            #下面开始分析本行内容，删除remote和revision等内容
            if ' remote=' in newstr:    # 包含remote信息，删除掉
                str1 = ' remote="'
                str2 = '"'
                newstr = newstr[0:newstr.index(str1)] + newstr[newstr.index(str1) + len(str1) + newstr[newstr.index(str1)+len(str1):].index(str2)+1:]
            if ' revision=' in newstr:   # 包含revision信息，删除掉
                str1 = ' revision="'
                str2 = '"'
                newstr = newstr[0:newstr.index(str1)] + newstr[newstr.index(str1) + len(str1) + newstr[newstr.index(str1)+len(str1):].index(str2)+1:]
            if ' upstream=' in newstr:   # 包含revision信息，删除掉
                str1 = ' upstream="'
                str2 = '"'
                newstr = newstr[0:newstr.index(str1)] + newstr[newstr.index(str1) + len(str1) + newstr[newstr.index(str1)+len(str1):].index(str2)+1:]
            #print(newstr)
            newfilestr = newfilestr + newstr + '\n'
        else:           # 本行没有name信息，不关心，原样输出
            newfilestr = newfilestr + linestr + '\n'

print(newfilestr)
with open(sys.argv[1], 'w') as fout:
    fout.write(newfilestr)

