'''
@Description: 
@Version: 
@Author: liguoying@iiotos.com
@Date: 2019-12-04 22:45:06
@LastEditTime: 2019-12-04 23:28:10
@LastEditors: 
'''

import sys
from functools import reduce

def add(a, b):
    assert isinstance(a, str) and isinstance(b, str)
    carry = 0
    maxlen = len(max([a,b], key=len))
    la = len(a)
    lb = len(b)
    i = 0
    res = []
    while i < maxlen:
        posa = la - i - 1
        posb = lb - i - 1
        if posa < 0:
            cura = 0
        else:
            cura = int(a[posa])
        if posb < 0:
            curb = 0
        else:
            curb = int(b[posb])
        cur_val = cura + curb + carry
        carry = cur_val // 10
        val = cur_val % 10
        i += 1
        res.append(str(val))
    return "".join(res[::-1])

while True:
    try:
        num = int(input())
        arrs = []
        for i in range(num):
            long_int = input()
            arrs.append(long_int)
        
        res = reduce(add, arrs)
        print(res)
    except:
        break