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
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3---2/%E7%AC%AC%E4%BA%8C%E5%BC%A0GIF.gif)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3---2/%E7%AC%AC%E4%BA%8C%E5%BC%A0GIF.py)  
点击动图以获取绘图的源代码。在动图中红色的球表示初始角度为0.2rad的摆，黄色的球表示初始角度为0.201rad的摆。绿色的球与中心连线与x轴正向的夹角表示两个摆之间的角度差。由图可知，两个混沌摆的夹角的变化没有规律，难以预测。
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3---2/%E7%AC%AC%E5%9B%9B%E5%BC%A0%E5%9B%BE.png)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3---2/%E7%AC%AC%E5%9B%9B%E5%BC%A0%E5%9B%BE.py)  
点击图片以获取绘图的源代码。这是F=0.5的情况下角度差的变化情况。从中可以看到，对于两个初始位置差异很小的非混沌摆，其角度差会迅速减小，最终趋于0.这表明非混沌摆对初值不敏感。  
## 混沌摆的角度与角速度的关系  
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3---2/fifth%20picture.png)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3---2/%E7%AC%AC%E4%BA%94%E5%BC%A0%E5%9B%BE.py)  
点击图片以获取绘图源代码。这是F=0.5，即非混沌情况下单摆的角度与角速度的关系。由图可见，除开最初的一段线，这关系基本上是一个椭圆，这表明对应每一个角度由两个角速度，反之亦然。最终的轨迹与初始值无关，这与上面的结论相合，也是符合简谐振动的规律的。  
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3---2/sixth.png)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3---2/%E7%AC%AC%E5%85%AD%E5%BC%A0%E5%9B%BE.py)  
点击图片以获取绘图的源代码。这是F=1.2，即混沌情况下的单摆的角度与角速度的关系。这里的图像明显比非混沌情况要复杂，但可以明显看出图像上的点并不是随机的，其中有一定的规律性。混沌系统一般都会显示这类的规律性。 [![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3---2/seven.png)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3---2/seven.py)  
点击图片以获取绘图的源代码。这张图是典型的Poincare图，与上一张图的不同是此图中只取了是驱动力周期倍数的时刻的情况。图中明显的结构是分形结构，被称作奇异吸引子，是混沌现象的一大特征：如果是非混沌情况，图中只会有一个点。而在混沌情况中图中会出现奇异吸引子。  
## level-1 3.12题 不同相位取值下奇异吸引子的变化情况  
在上文中的奇异吸引子的图中，我们取的是外力相位为0的时刻。在这里，我们探究一下取别的相位为基准时，奇异吸引子有什么变化。  
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3---2/eight.png)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3---2/eight.py)  
点击图片以获取绘图的源代码。这张图的时间取值是外力相位为+pi/2的时刻。  
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3---2/nine.png)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3---2/nine.py) 
点击图片以获取绘图的源代码。这张图的时间取值是外力相位为+pi/4的时刻。  
由这两张图连同上文中的一张图可以看出，这里明显随着相位从0到pi/4再到pi/2,奇异吸引子先向右上方、再向右下方运动。这表明随着相位的变化，奇异吸引子也相应的运动。  
## level-2 3.16题 参数有微小变化时奇异吸引子的变化情况  
接下来我们探究当参数有微小变化时奇异吸引子的变化情况。我们选择外力的幅度和频率作为参数，分别令幅度F=1.2，1.25,1.3和f=2/3,2/3+0.00001,2/3+0.00002，观察奇异吸引子的变化。  
首先是幅度变化时的情况：  
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3---2/ten.png)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3---2/ten.py)  
点击图片以获取绘图的源代码。由这三张图可以看出，当F增加时，奇异吸引子的位置没有发生改变，但其上的点逐渐减少，这表明系统在逐渐离开混沌状态 。  
之后是频率变化时的情况：  
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3---2/eleven.png)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3---2/eleven.py)  
点击图片以获取绘图的源代码。由这三张图可以看出，当外力频率每次以0.00001的大小增加时，奇异吸引子的位置基本没变，但其上的点逐渐增加，吸引子的在相空间中体积增大，表明其“吸引”能力在逐渐下降。  
## 通往混沌之路  
接下来我们研究单摆系统是如何从简谐振动变为混沌振动的。我们先考察F=1.35,1.44,1.465时角度随时间的变化关系。  
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3---2/12-1.png)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3---2/twelve.py)  
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3---2/12-2.png)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3---2/twelve.py)  
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3---2/12-3.png)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3---2/twelve.py)  
点击上方任一图片以获取绘图源代码。第一张图的周期与外界驱动力的相同，第二张图的周期是外力周期两倍，第三张图是外力周期四倍。由此我们可以看出，随着外力在这个范围内的增加，单摆的周期变为外力周期的两倍、四倍、八倍等等，最终进入混沌状态。   
为了更好地研究这一渐变过程，我们画所谓的bifurcation图。  


