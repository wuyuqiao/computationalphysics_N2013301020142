#Homework of chapter 2
##Abstract  
###Question 2.9:  
Calculate the trajectory of our cannon shell including both air drag and the reduced air density at high altitudes so that you can reproduce the results in Figure 2.5. Perform your calculation for different firing angles and determine the value of the angle that gives the maximum range.  
###Problem  
作业L1 2.9题  

作业L2 2.10题强化版（引入风阻）————“辅助精确打击系统”  

作业L3 发展“超级辅助精确打击系统”（考虑炮弹初始发射的时候发射角度误差1%，速度有5%的误差，风阻误差10%，可以考虑引入Coriolis force等，以炮弹落点与打击目标距离差平方均值最小为优胜）

##Background  
The Euler method we used to treat the problem in chapter 1 can easily be generalized to deal with motion in two spatial dimensions. To be specific, we can consider a projectile such as a shell shot by a cannon. If we ignore the air resistance, the equations of motion, which are again obtained from Newton's second law, can be written as  
![1](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter2/1.png)  
where x and y are the horizontal and vertical coordinates of the projectile, and g is the acceleration due to the gravity. These are second-order differential equations.  
To make it easier to handle, we write each of these second-order equations as two first-order differential equations  
![2](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter2/2.png)  
where vx and vy are the x and y components of the velocity. While we now have twice as many equations to deal with, we can use our standard Euler approach to solve each one. To use the Euler method, we write each derivative in finite difference form,  
![3](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter2/3.png)  
Then we add the correction due to air resistance and air density, then the equations change to,  
![4](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter2/4.png)  
Because we calculate the coordinates of the shell in a discrete way, it is inevitable that y<0 for the last point. To avoid this awkward situation, we just need to use the equation,  
![5](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter2/5.png)  
to calculate x coordinate of the landing point, and set the y coordinate of it to be zero. Then this landing point will take the place of last point in which y<0.



