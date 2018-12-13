# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 15:00:48 2018

@author: zhangyaxu

给定一个从小到大排序的数值型array或list，获得最大的合法排列的数量
合法的定义： 排列中靠后的值必须必靠前的值大，比如 2|3 是合法的， 3|2是非法的
"""

import pandas as pds


def most_permutation(x):
    # 1 基础处理，数据准备，参数准备
    z=pds.DataFrame([(xx,str(xx)) for xx in x],columns=['idx','val']) # 演变的基础数据，每次从此非数据中选出比尾部大的那几个单值 ，存了排列的尾部最大值 和排列本身，不可更新
    rst_df=z.copy()
    rst_df['sta']=0 # 判断尾部最大值是否已使用 ，可有可无，just为了好理解， 可更新，比如初始的[(1,'1'),] 更新可为[(2,'1|2')] ,注意 (1,'1')仍保留，只是状态sta变成了1
    sep='|' # 分隔符
    new_idx=z.idx.values  # 可能的尾部最大值，从小到大，由于z已排序过，所以无需再排序

    # 2 开始逐个生成排列
    for idxi in new_idx:
        #例 idxi=3
        val_idxi=rst_df.loc[(rst_df.idx==idxi)&(rst_df.sta==0),'val'].values.tolist() # 需要继续追加比尾部大的值的排列集合A, 若 idxi=3 的  A 包括 ['1|3','2|3',...] 是所有尾部值是3的排列集合
        can_append=z.loc[z.idx>idxi,['idx','val']].values.tolist()  # 从原生数据中找到比idxi大的值并追加到A的各排列的尾部
        rst=[(ca_ix,val_idxix+sep+ca_vx,0) for val_idxix in val_idxi for ca_ix,ca_vx in can_append] # 此时生成 [(4,'1|3|4',0),(4,'2|3|4',0),....] ,排列的尾部最大值被更新
        rst_df=pds.concat([rst_df,pds.DataFrame(rst,columns=['idx','val','sta'])],axis=0).reset_index(drop=True)  # 新的合法排列与旧的合并
        rst_df.loc[rst_df.idx==idxi,'sta']=1  # 标记本次的尾部值 idx=3的排列状态sta=1 表示已追加并生成了新排列
        #进入下一个循环，即更大的尾部值的排列的更新
    return rst_df

x=[1,2,3]
rst=most_permutation(x)
print('array is :',x,'\n',rst)
x=[1,2,3,4]
rst=most_permutation(x)
print('array is :',x,'\n',rst)

#--- 结果如下
'''
array is : [1, 2, 3] 
   idx    val sta
0   1      1   1
1   2      2   1
2   3      3   1
3   2    1|2   1
4   3    1|3   1
5   3    2|3   1
6   3  1|2|3   1

array is : [1, 2, 3, 4] 
    idx      val sta
0    1        1   1
1    2        2   1
2    3        3   1
3    4        4   1
4    2      1|2   1
5    3      1|3   1
6    4      1|4   1
7    3      2|3   1
8    4      2|4   1
9    3    1|2|3   1
10   4    1|2|4   1
11   4      3|4   1
12   4    1|3|4   1
13   4    2|3|4   1
14   4  1|2|3|4   1
'''


