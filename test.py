'''
@Description: 
@Version: 
@Author: liguoying@iiotos.com
@Date: 2019-12-04 00:39:04
@LastEditTime: 2019-12-04 00:45:05
@LastEditors: 
'''
import sys

str1 = input()
str2 = input()
for s in [str1, str2]:
    if len(s) < 8:
        print(s+"0"*(8-len(s)))
    for i in range(0,len(s)//8+1):
        curs = s[i*8:(i+1)*8]
        if len(curs)<8:
            print(curs+"0"*(8-len(curs)))
        else:
            print(curs)