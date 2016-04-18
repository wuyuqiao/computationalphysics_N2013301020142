#第二章 第19题 Level 1-2  
姓名：吴雨桥  
学号：2013301020142  
日期：2016年4月10日  
## 摘要  
## 背景介绍  
![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter2_new/%E6%A3%92%E7%90%83%E8%BF%90%E5%8A%A8%E7%A4%BA%E6%84%8F.gif)  
本文中主要讨论棒球运动中受到打击的棒球的运动规律。为了研究棒球的实际运动，我们必须要考虑两种不同的物理效应。其中一种效应是棒球的自旋；它对曲线球的运动轨迹有决定性的影响。另一种效应考虑到了棒球的质地（粗糙或光滑）对阻尼系数（drag coefficient）的影响，所谓“knuckleball”的运动轨迹与这第二种效应有关。  
## 不同质地的棒球的阻尼系数  
在《计算物理》一书的33页的图2.6中作者给出了对于不同质地的棒球，阻尼系数关于运动速度的函数关系。该图是一个经验图像，为了将之应用于后文中的计算中去，我在此对于每一种质地（光滑、普通、粗糙）的棒球的阻尼系数定义一个分段函数，使得分段函数的图像与经验图像尽可能相似。  
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter2_new/drag%20appr.png)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter2_new/drag%20coefficient%20define.py)  
点击图片可以获得绘图的源代码。这幅图与书中所给的经验图相比做了相当的简化，但是保留了转折点的值以及函数变化趋势。  
为了直观看到不同质地的棒球阻尼系数不同带来的轨迹的不同，我做了一个简单的模拟。以110mph(30.56m/s)的初速度，45°的角度，1m的挥棒高度将这三种不同的球击打出去，观察它们的运动轨迹。  
[![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter2_new/drag%20ball.png)](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter2_new/drag%20ball.py)  
点击图片以获得绘图源代码。  
 
  
## 自旋对棒球轨迹的影响  
棒球的自旋会使得空气对棒球产生一种力，流体力学中称为马格努斯力。  
![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter2_new/%E9%A9%AC%E6%A0%BC%E5%8A%AA%E6%96%AF%E5%8A%9B%E7%A4%BA%E6%84%8F%E5%9B%BE.jpg)   
理论推导表明，马格努斯力的大小与棒球自转的角速度、棒球的半径和棒球在空气中的运动速度有关。以S0表示空气对棒球的牵引力的平均效应，可得棒球所受马格努斯力的表达式为  
![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter2_new/%E9%A9%AC%E6%A0%BC%E5%8A%AA%E6%96%AF%E5%8A%9B%E5%85%AC%E5%BC%8F.png)  

  
 
