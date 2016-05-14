# 第十二次作业
姓名：吴雨桥  
学号：2013301020142  
日期：2016年5月13日  

![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Ex-12/gaps.jpg)  

## 摘要  
尽管太阳系中各个星球的运动已经被天文学家研究的比较透彻，我们仍然有一些有趣的问题值得探讨。首先是太阳系中最大的行星——木星对地球的引力作用使得日-地-木系统变为三体系统；其次是太阳系中的共振现象导致的Kirkwood断带和行星环;最后是土卫七的混沌运动。通过对这三个问题的探讨，我们可以加深对引力定律和开普勒定律的认识。  
## 日-地-木三体系统  
查询数据可知，太阳的质量约为木星质量的1000倍，地球质量的33万倍。木星质量约为地球质量的318倍。由此可知，在计算这个三体系统的运动，各种引力作用都要考虑。这里我们的系统总动量均为零，且木星的初速度不变。  
首先我们来看木星的质量为真实质量的情形。  
![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Ex-12/mj%3Dmj.png)  
由图可知，此时地球的轨道没有什么太大的变化。在近处观察可见，  
![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Ex-12/close%20earth%201.png)  
故此时地球轨道只是受到一些扰动。这与实际情况是相符合的。  
之后我们将木星质量变为真实值的十倍。  
![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Ex-12/mj%3D10mj.png)  
可见此时地球受到的扰动更大，但还是维持椭圆轨道。太阳也有了明显的运动。  
接下来我们将木星质量变为真实值的一百倍。  
![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Ex-12/mj%3D100mj.png)  
此时太阳有了明显的运动，地球围绕着太阳运动。  
最后我们让木星质量与太阳相等。  
![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Ex-12/mj%3D1000mj.png)  
由图可见，引力无法束缚住太阳和木星，它们相互远离。由于地球一开始与太阳距离更近，在之后地球跟随着太阳运动。  
之所以这个三体系统没有表现明显的混沌现象，是因为其中地球的质量太小了，对太阳和木星的影响只能算作围绕。这个系统的实质是太阳和木星组成的两体系统。地球只是相当于一个“试探质点”的角色。  
## 如果太阳系有三个太阳  
这里我们假设太阳系中有三个太阳，观察其中地球的运动。三个太阳之间距离为5AU，地球与其中一个太阳距离为1AU。  
![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Ex-12/3%20s.png)  
第一张图为三颗太阳的运动轨迹。不出所料的是，混沌现象出现在了这样的系统中。  
第二张图为地球与第一个太阳的轨迹。由于地球与第一颗太阳距离较近，故在后来也一直围绕着它运动。  
之后我们将地球放置在三颗恒星的中心位置，观察其运动。这里为简洁起见，只显示了地球的轨迹。
![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Ex-12/middle.png)  
可见，此时地球不随着任何太阳转动，其轨迹也是混沌的。
## 土卫七的混沌运动  
土卫七是土星的一颗卫星，其形状不是通常的球形。这里我们用一根细杆连接着的两个等质量质点来模拟土卫七。其角度会呈现混沌现象。  
当其质心做圆周运动时，  
![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Ex-12/heperion%201.png)  
此时，系统不呈现混沌现象。  
当其质心做椭圆运动时，  
![](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Ex-12/hyperion%202.png)  
此时，系统的角度变化呈现明显的混沌现象。  