##Main text  
###1. Level 1  
To reproduce Figure 2.5, I write two functions which can do the calculation with or without the air density correction. In each function, first I designed four lists represent x coordinate, y coordinate, x component of velocity, y component of velocity. Then I set the value of some constants. For example, I set the original velocity to be 700m/s. Next, there is a loop that do the calculation until y<0. Then I use landing point to take the place of last value in the coordinate lists. After the calculation, the functions return a tuple containing the lists of x coordinate and y coordinate.  
After the design of calculating functions, I use matplotlib to reproduce Figure 2.5.  
If you want to check the code to reproduce Figure 2.5, [please click here.](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter2/reproduce%202.5.py)   
This is the reproduction of Figure 2.5:  
![1](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter2/figure_1.png)  
From the diagram, we can make a few comments about this problem:  
1. In consistence with what we have learned in the classical mechanic, when a cannon fire at angle 45 degree, the shell will reach the highest point.  
2. With air density correction, the shells move higher and farther than those without air density correction. This is because density correction says that in higher space, the density of air will decrease, so the air resistance will decrease which permits the shell to move higher and farther.  
Then I need to perform the calculation for different firing angles and determine the value of the angle that gives the maximum range. First I need to know the variation tendency of range when the firing angle changes. So I change the code([click to check code](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter2/tendency.py)) and make a graph showing the tendency:  
![2](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter2/tendency.png)  
From this figure, we can see that with the increment of firing angle, the range increase at first, then decrease to zero. It is at somewhere near pi/4 that the range reaches its maximum.  
Then I locate the angle where range reaches maximum.  
[click to check the code](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter2/max.py)  
The result of the calculation is: With the error of range smaller than 1 meter, considering the corrections, when a cannon fire a shell with the original speed 700m/s, the maximal range of it is 24731m, and the angle is 43.87 degree.  
###2.level 2  
Level 2 asks us to design a system that can help the cannon fire the shells which can hit the targets accurately. And the target is not just at the ground, its x coordinate and y coordinate can be arbitrary. Now the problem is : the observer of the cannon group tell the operator of cannon that there is a valuable target whose coordinates is (x,y), and the wind is along the x direction with a specific speed. Then how should the operator adjust the cannon so that the shells can hit a place as close as possible.  
To solve this problem, we will not adjust the velocity of shell(which can be adjusted by changeing the amount of powder we put in the cannon) and the firing angle(which can be adjusted by changeing the direction of the cannon gun). Instead, I put forward two system, one of them take the coordinate of target, the firing angle, the speed of the wind and the accuracy(represent the length of the zone that the shell will hit, of course, the target is within this zone) as input, and give the operator the needed velocity of shell. Another system will take the coordinate of target, the original velocity of shell, the speed of the wind and the accuracy as input, and give the operator the needed firing angle.  
[Click me to get the code of the velocity adjustment system.](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter2/velocity%20adjust.py)  
The basic idea of this code is there is a tendency that with a given angle, the bigger the original velocity of shell, the farther the shell will go. So we just need to fire at a random velocity, then collect the x coordinate of hit point. If its x is smaller than the target's, then next time we add the velocity a little. If x is larger than the target's, then next time we subtract the velocity a little. Then this process will continue until the x coordinate of the last hit point is within the accuracy.  
Now this system can hit a target 25000 meters away with accuracy less than 1 meter. That is to say, the shell will hit a place whose distance to the target no more than 0.5 m. I think that distance is close enough to assure that the target will be destroyed.  
[Click me to get the code of the angle adjustment system.](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter2/angle%20adjust.py)  
The idea of this angle adjustment system is very similar with the velocity adjustment system. Here is the difference:  
1. With a given velocity, there exists a maximal range that the shell can go to. So a target beyond that maximal range cannot be get.  
2. The total tendency of range with the increment of angle is that it grow from zero to the maximum, then it decrease to zero again. So for a target within the maximal range, there will be two different angles that can satisfy the need.  
So first I find the maximum point. Then if the target is beyond the maximal range, the code just tell us that target cannot be reached with the given input. If the target is just at the maximum point, the code just give us the data of the maximal point. If the target is within the maximal range, then we set the maximal point as the start point and use the same process in velocity adjustment system to find two angle that within the accuracy of hit point. Next we compare this two angle and choose the one whose x coordinate of hit point is closer.   
Like the velocity adjustment system, now this system can hit a target 25000 meters away with accuracy less than 1 meter. That is to say, the shell will hit a place whose distance to the target no more than 0.5 m. I think that distance is close enough to assure that the target will be destroyed.  
###3. Level 3  
In this level, to simulate the true world, we assume that the parameters obey normal distribution. I write code which takes these parameters as random variable which obey certain normal distribution.With the help of angle adjustment system, the code carries on a hundred shell firing experiment, then we calculate the standard deviation of the distance between the hit points and target(Calculating the average value of them is meaningless, as we know that it will be very close to the x coordinate of target if the parameters do obey normal distribution).  
[Click to get the code in this level.](https://github.com/wuyuqiao/computationalphysics_N2013301020142/blob/master/Chapter2/trial.py)  
In my experiment, as the problem asked, I set the error of original velocity 5%, the error of angle 1%, the error of speed of wind 10%, the number of firing events 100. The target is 20000m away,100 m high, the average original velocity is 700 m/s, the average speed of wind is 3 m/s.   
The result is 1273.4868971819358 m. Considering the distance between cannon and target is 20000m, the error is 6.365%, which is of the magnitude of the parameters' errors.        
##Conclusion  
1. when a cannon fire at angle 45 degree, the shell will reach the highest point.  
2. With air density correction, the shells move higher and farther than those without air density correction.  
3. With the increment of firing angle, the range increase at first, then decrease to zero.  
4. With the error of range smaller than 1 meter, considering the corrections, when a cannon fire a shell with the original speed 700m/s, the maximal range of it is 24731m, and the angle is 43.87 degree.    
5. The two systems in level 2 that I designed can make sure that if the parameters can be specified, the distance between hit poing and target is less than 1m.  
6. The randomness in firing parameters will greatly increase the error. 
