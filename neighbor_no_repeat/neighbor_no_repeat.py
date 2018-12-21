# -*- coding: utf-8 -*-
"""
Created on 2018-12-20

@author: zhangyaxu
"""

def neighbor_no_repeat(x):
    uniquex=set(x)
    msg=''
    if len(x)==len(uniquex):
        msg = '无重序列, 直接返回'
        rst=list(x)
    else:
        rst=[] # 结果序列默认初始为空
        numx=[]
        for xtem in uniquex:
            numtem=x.count(xtem)
            numx.append((xtem,numtem))
        numx.sort(key=lambda y: y[1])
        numx.reverse()
        max_cover=len(x)-numx[0][1]  # 出现次数最多的那个字符之外 的其它字符出现的总次数m
        #
        if numx[0][1] - 1 > max_cover :
            #其它字符无法填充最长字符的相隔位，则没有这样的合规序列，不更新rst
            msg = '无法生成合规序列'
        else:
            msg='合规序列success'
            # 存在合规序列，则找到合规序列
            while len(numx)>0:
                if len(rst)==0:
                    numcur=numx.pop(0)  # 从当前出现最多的字符开始间隔填充， numcur: ('a',5) ,  numx:[('b',3),('c',3)('d',1)]
                    current_str=[numcur[0]]*numcur[1] # ['a','a','a','a','a']
                else:
                    current_str=rst
                most_insert_len=len(current_str)*2-2  # 最大可填充的index位置 ，此例第一次a的间隔填充最大位置为 5+4-1 即 5*2-2=8
                baseidx=0;baseidx_impr = 0 # 第一个填充的字符的初始位，默认0，若第一个字符没填充满a的间隔，会更新baseidx_impr到对应的位置
                insert_status=True # 当前待填充的填充状态，默认为True，即 仍未完成当前最多字符的间隔填充。
                while len(numx)>0 and insert_status==True:
                    baseidx = baseidx + baseidx_impr # 本轮填充的基础位置
                    coverx=numx.pop(0)
                    cover_str=[coverx[0]]*coverx[1] # ['b','b','b'] , ['c','c','c']
                    for cover_idx,cover_strx in enumerate(cover_str):
                        if baseidx+cover_idx*2+1<=most_insert_len:
                            # 没超出最多可填充位，则依次按位填充
                            current_str.insert(baseidx+cover_idx*2+1,cover_strx) # ['a','b','a','b','a','b','a','c','a']
                            baseidx_impr=cover_idx*2+1+1  # 注意，本例中，对a序列填充b后，c的填充初始位需要增加6个
                        else:
                            numx.append((cover_strx,len(cover_str)-cover_idx)) # 多的填充字符 需要保留多余的那部分 本例是保留 ('c',2),为了避免下一轮填充时立即相遇，保留值要追加到尾部供最后填充
                            insert_status=False # 当前待填充的状态：填满
                            break # 跳出补位字符填充
                rst=current_str# 填充的部分追加到结果中，开始下一轮识别和填充
    print(msg)
    return ''.join(rst)


if __name__=='__main__':
    x='aaaaabbdbccc'
    new_x=neighbor_no_repeat(x=x)
    print(x,'=>\t',new_x)

    print()
    x='aaaabc'
    new_x=neighbor_no_repeat(x=x)
    print(x,'=>\t',new_x)

    print()
    x='好好的说说话'
    new_x=neighbor_no_repeat(x=x)
    print(x,'=>\t',new_x)

    print()
    x='aaaaaabbbbccccd'
    new_x=neighbor_no_repeat(x=x)
    print(x,'=>\t',new_x)






