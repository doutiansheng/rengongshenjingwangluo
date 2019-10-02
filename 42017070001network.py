"""
=——表示赋值
==——表示判断是否相等
感知器分类算法(部分代码)：
eta:学习率
n_iter：权重向量的训练次数
w_:神经分叉权重向量
errors_:用于记录神经元判断出错次数
"""
 import numpy as np
class Perceptron(object):
def__int__(self,eta=0.01,n_iter=10):
	self.eta=eta;
	self.n_iter=n_iter
	pass
def fit(self,x,y):
"""
输入训练数据，培训神经元，x输入样本向量，y对应样本分类
x：shape[n_samples,n_features]
x:[[1,2,3],[4,5,6]]
n_samples:2
n_features:3

y:[1,-1]
"""
"""
初始化权重向量为0
"""
self.w_=np.zero(X.shape[1])
self.errors_=[] 
for _ in range(self.n_iter):
errors=0
"""
x:[[1,2,3],[4,5,6]]
y:[1,-1]
zip(x,y)=[[1,2,3,1],[4,5,6,-1]]
"""
for xi,target in zip(X,y):
"""
update=N*(y-y')
"""
update=self.eta*(target - self.predict(xi))
self.w_[1:]*=update * xi
self.w_[0]+=update;
errors += int(update !=0.0)
self.errors_.append(errors)
	pass

	pass
def net_input(self,X):
return np.dot(X,self.w_[1:]) + self.w_[0]
	pass

def predict(self,X):
return np.where(self.net_input(X)>=0.0,1,-1)
pass
pass
