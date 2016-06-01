# 作业15 随机过程  
姓名：吴雨桥  
学号：2013301020142  
日期：2016年6月1日  
## 一、背景介绍  
![](http://www.anystandards.com/uploads/allimg/151104/1J24W527-6.jpg)  
本文中我们考虑这样一类系统，其中随机性占据重要位置。这些系统一般含有较大数目的“自由度”，比如一滴雨水中的大量水分子，或是一块铁磁体中的大量自旋。  
在这种系统中，尽管理论上每个粒子的运动可以由力学定律决定，但是这会带来天文数字的微分方程，难以实际求解。为此，我们使用概率论来描述这个系统，使得原系统和这个随机系统在某些我们感兴趣的宏观性质上一致。通过探究这个随机系统，我们可以了解真实系统的情况。  
## 二、左右等可能随机行走  
这里我们考虑一个典型的一维随机行走问题。行人初始时刻位于x=0处，步长为1，相邻的两步之间时间间隔固定（故步数正比于时间），每一步向左和向右概率均为0.5。我们假设有5000个相同的行人，观察他们运动的平均性质。  
他们距离原点的平均距离随步数的变化关系为  
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Ex-15/random%201.png)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Ex-15/random%20walk%201.py)  
点击图片得绘图代码。可见，由于每一步向左向右的概率相同，平均距离保持在0附近波动。  
他们距离原点距离平方随步数的变化关系为  
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Ex-15/random%202.png)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Ex-15/random%20walk%202.py)  
点击图片得绘图代码。x的平方的平均值与步数近似为线性关系，这种线性关系表明这个随机行走的过程是“类扩散的”。  
接下来我们将情况一般化，此时每一步的步长为-1~+1之间的一个值。此时两个平均值随步数的变化关系为  
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Ex-15/random%203.png)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Ex-15/random%20walk%203.py)  
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Ex-15/random%204.png)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Ex-15/random%20walk%204.py)  
点击图片获得绘图代码。由图可知，此时的x的平方的平均值与步数近似为线性关系，此过程也是“类扩散的”。  

