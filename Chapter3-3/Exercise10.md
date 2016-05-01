# 第十次作业 3.26、3.29、3.33及其3D展示 
姓名：吴雨桥  
学号：2013301020142  
时间：2016年4月27日  
## 摘要  
本文使用Euler法通过数值计算研究了Lorenz模型和台球问题，并回答了书上的3.26、3.29和3.33题，并使用Vpython进行了3D展示。  
## Lorenz模型  
![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3-3/Lorenz_Attractor.gif)  
大气物理学家Lorenz在研究Rayleigh-Benard问题时，将流体力学基本方程组Navier-Stokes方程组化简为简单形式：
![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3-3/Lorenz%20equations.png)  
这个方程组被称为Lorenz方程组，或Lorenz模型。其中x,y,z为变量，其余为常数。  
## Lorentz模型在不同r下的行为
接下来我们考察Lorenz模型的行为。我们令sigma=10，b=8/3，改变r的大小，观察z随时间的变化情况（x与y将呈现相似的行为）。在这个模型中，r代表了流体顶部与底部的温度差，类似于单摆问题中外界驱动力的地位。  
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3-3/z%20versus%20time%20for%20different%20r.png)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3-3/z%20vs%20t.py)  
点击图片以获取绘图的源代码。由图可知，当r=5时，图像一开始有一点振荡，随后振幅衰减，z变成一个与时间无关的常数。当r=10时，图像的特征相似，只是振幅衰减所花的时间要更长一些。这两种情况对应于流体中的稳定对流运动。它类似于非混沌单摆的运动模式。当r=25时，图像最终变为混沌状态。从非混沌到混沌状态的转变点为r=470/19，其推导过程在给老师的邮件中。  
## 相空间中的混沌lorenz模型  
接下来我们考察在相空间中z与x的关系。为此我们在x-z平面作图。各参数的选择与上文相同。
首先我们令r=5、10以使得系统处于非混沌状态。  
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3-3/nonchaotic.png)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3-3/Phase%20space%20nonchaotic.py)  
点击图片以获取绘图的源代码。有图可知，当系统处于非混沌状态时，其轨迹最终会收缩到相空间中的一个点，即代表系统处于稳定状态。
之后我们令r=25以使得系统处于混沌状态。  
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3-3/lorenz%202d.png)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3-3/Phase%20space.py)  
点击图片以获取绘图的源代码。由图可知，与混沌摆的情况类似，出现了奇异吸引子。由于它们出现在Lorenz模型中，习惯上被称为Lorenz吸引子。  
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3-3/Phase%203d.png)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3-3/phase%203d.py)  
点击图片以获取绘图的源代码。这是Lorenz吸引子的三维图示。  
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3-3/gif1.gif)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3-3/Phase%20space%20-%20Copy.py)  
点击图片以获取绘图的源代码。图中为Lorenz吸引子在三维相空间中形成的动态图示。  
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3-3/GIF2.gif)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3-3/2%20balls.py)  
点击图片以获取绘图的源代码。上图在相空间中显示了系统的混沌性。红色和绿色代表的系统初始位置仅仅在x坐标上相差0.1，但可以明显看出一段时间后两个系统的图像不再重合，差值变大。
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3-3/slice1.png)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3-3/slice1.py)  
点击图片以获取绘图的源代码。上图为r=25时Lorentz吸引子的截面图。左图为x=0时y-z平面，右图为y=0时x-z平面。  
## 通往混沌之路 
与物理摆类似的是，Lorenz系统随着r的增大，也会从周期状态逐渐变为混沌状态。这里我们考察该系统是如何变成混沌状态的。  
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3-3/road.png)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3-3/road.py)  
点击图片查看绘图的源代码。当r=160的时候，系统是周期性的。而当r=163.8的时候，系统开始出现一些非周期的因素，也就是开始变得混沌。一般来说，当r较小时为周期性的系统，随着r的增加，其非周期性会增强。   
## 台球在球场型桌面的运动  
台球在桌面上的运动是比较简单的运动，当桌面为正圆面时，其运动轨迹将为非混沌的。而当桌面为球场型时，其运动为混沌的。  

首先我们考察纯圆面的情况。  

[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3-3/circle%20taiqiu.gif)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3-3/circle%20taiqiu.py)  

点击图片以获取绘图的源代码。可见轨迹为对称的，表明系统是非混沌系统。  
接下来我们考察球场型的桌面。取alpha为0.1，台球在其上的运动轨迹为   

[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3-3/stadium.gif)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3-3/stadium%200.1.py)  
点击图片以获取绘图的源代码。可见，当桌面从正圆形变为球场型之后，台球的轨迹立刻变为混沌系统，这体现在轨迹并无明显的对称性上。   
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3-3/2d%20four%20kinds.png)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3-3/4%20kinds%202d.py)  
点击图片以获取绘图的源代码。上图为二维图，展现了随着alpha的增大，系统的混沌性增强的特点。  
之后我们在相空间中画出不同的alpha情况下，当y=0时，x方向上位置和速度的关系。  
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3-3/phase4.png)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3-3/phase4.py)  
点击图片以获取绘图的源代码。按照左上、右上、左下、右下的顺序分别为alpha为0、0.001、0.01、0.1的情况下相空间的情况。可见随着alpha的增大，原先的规则图像逐渐变得不规则。  
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3-3/sep.png)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter3-3/separate.py)  
点击图片以获取绘图的源代码。此图的纵坐标已经做了对数函数转换。由图可知，初始位置相差仅为10^(-5)的两个台球，在alpha=0.01的情况下，经过一段时间，其距离差会变得越来越大。
## 台球在内圆外方桌面的运动  
点击图片以获取绘图的源代码。这幅动图描绘了台球在一张内圆外方的桌子上的运动轨迹。由图可知，台球在这张桌子上的运动也是混沌运动。 
 
