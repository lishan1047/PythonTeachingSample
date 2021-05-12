'''
食堂满意度调查表
编号	性别	年龄	满意度
1	    1	    23	    4
2	    2	    43	    2
3	    1	    25  	3
4	    2	    47	    4
…			
# 采用NumPy 的二维数组表示问卷调查结果：
# （1）求解各个性别的人数及比例
# （2）按照[0,30)，[30,50)，[50,) 进行年龄分组，并计算每组人数分布
# （3）按照性别分组计算最大满意度、最小满意度、满意度均值、满意度标准差
# （4）按照[0,30)，[30,50)，[50,) 进行年龄分组计算最大满意度、最小满意度、满意度均值、满意度标准差
# （5）检测性别对满意度是否存在显著差异
# （6）检测年龄对满意度是否存在显著差异
# （7）检测性别、年龄共同对满意度是否存在显著差异
'''

import numpy as np

quest = np.array([[1,23,4],
                  [2,43,2],
                  [1,25,3],
                  [2,47,4],
                  [1,54,5]])

## 求解性别人数占比
count = len(quest)
print('男性：{:.2%}'.format(len(quest[quest[:,0]==1]) / count))
print('女性：{:.2%}'.format(len(quest[quest[:,0]==2]) / count))

## 求解年龄段人数分布
print('[0,30)：{:.2%}'.format(len(quest[(quest[:,1]>=0) & (quest[:,1]<30)]) / count))
print('[30,50)：{:.2%}'.format(len(quest[(quest[:,1]>30) & (quest[:,1]<50)]) / count))
print('[50,)：{:.2%}'.format(len(quest[(quest[:,1]>=50)]) / count))

## 按性别分组的最大满意度、最小满意度、满意度均值、满意度标准差
print('男性最大满意度：{}'.format(quest[quest[:,0]==1][:,2].max()))
print('女性最大满意度：{}'.format(quest[quest[:,0]==2][:,2].max()))
print('男性最小满意度：{}'.format(quest[quest[:,0]==1][:,2].min()))
print('女性最小满意度：{}'.format(quest[quest[:,0]==2][:,2].min()))
print('男性平均满意度：{}'.format(quest[quest[:,0]==1][:,2].mean()))
print('女性平均满意度：{}'.format(quest[quest[:,0]==2][:,2].mean()))
print('男性满意度标准差：{:.2}'.format(quest[quest[:,0]==1][:,2].std()))
print('女性满意度标准差：{:.2}'.format(quest[quest[:,0]==2][:,2].std()))

