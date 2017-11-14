#!/usr/bin/python3

import os
import sys

if len(sys.argv) == 1:
    print('错误！请传入 xml 文件')
elif len(sys.argv) > 2:
    print('错误！传入参数太多')
else:
    print('传入的文件是 %s' % sys.argv[1])

with open(sys.argv[1], 'r') as fin:
    while True:
        linestr = fin.readline()
        if linestr == '':       #表示文件结束
            break
        #print(linestr)
        #下面开始对本行内容分析
        if (('name=' in linestr) or ('name =' in linestr)) and (('project' in linestr) or ('path' in linestr)):   #本行内容含有name信息
            #print(linestr)
            #下面分析本行内容，并提取name
            charistr1 = 'name="'
            charistr2 = '"'
            gitprojstr = linestr[linestr.index(charistr1)+len(charistr1) : linestr.index(charistr1)+len(charistr1)+ linestr[linestr.index(charistr1)+len(charistr1):].index(charistr2)]
            #print(gitprojstr)
            #下面开始创建git工程
            cmd = 'git init --bare %s.git' % gitprojstr
            print(cmd)
            os.system(cmd)

