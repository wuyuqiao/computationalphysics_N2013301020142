# 第三章 第8题  
姓名：吴雨桥  
学号：2013301020142  
日期：2016年4月13日  
## 摘要  
本文简要讨论了单摆的运动，从最简单的简谐振动开始，分别讨论了阻尼、外界驱动力、非线性现象等因素的影响。并以此为基础，解答了第三章第8题。  
##背景介绍  
![单摆](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/chapter3/%E5%8D%95%E6%91%86%E7%A4%BA%E4%BE%8B.gif.gif)  
如我们所知，振动现象在自然界中比比皆是，比如电子在原子中的运动、行星运动以及弹簧振子的运动。其中最为我们所熟知、也是被研究地最透彻的就是单摆。单摆由一个支点、一个质点与其间连接着的绳索组成。在最理想的情况下，阻尼为零，外界驱动力为零，不考虑非线性现象，绳索与垂直方向的夹角很小。此时，单摆的运动可以近似为简谐振动。而当我们考虑一个实际的单摆时，就不得不考虑那些影响因素。这时，单摆的运动可能会非常复杂，甚至其运动轨迹对初值的依赖性会非常大，也就是产生所谓的“混沌”现象。  
##单摆的简谐运动  
![单摆的简谐运动](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/chapter3/%E5%8D%95%E6%91%86%E7%9A%84%E7%AE%80%E8%B0%90%E8%BF%90%E5%8A%A8.jpg)  
首先考虑一个质量为m的粒子，它被一条质量为零的绳索链接在一个固定的支点上。假设粒子只受到两种力的作用，即重力与绳索施加在其上的张力。在平行于绳索的方向上合力显然为零。在垂直于绳索的方向上，相关的方程为：  
![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/chapter3/%E5%85%AC%E5%BC%8F1.png)  
第一个方程是该方向上的合力表达式，在此我们取逆时针方向为角度的正方向，故等号的右侧有一个负号。  
由牛顿第二定律，第一个方程可以转化为粒子在弧线上的运动方程。由于绳长不变，故运动方程可以转化为上述第二个方程。其中g表示重力加速度，l表示绳索的长度。  
第二个方程的解析解是第三个方程。由此我们可以看到，在简谐振动的情况下，角度随时间的变化是正弦函数的形式，并且振动的幅度不会衰减。振动的角速度由重力加速度和绳长的比值决定，而与粒子的质量和振动的幅度无关。  
由此我们可以使用Euler-Cromer方法数值解出角度与时间的关系。与我们的解析分析相同，数值解为正弦函数形式。  
为证明数值解的结果与解析解的结果是相同的，我选择了三个等长为1的摆，在9.8的重力加速度下，分别在角度为45°，90°，22.5°的情况下由静止释放，观察它们的运动状态。  
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/chapter3/%E4%B8%89%E4%B8%AA%E5%8D%95%E6%91%86%E4%BA%8C%E7%BB%B4.png)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/chapter3/%E5%8D%95%E6%91%86%E4%BA%8C%E7%BB%B4%E5%9B%BE.py)   
点击上图以获取绘图的源代码。由图可知，这三种情况下的单摆的角度随时间变化的关系正是正弦函数关系，这就验证了解析解和数值解的一致性。由于我设定每个单摆都是从一定角度由静止状态自由开始运动，故各个单摆的振动幅度仅由初始位置决定，并且在这里的无外界干扰状态下保持不变。由于单摆的振动频率仅仅取决于绳索的长度与重力加速度的大小，而这两个量对于这三个单摆都是相同的，故由图可知其周期相等。  
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/chapter3/%E4%B8%89%E4%B8%AA%E5%8D%95%E6%91%86.gif)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/chapter3/%E5%8D%95%E6%91%86%E5%8A%A8%E6%80%81%E7%A4%BA%E6%84%8F.py)   
点击上方gif图以获取绘图的源代码。在这里，我在三维空间中呈现了这三个单摆运动的动态情形。红色天花板下初始角度为45°，绿色下为90°，蓝色下为22.5°。  
## 单摆的阻尼振动  
有阻尼且没有外界驱动力的单摆的振动幅度一般不会保持一个常数，而是会逐渐衰减。这种阻尼振动又根据阻尼的大小细分为三种情况。当阻尼比较小时，单摆振动的幅度逐渐减小，但是还是能完成若干次周期运动的成为弱阻尼振动。当阻尼很大，单摆连一次周期振动都无法完成，只是慢慢回到平衡位置就停止了，这被称为过阻尼振动。如果阻尼的大小刚好使得单摆无法完成周期振动，同时又最快回到平衡位置，这被称为临界阻尼振动。  
在有阻尼的情况下，单摆的振动方程可以进行改写：  
![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/chapter3/%E9%98%BB%E5%B0%BC%E6%8C%AF%E5%8A%A8%E6%96%B9%E7%A8%8B.png)  
显然，第一个方程只是原来的运动方程的改动版，在等号右侧加入了阻尼项。阻尼项之所以正比于角速度，是因为实验上发现阻力一般与物体的速度成反比关系。第二个方程是弱阻尼情况下的振动方程，第三个是过阻尼情况下的方程，第四个是临界阻尼情况下的方程。  
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/chapter3/%E9%98%BB%E5%B0%BC%E6%91%86%E4%BA%8C%E7%BB%B4%E5%9B%BE.png)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/chapter3/damped%20pendulum%202d.py)  
点击图片来获得绘图的源代码。如图为三个阻尼系数q不同的单摆，其初始角度均为45°，初始速度均为0。在这三条曲线中，q=0.1时为弱阻尼情况，单摆振动的幅度逐渐下降，在完成若干个周期振动之后停止在平衡位置。q=1时为过阻尼情况，振幅迅速下降，停止在平衡位置。q=0.8时近似为临界阻尼情况，可见和过阻尼情况十分相似，但是振幅下降的速度要快一些。  
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/chapter3/%E5%8D%95%E6%91%86%E9%98%BB%E5%B0%BC3d.gif)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/chapter3/%E5%8D%95%E6%91%86%E9%98%BB%E5%B0%BC3d.py)  
点击动图来获得绘图的源代码。这里的动图显示了有阻尼情况下单摆的运动形式。在红色板、绿色板和蓝色板下面分别是q=0.1，q=0.8和q=1.0的单摆。  
## 有外力驱动下的有阻尼单摆  
之后我加入了外界驱动力，考察此时的单摆运动。因为所有的外力的函数可以分解为若干正弦函数的组合，故我在此假设外力是正弦函数形式。这样单摆的动力学方程可以写成  
![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/chapter3/%E5%A4%96%E5%8A%9B%E6%96%B9%E7%A8%8B.png)  
显然，单摆最终做正弦运动，其振幅由单摆固有频率，外力频率和阻尼系数共同决定，其频率等于外力的频率。  
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/chapter3/%E5%A4%96%E5%8A%9B2d.png)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/chapter3/%E5%A4%96%E5%8A%9B%E4%BA%8C%E7%BB%B4.py)  
点击图片查看绘图的源代码。由此图可知，单摆的振幅先变化震荡一段时间，后来做简谐振动，振动频率与外力频率是一致的。这与解析解是相符的。  
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/chapter3/%E5%A4%96%E5%8A%9B3d.gif)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/chapter3/%E5%A4%96%E5%8A%9B3d.py)   
点击动图来获得绘图的源代码。此动图模拟了有阻尼的单摆在频率为5的，幅度为1的外力作用下的运动状态。  
## 非线性单摆  
到现在我们都认为单摆的运动是线性的，而现实中单摆的运动是非线性的。我现在考虑无阻尼、无驱动力的非线性单摆。其运动方程为  
![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/chapter3/%E9%9D%9E%E7%BA%BF%E6%80%A7%E8%BF%90%E5%8A%A8%E6%96%B9%E7%A8%8B.png)  
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/chapter3/nonlinear%202d.png)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/chapter3/%E9%9D%9E%E7%BA%BF%E6%80%A72d.py)  
点击图片以获得绘图的源代码。由图可知，即使是非线性的单摆，在无阻力且无外界驱动力的情况下也是做周期运动。同时可以发现，初始角度较大的非线性单摆的周期也较长。  
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/chapter3/nonlinear%203d.gif)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/chapter3/nonlinear%203d.py)   
点击动图以获得绘图的源代码。这个动图红色板下的单摆初始角度为45°，绿色版下的初始角度为90°。这里在三维空间中显示了非线性单摆的运动状态。 
## 非线性单摆下振动幅度与振动周期之间的关系。  
第八题的要求是在非线性单摆的基础上，找出其振动幅度与振动周期之间的关系。由于我设定单摆由一定角度由静止状态释放，所以振动幅度只取决于初始角度。为了探究这一关系，我选定了一系列初始角度，计算出各自的周期，然后通过作图观察它们之间的关系。  
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/chapter3/%E7%AC%AC%E5%85%AB%E9%A2%98.png)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/chapter3/find.py)  
点击图片以获得绘图的源代码。图中两条曲线的参数均相同，唯一的区别是蓝线表示非线性过程，绿线表示线性过程。  
由图可知，在非线性单摆的运动过程中幅度与周期的规律为：当幅度较小时，其周期接近于一个常数，于线性单摆的性质相似；而随着振荡幅度的增加，单摆的周期也随之增加。  
经过解析分析，非线性单摆的解析解为  
![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/chapter3/%E9%9D%9E%E7%BA%BF%E6%80%A7%E8%A7%A3%E6%9E%90%E8%A7%A3.png)  
方程中K为第一类完全椭圆积分。  
![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/chapter3/%E8%A7%A3%E6%9E%90%E8%A7%A3%E5%9B%BE.jpg)  
上图为解析解的图像，此处只是展现解析解的变化性质，具体参数与上一幅图并不一致。  
## 结论  
对于非线性的单摆，其幅度与周期的关系的解析解为：  
![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/chapter3/%E9%9D%9E%E7%BA%BF%E6%80%A7%E8%A7%A3%E6%9E%90%E8%A7%A3.png)   
数值解的图像为：  
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/chapter3/%E7%AC%AC%E5%85%AB%E9%A2%98.png)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/chapter3/find.py)    
由图可知，在非线性单摆的运动过程中幅度与周期的规律为：当幅度较小时，其周期接近于一个常数，于线性单摆的性质相似；而随着振荡幅度的增加，单摆的周期也随之增加。  
## 参考文献   
1.百度百科 单摆词条  
2.计算物理 Nicholas J.Giordano, Hisao Nakanishi  
