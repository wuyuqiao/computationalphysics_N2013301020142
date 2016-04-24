# 第三章 第12、16、21题  
姓名：吴雨桥  
学号：2013301020142  
日期：2016年4月20日  
##摘要  
##背景介绍  
![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3---2/%E6%B7%B7%E6%B2%8C%20%E4%B8%8B%E8%BD%BD.jpg)  
图中的现象是混沌的典型特征。  
上一次的作业我讨论了外界驱动力、能量耗散和非线性这三种因素是如何分别作用于简单单摆并影响其运动轨迹的。在本次作业，我将讨论同时考虑这三种因素的单摆，也就是所谓的物理摆。物理摆有许多性质与简单单摆一致，但是也有很多自身独有的奇特性质。其中最重要的可能就是所谓的混沌现象。
## 不同驱动力下物理摆的运动  
在综合考虑了能量耗散、外力驱动和非线性之后，物理摆的运动方程可以写作：  
![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3---2/%E7%89%A9%E7%90%86%E6%91%86%E8%BF%90%E5%8A%A8%E6%96%B9%E7%A8%8B.png)  
接下来我选择重力加速度和摆长均为9.8，阻尼系数为0.5，外力频率为2/3，时间间隔为0.04.分别对外力幅度为0、0.5、1.2的情况绘制摆的角度与时间的关系图。  
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3---2/%E7%AC%AC%E4%B8%80%E5%BC%A0%E5%9B%BE.png)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3---2/%E7%AC%AC%E4%B8%80%E5%BC%A0%E5%9B%BE.py)  
点击图片以获得绘图的源代码。图中蓝色线表示外力为零的状态，可见没有外界驱动力下的单摆在阻力的影响下很快就停止了。图中绿线表示外力幅度为0.5时的运动，可见单摆在开始阶段将初始条件决定的运动通过阻力消耗后，在之后的运动中做与外力同频率的简谐振动。这两种单摆的运动与上一篇文章中描述的一样。红色的线表示外力幅度为1.2时的运动状态，可以看到，单摆的运动是没有周期性的，这就是混沌的特征。图中竖直的线是由于当角度超过180度时，程序将其角度自动减小360度，反之亦然。  
下图为角速度的变化情况。  
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3---2/%E7%AC%AC%E4%BA%8C%E5%BC%A0%E5%9B%BE.png)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3---2/%E7%AC%AC%E4%BA%8C%E5%BC%A0%E5%9B%BE.py)  
点击图片以获取绘图的源代码。由上图可见，三种单摆的角速度的变化特征与上面所述的角度的变化特征相似。这是显然的，因为角速度只不过是角度对时间的导数罢了。  
下图为三维情况下三种摆的运动状态。  
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3---2/%E7%AC%AC%E4%B8%80%E5%BC%A0GIF.gif)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3---2/%E7%AC%AC%E4%B8%80%E5%BC%A0GIF.py)  
点击动图以获取绘图源代码。最左方的红球表示外力为0的单摆，仅仅摆动了几下之后就静止了。中间的黄球表示外力为0.5的单摆，后来一直做与外力同频率的简谐振动。右方的绿球表示外力为1.2的混沌摆，其摆动轨迹是无法预测的，且摆动的幅度也比较大。  
## 混沌摆对初值的敏感性  
混沌摆的最大特征是当初值仅仅改变了一点点时，结果就会有极大的变化。为了示意这种情况，我选择两个摆，它们的初始角度仅仅相差0.001rad。之后观察它们分别在F=1.2（混沌）和F=0.5（非混沌）的情况下角度之差的变化规律。  
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3---2/%E7%AC%AC%E4%B8%89%E5%BC%A0%E5%9B%BE.png)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3---2/%E7%AC%AC%E4%B8%89%E5%BC%A0%E5%9B%BE.py)   
点击图片以获取绘图的源代码。这是F=1.2的情况下角度差的变化情况。可以明显看出，在混沌状态下，初始角度相差极小的两个物理摆的角度差随着时间推移会变大，最终趋于稳定，这种稳定是因为已经达到可能的最大差2pi。这表明混沌摆对初值敏感性很强。  
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3---2/%E7%AC%AC%E5%9B%9B%E5%BC%A0%E5%9B%BE.png)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3---2/%E7%AC%AC%E5%9B%9B%E5%BC%A0%E5%9B%BE.py)  
点击图片以获取绘图的源代码。这是F=0.5的情况下角度差的变化情况。从中可以看到，对于两个初始位置差异很小的非混沌摆，其角度差会迅速减小，最终趋于0.这表明非混沌摆对初值不敏感。 
  
  
