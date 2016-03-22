#Homework of chapter 1  Question 1.5  
##Abstract  
###Question 1.5:  
Consider again a decay problem with two types of nuclei A and B, but now suppose that nuclei of type A decay into ones of type B, while nuclei of type B decay into ones of type A. Strictly speaking, this is not a "decay" process, since it is possible for the type B nuclei to turn back into type A nuclei. A better analogy would be a resonance in which a system can tunnel or move back and forth between two states A and B which have equal energies. The corresponding rate equations are   
![rate equtions](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter1/Picture1%20for%20chapter%201.png)  
where for simplicity we have assumed that the two types of decay are characterized by the same time constant, tau. Solve this system of equation for the numbers of nuclei, NA and NB, as functions of time. Consider different initial conditions, such as NA=100, NB=0, etc, and take tau=1s. Show that your numerical results are consistent with the idea that the system reaches a steady state in which NA and NB are constant. In such a steady state, the time derivatives dNA/dt and dNB/dt should vanish.  
##Background  
From the rate equations, it is not hard to recognize that this is a first-order ordinary differential equation set. With Euler method which is particularly useful when you want to get some numerical answers of this kind of first-order ordinary differential equations.   
The main idea of Euler method is based on the Taylor expansion:  
![Taylor expansion](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter1/Picture%202%20for%20chapter%202.png)   
If we take the increment of t to be quite small, it's a good approximatioin to simply ignore the terms that involve second and higher powers of the change of time, leaving us with:  
![approximation](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter1/picture%203%20for%20chapter%201.png)  
With this kind of approximation and the original first-order differential equations in Abstract section, keeping in mind that the question asked us to take time constant oto be 1, then it is very easy for you to see that:  
![picture](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter1/PICTURE%204.png)  
Given that we know the value of NU at some value of t, we can use these equations to estimate its value a time step later. If we follow this process, we can easily get its value two time steps later, three time steps later,......and this is the essential content of Euler method.  
##Main text  
###1.Thinking process  
Following the Euler method, I designed several steps to get the numerical answer of this problem.  
First, I initialized the parameters and variables that we needed in the code.  
Second, I did the real calculation to get lists of NA, NB and time(which I use t to represent).  
Third, with the help of matplotlib and numpy, I used the lists that obtained in the last step as data to draw several pictures with different initial conditions.   
Fourth, with pictures drawed in the third step, I found my numerical results are consistent with the idea that the system reaches a steady state in which NA and NB are constant.  
###2.Code  
This code asks users to input the initial conditions, and give users a picture showing the variation tendency of NA and NB. If you would like to see the raw code, [please click here.](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter1/chapter1.py)  
   
    #Initialize parameters

    print 'Please declare the initial situation that we need to continue: '

    na_0=float(raw_input('The initial number of A: '))
    nb_0=float(raw_input('The initial number of B: '))
    t_0=float(raw_input('The initial number of time: '))
    dt=float(raw_input('The time step is: '))
    na=[na_0]
    nb=[nb_0]
    t=[t_0]

    #Run the calculation

    for i in range(200):
        na_next=na[-1]+(nb[-1]-na[-1])*dt
        nb_next=nb[-1]+(na[-1]-nb[-1])*dt
        t_next=t[-1]+dt
        na.append(na_next)
        nb.append(nb_next)
        t.append(t_next)

    #Draw the picture

    from pylab import *


    nana=array(na)
    nbnb=array(nb)
    tt=array(t)

    plot(tt,nana,label='NA',color='b')
    plot(tt,nbnb,label='NB',color='r')
    grid(True)

    yticks([0,10,20,30,40,50,60,70,80,90,100])

    legend(loc='upper right',frameon=False)

    show()  
###3.Calculation based on different initial conditions  
The question asked us to do the calculation on different initial conditions. So I picked three different initial conditions(attention: because in this question, A and B have exactly the same status, so NA=100,NB=0 and NA=0, NB=100 are same. So, to make diffenent initial conditions, we need to change the ratio of A and B), those are:  
1.NA=100,NB=0  
The operation interface is   
![p1](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter1/picture%205.png)  
the variation tendency is   
![p2](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter1/picture%206.png)  
2.NA=100,NB=30  
The operation interface is  
![p3](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter1/picture%207.png)  
the variation tendency is  
![p4](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter1/picture%208.png)  
3.NA=100,NB=80  
The operation interface is  
![p5](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter1/picture%209.png)   
the variation tendency is  
![p6](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter1/pic%2010.png)   
##Conclusion  
It is clear from the pictures that:  
When NA=100 and NB=0 at the beginning, the system will reach a system where NA=NB=50.   
When NA=100 and NB=30 at the beginning, the system will reach a system where NA=NB=65.   
When NA=100 and NB=80 at the beginning, the system will reach a system where NA=NB=90.  
In general, in this question, no matter what the initial ratio of NA and NB is, the system will eventually reach a stable state where NA=NB=(NA(0)+NB(0))/2. This is consistent with the idea that the system reaches a steady state in which NA and NB are constant. In such a steady state that the time derivatives dNA/dt and dNB/dt should vanish which can also be observed from the graphes above.   


   
  

 
  

