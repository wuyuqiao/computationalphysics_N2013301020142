# 作业13 电磁场分布的数值求解  
姓名：吴雨桥  
班级：13级弘毅班  
日期：2016年5月23日  
## 背景介绍  
![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Ex13/electric.jpg)  
上图表示空间中电磁场的一种可能分布。  
在不存在电荷的空间中，电势的分布遵循拉普拉斯方程:  
![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Ex13/Laplace.png)  
如果加上边界条件，理论上我们就可以解出电势V。但是除了一些特殊的边界条件以外，对于这类问题我们难以得到解析解。所以我们必须使用数值计算的方法，得到电势的数值解。理论分析表明，对于本文中所讨论的情况，二维网格化离散的情况下，非边界上的点的电势相等于其周围最近的四个点的电势的平均值。  
在本文中我们使用的方法是relaxation method，这种方法可以用来数值求解以拉普拉斯方程为代表的一类所谓的“椭圆偏微分方程”。  
这种方法也是有不同的版本，最简单的一种是Jacobi方法。Jacobi方法的精髓是从一个符合边界条件的猜测解开始，通过迭代，使得数值解收敛于真实的解。  
Jacobi方法的改进版是Gauss-Seidel方法。在计算中，我们总是算完一个点再算另一个点，也就是逐点更新计算结果。该方法主要的改进是在计算某一点的电势时，使用之前的点已经更新后的数据。  
Gauss-Seidel方法的改进版是simultaneous over-relaxation （SOR）方法。在这种方法中引入了参数alpha，从而增大了收敛速度。
