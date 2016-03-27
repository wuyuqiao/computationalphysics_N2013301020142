#第三次作业（level 1-2-3）  
##一、摘要  
###作业要求（摘自老师的Exercise.md文件）  
作业L1 在屏幕上用字符拼出自己姓名的英文  
作业L2 在屏幕上用字符拼出任意次序的姓名  
作业L3 在屏幕上用字符做出一份动画  
  
本次作业使用了python语言设计了代码，可以实现作业上的要求。在下方有附上具体代码，同时在Chapter1文件夹中可以看到代码的源文件，如需查看，请点击下方超链接。  
[L1 和 L2 的代码](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter1/Code%20for%20level%201-2)   
[L3 的代码](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter1/level%203.py)
  
##二、背景介绍      
对于level 1-2的作业，要实现打印出名字的功能，可以使用print函数。但是如果我们想用比较大的图形形式打印出来，就要编写程序来执行。我们可以选择5*5的格式来打印，这样能够清晰的辨认出来每个字母，同时又不会占用太大的屏幕空间。本次作业实际上显示了计算机屏幕显示字符的运行机制。  
对于level 3的作业，我的目标是让用户输入的任意字符串可以在一定的屏幕区域内弹来弹去（具体效果参见正文中的演示效果）。这个动画效果有几个重要的部分。首先要画出每一张图，这里我沿用了level 1-2的代码。然后使用延时效果，不断地清除上一张图，再打印出新的一张图。如果帧数够高，则人眼会认为这是动着的图像。这也是电影的原理。
##三、正文  
###1.level 1-2功能的实现  
1.显然可见，如果实现了作业L2所要求的功能，那么作业L1的功能亦可实现，故本文从一开始就注意在作业L2功能的实现。  
  
2.要拼出任意次序的姓名，要先考察姓名的基本组成。如作者的姓名是YUQIAO WU，其基本的组成元素是英文字母，而字母一共有26个。本文设想当字母显示在屏幕上时，每个字母应该是由#和空格组成的图形。比如字母A应该显示为:  
![A](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter1/%E5%AD%97%E6%AF%8DA.png)  
此图中的A字母是显示在一个5*5的矩阵上。  
  
3.显然这需要用到print函数。而print函数是一行一行打印的，故本文将每一个字母按行数分为五行，每行单独用一个名称表示。比如对于字母A，用a1代表第一行，a2代表第二行，如此类推。比如a1=' '*2+'#'+' '*2。同时还要单独列一个5*5矩阵表示空格矩阵。  
  
4.用#号和空格表示出每一个字母的每一行后，要将每一个字母的五行单独统一起来。于是对于每个字母生成一个列表，列表中的元素就是该字母的五个行的表示名称，这也就是定义每个字母。如aa=[a1,a2,a3,a4,a5]。  

5.当用户输入名字的时候，程序应该能将名字中的单个字母与程序中定义了的字母进行联系，故我们定义一个字典，将string格式的字母与上面定义了的图形的字母对应起来。  

6.把每个字母的图形格式编写好之后，需要按行把名字按行打印出来。由于每个字母都是在5*5的矩阵上编写的，我们需要首先打印出所有字母的第一行，之后打印出所有字母的第二行、第三行、第四行和第五行。这样一共有五行的打印任务，我们编写五个函数来实现。  

7.有了这五个函数之后，再编写一个总函数以执行上一步的五个函数，命名为bigpattern，有一个自变量，取用户输入的字符串为该自变量。函数的作用就是将输入的字符串用图形形式打印出来。  

###2.level 3功能的实现  
1.首先，要修改level 1-2的代码，定义一个函数，这样每次执行它的时候，就会生成一张新的图。  

2.然后，定义图像“移动”的方向，我设定为左上、左下、右上、右下四个方向。  

3.再次，当图像中的字符串“撞墙”的时候，它应该可以自动按照反射定律调整运行方向，于是我定义了一个change函数做这件事。  

4.最后，我定义了run函数，它是一个while True的死循环结构，来保证图像一直在动。它的作用是：打印出一副新图像，检查是否"撞墙",设定下一张图的参数，暂停一个较小的时间间隔，清空屏幕。然后就如此循环下去。 
###3.python代码  
1.level 1-2的代码  
  
    #定义每个字母的每一行
    a1=' '*2+'#'+' '*2
    a2=' '+'#'+' '+'#'+' '
    a3='#'+' '*3+'#'
    a4='#'*5
    a5='#'+' '*3+'#'
    b1='#'*4+' '
    b2='#'+' '*3+'#'
    b3='#'*4+' '
    b4='#'+' '*3+'#'
    b5='#'*4+' '
    c1='#'*5
    c2='#'+' '*4
    c3='#'+' '*4
    c4='#'+' '*4
    c5='#'*5
    d1='#'*4+' '
    d2='#'+' '*3+'#'
    d3='#'+' '*3+'#'
    d4='#'+' '*3+'#'
    d5='#'*4+' '
    e1='#'*5
    e2='#'+' '*4
    e3='#'*5
    e4='#'+' '*4
    e5='#'*5
    f1='#'*5
    f2='#'+' '*4
    f3='#'*5
    f4='#'+' '*4
    f5='#'+' '*4
    g1='#'*5
    g2='#'+' '*4
    g3='#'+' '+'#'*3
    g4='#'+' '*3+'#'
    g5='#'*5
    h1='#'+' '*3+'#'
    h2='#'+' '*3+'#'
    h3='#'*5
    h4='#'+' '*3+'#'
    h5='#'+' '*3+'#'
    i1='#'*5
    i2=' '*2+'#'+' '*2
    i3=' '*2+'#'+' '*2
    i4=' '*2+'#'+' '*2
    i5='#'*5
    j1='#'*5
    j2=' '*2+'#'+' '*2
    j3=' '*2+'#'+' '*2
    j4='#'+' '+'#'+' '*2
    j5=' '+'#'*2+' '*2
    k1='#  ##'
    k2='# #  '
    k3='##   '
    k4='# #  '
    k5='#  ##'
    l1='#    '
    l2='#    '
    l3='#    '
    l4='#    '
    l5='#####'
    m1='#####'
    m2='# # #'
    m3='# # #'
    m4='# # #'
    m5='# # #'
    n1='#   #'
    n2='##  #'
    n3='# # #'
    n4='#  ##'
    n5='#  ##'
    o1=' ### '
    o2='#   #'
    o3='#   #'
    o4='#   #'
    o5=' ### '
    p1='#### '
    p2='#   #'
    p3='#### '
    p4='#    '
    p5='#    '
    q1='#### '
    q2='#  # '
    q3='# ## '
    q4='#### '
    q5='    #'
    r1='#### '
    r2='#   #'
    r3='#### '
    r4='# #  '
    r5='#  ##'
    s1='#####'
    s2='#    '
    s3='#####'
    s4='    #'
    s5='#####'
    t1='#####'
    t2='  #  '
    t3='  #  '
    t4='  #  '
    t5='  #  '
    u1='#   #'
    u2='#   #'
    u3='#   #'
    u4='#   #'
    u5='#####'
    v1='#   #'
    v2='#   #'
    v3=' # # '
    v4=' # # '
    v5='  #  '
    w1='# # #'
    w2='# # #'
    w3='# # #'
    w4='# # #'
    w5='#####'
    x1='#   #'
    x2=' # # '
    x3='  #  '
    x4=' # # '
    x5='#   #'
    y1='#   #'
    y2=' # # '
    y3='  #  '
    y4='  #  '
    y5='  #  '
    z1='#####'
    z2='   # '
    z3='  #  '
    z4=' #   '
    z5='#####'
    wu1='     '
    wu2='     '
    wu3='     '
    wu4='     '
    wu5='     '  
    #定义每个字母
    aa=[a1,a2,a3,a4,a5]
    bb=[b1,b2,b3,b4,b5]
    cc=[c1,c2,c3,c4,c5]
    dd=[d1,d2,d3,d4,d5]
    ee=[e1,e2,e3,e4,e5]
    ff=[f1,f2,f3,f4,f5]
    gg=[g1,g2,g3,g4,g5]
    hh=[h1,h2,h3,h4,h5]
    ii=[i1,i2,i3,i4,i5]
    jj=[j1,j2,j3,j4,j5]
    kk=[k1,k2,k3,k4,k5]
    ll=[l1,l2,l3,l4,l5]
    mm=[m1,m2,m3,m4,m5]
    nn=[n1,n2,n3,n4,n5]
    oo=[o1,o2,o3,o4,o5]
    pp=[p1,p2,p3,p4,p5]
    qq=[q1,q2,q3,q4,q5]
    rr=[r1,r2,r3,r4,r5]
    ss=[s1,s2,s3,s4,s5]
    tt=[t1,t2,t3,t4,t5]
    uu=[u1,u2,u3,u4,u5]
    vv=[v1,v2,v3,v4,v5]
    ww=[w1,w2,w3,w4,w5]
    xx=[x1,x2,x3,x4,x5]
    yy=[y1,y2,y3,y4,y5]
    zz=[z1,z2,z3,z4,z5]
    wu=[wu1,wu2,wu3,wu4,wu5]  
    #定义字典，将string格式的字母与图形形式的字母联系起来
    engdic={'a':aa,'b':bb,'c':cc,'d':dd,'e':ee,'f':ff,'g':gg,'h':hh,'i':ii,'j':jj,'k':kk,'l':ll,'m':mm,'n':nn,'o':oo,'p':pp,'q':qq,'r':rr,'s':ss,'t':tt,'u':uu,'v':vv,'w':ww,'x':xx,'y':yy,'z':zz,' ':wu}  
    #编写五个函数来实现分行打印的功能
    def line0(x):
        y=list(x)
        length=len(y)
        line_0=''
        for i in y:
            line_0=line_0+' '+engdic[i][0]
        return line_0

    def line1(x):
        y=list(x)
        length=len(y)
        line_1=''
        for i in y:
            line_1=line_1+' '+engdic[i][1]
        return line_1

    def line2(x):
        y=list(x)
        length=len(y)
        line_2=''
        for i in y:
            line_2=line_2+' '+engdic[i][2]
        return line_2

    def line3(x):
        y=list(x)
        length=len(y)
        line_3=''
        for i in y:
            line_3=line_3+' '+engdic[i][3]
        return line_3
    
    def line4(x):
        y=list(x)
        length=len(y)
        line_4=''
        for i in y:
            line_4=line_4+' '+engdic[i][4]
        return line_4

    def bigpattern(x):
        print line0(x)
        print line1(x)
        print line2(x)
        print line3(x)
        print line4(x)

    y=raw_input('What do you want to show: ')
    x=y.lower()
    bigpattern(x)
    raw_input('Press enter to exit')  

2.level 3的代码  
    import os
    import time
    #use string to define each single line of each single English letter

    a1=' '*2+'#'+' '*2
    a2=' '+'#'+' '+'#'+' '
    a3='#'+' '*3+'#'
    a4='#'*5
    a5='#'+' '*3+'#'
    b1='#'*4+' '
    b2='#'+' '*3+'#'
    b3='#'*4+' '
    b4='#'+' '*3+'#'
    b5='#'*4+' '
    c1='#'*5
    c2='#'+' '*4
    c3='#'+' '*4
    c4='#'+' '*4
    c5='#'*5
    d1='#'*4+' '
    d2='#'+' '*3+'#'
    d3='#'+' '*3+'#'
    d4='#'+' '*3+'#'  
    d5='#'*4+' '
    e1='#'*5
    e2='#'+' '*4
    e3='#'*5
    e4='#'+' '*4
    e5='#'*5
    f1='#'*5
    f2='#'+' '*4
    f3='#'*5
    f4='#'+' '*4
    f5='#'+' '*4
    g1='#'*5
    g2='#'+' '*4
    g3='#'+' '+'#'*3
    g4='#'+' '*3+'#'
    g5='#'*5 
    h1='#'+' '*3+'#'
    h2='#'+' '*3+'#'
    h3='#'*5
    h4='#'+' '*3+'#'
    h5='#'+' '*3+'#'
    i1='#'*5
    i2=' '*2+'#'+' '*2
    i3=' '*2+'#'+' '*2
    i4=' '*2+'#'+' '*2
    i5='#'*5
    j1='#'*5
    j2=' '*2+'#'+' '*2
    j3=' '*2+'#'+' '*2
    j4='#'+' '+'#'+' '*2
    j5=' '+'#'*2+' '*2
    k1='#  ##'
    k2='# #  '
    k3='##   '
    k4='# #  '
    k5='#  ##'
    l1='#    '
    l2='#    '
    l3='#    '
    l4='#    '
    l5='#####'
    m1='#####'
    m2='# # #'
    m3='# # #'
    m4='# # #'
    m5='# # #'
    n1='#   #'
    n2='##  #'
    n3='# # #'
    n4='#  ##'
    n5='#  ##'
    o1=' ### '
    o2='#   #'
    o3='#   #'
    o4='#   #'
    o5=' ### '
    p1='#### '
    p2='#   #'  
    p3='#### '
    p4='#    '
    p5='#    '
    q1='#### '
    q2='#  # '
    q3='# ## '
    q4='#### '
    q5='    #'
    r1='#### '
    r2='#   #'
    r3='#### '
    r4='# #  '
    r5='#  ##'
    s1='#####'
    s2='#    '
    s3='#####'
    s4='    #'
    s5='#####'
    t1='#####'
    t2='  #  '
    t3='  #  '
    t4='  #  '
    t5='  #  '
    u1='#   #'
    u2='#   #'
    u3='#   #'
    u4='#   #'
    u5='#####'
    v1='#   #'
    v2='#   #'
    v3=' # # '
    v4=' # # '
    v5='  #  '
    w1='# # #'
    w2='# # #'
    w3='# # #'
    w4='# # #'
    w5='#####'
    x1='#   #'
    x2=' # # '
    x3='  #  '
    x4=' # # '
    x5='#   #'
    y1='#   #'
    y2=' # # '
    y3='  #  '
    y4='  #  '
    y5='  #  '
    z1='#####'
    z2='   # '
    z3='  #  '
    z4=' #   '
    z5='#####'
    wu1='     '
    wu2='     '
    wu3='     '
    wu4='     '
    wu5='     '

    #use list to define each single letter

    aa=[a1,a2,a3,a4,a5]
    bb=[b1,b2,b3,b4,b5]
    cc=[c1,c2,c3,c4,c5]
    dd=[d1,d2,d3,d4,d5]
    ee=[e1,e2,e3,e4,e5]
    ff=[f1,f2,f3,f4,f5]
    gg=[g1,g2,g3,g4,g5]
    hh=[h1,h2,h3,h4,h5]
    ii=[i1,i2,i3,i4,i5]
    jj=[j1,j2,j3,j4,j5]
    kk=[k1,k2,k3,k4,k5]
    ll=[l1,l2,l3,l4,l5]
    mm=[m1,m2,m3,m4,m5]
    nn=[n1,n2,n3,n4,n5]
    oo=[o1,o2,o3,o4,o5]
    pp=[p1,p2,p3,p4,p5]
    qq=[q1,q2,q3,q4,q5]
    rr=[r1,r2,r3,r4,r5]
    ss=[s1,s2,s3,s4,s5]
    tt=[t1,t2,t3,t4,t5]
    uu=[u1,u2,u3,u4,u5]
    vv=[v1,v2,v3,v4,v5]
    ww=[w1,w2,w3,w4,w5]
    xx=[x1,x2,x3,x4,x5]
    yy=[y1,y2,y3,y4,y5]
    zz=[z1,z2,z3,z4,z5]
    wu=[wu1,wu2,wu3,wu4,wu5]

    #use dic to show the connection between letter and pattern

    engdic={'a':aa,'b':bb,'c':cc,'d':dd,'e':ee,'f':ff,'g':gg,'h':hh,
        'i':ii,'j':jj,'k':kk,'l':ll,'m':mm,'n':nn,'o':oo,'p':pp,'q':qq,
        'r':rr,'s':ss,'t':tt,'u':uu,'v':vv,'w':ww,'x':xx,'y':yy,'z':zz,' ':wu}

    #define the output of each line

    def line0(x,s):
        li=list(s)
        length=len(li)
        line_0=''
        for i in li:
            line_0=line_0+' '+engdic[i][0]
        return '|'+(x[0]-1)*' ' + line_0 + (61-x[0]-length)*' '+'|'

    def line1(x,s):
        li=list(s)
        length=len(li)
        line_1=''
        for i in li:
           line_1=line_1+' '+engdic[i][1]
        return '|'+(x[0]-1)*' ' + line_1 + (61-x[0]-length)*' '+'|'

    def line2(x,s):
        li=list(s)
        length=len(li)
        line_2=''
        for i in li:
            line_2=line_2+' '+engdic[i][2]
        return '|'+(x[0]-1)*' ' + line_2 + (61-x[0]-length)*' '+'|'

    def line3(x,s):
        li=list(s)
        length=len(li)
        line_3=''
        for i in li:
            line_3=line_3+' '+engdic[i][3]
        return '|'+(x[0]-1)*' ' + line_3 + (61-x[0]-length)*' '+'|'

    def line4(x,s):
        li=list(s)
        length=len(li)
        line_4=''
        for i in li:
            line_4=line_4+' '+engdic[i][4]
        return '|'+(x[0]-1)*' ' + line_4 + (61-x[0]-length)*' '+'|'

    #define the function to draw a single picture

    def draw(x,y,s):
        for i in range(3):
            print
        print 40*' '+'-'*len(line0(x,s))
        for up in range(y[0]-1):
            print 
        print 40*' '+line0(x,s)
        print 40*' '+line1(x,s)
        print 40*' '+line2(x,s)
        print 40*' '+line3(x,s)
        print 40*' '+line4(x,s)
        for down in range(26-y[0]):
            print 
        print 40*' '+'-'*len(line0(x,s))
 
    #functions to make block move

    def move_ul():
        x[0]=x[0]-1
        y[0]=y[0]-1

    def move_ur():
        x[0]=x[0]+1
        y[0]=y[0]-1

    def move_dl():
        x[0]=x[0]-1
        y[0]=y[0]+1

    def move_dr():
        x[0]=x[0]+1
        y[0]=y[0]+1

    #define the way to change direction 

    def change(x,y,count):
 
        if (x[0],y[0]) == (1,1) and count[0] == 0:
            count[0]=3

        if (x[0],y[0]) == (61-len(s),1) and count[0] == 1:
            count[0]=2
 
        if (x[0],y[0]) == (1,26) and count[0] == 2:
            count[0]=1

        if (x[0],y[0]) == (61-len(s),26) and count[0] == 3:
            count[0]=0

        if y[0] == 1:
            if count[0] == 1:
                count[0] = 3
            if count[0] == 0:
                count[0] = 2

        if y[0] == 26:
            if count[0] == 3:
                 count[0] = 1
            if count[0] == 2:
                 count[0] = 0

        if x[0] == 1:
            if count[0] == 2:
                count[0] = 3
            if count[0] == 0:
                count[0] = 1
 
        if x[0] == 61-len(s):
            if count[0] == 1:
                count[0] = 0
            if count[0] == 3:
                count[0] = 2           
            

    #define the way to run
    def run():
        while True:
            draw(x,y,s)
            change(x,y,count)
            if count[0] == 0:
                move_ul()
            elif count[0] == 1:
                move_ur()
            elif count[0] == 2:
                move_dl()
            elif count[0] == 3:
                move_dr()
            time.sleep(0.2)
            i=os.system('cls')
        

    x = [1]
    y = [1]
    count = [0]
    s=raw_input('What do you want to show? ')
    run()
    

###3.程序执行情况  
1.作业L1执行情况  
作业L1的要求是在屏幕上拼出自己名字的英文。我的名字是吴雨桥，大写英文就是YUQIAO WU。执行情况如下：  
  
  
![作业L1执行情况](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter1/%E4%BD%9C%E4%B8%9AL1%E6%89%A7%E8%A1%8C%E6%83%85%E5%86%B5.png)  
  
2.作业L2执行情况  
作业L2的要求是在屏幕用字母拼出任意次序的姓名，为此我选取了我名字的倒写UW OAIQUY、 HAOCAI、WUHAN UNI三个名字显示。执行情况如下：
![作业L2执行情况第一张](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter1/%E4%BD%9C%E4%B8%9AL2%E7%AC%AC%E4%B8%80%E5%BC%A0.png)  
  
![作业L2执行情况第二张](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter1/%E4%BD%9C%E4%B8%9AL2%E7%AC%AC%E4%BA%8C%E5%BC%A0.png)  
  
![作业L2执行情况第三张](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter1/%E4%BD%9C%E4%B8%9AL2%E7%AC%AC%E4%B8%89%E5%BC%A0.png)   

3.作业L3的执行情况  
作业L3的要求是在一定范围的屏幕上用字符做出动画。我想做出字符在两个球拍之间传来传去的效果。我首先让图像为5帧，要显示的字符串为HELLO，执行效果如下：  
![gif 1](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter1/level%203_1.gif)  
之后，我显示了PHYSICS, 帧数为20帧，执行效果如下：  
![gif 2](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter1/gif%202.gif)  
  
  
##4.结论  
本文中使用了python语言，定义了几个简单的函数，同时运用了列表和字典的知识。第一份代码可以将用户输入的任意字符串以大写字母的图形形式表现出来。第二份代码可以读取用户输入的任何字符串，并用如上的动画效果显示出来。该程序还有许多可以改进的地方，最重要的是两点：  
1.加入小写字母的数据，实现输出小写字母的图形的功能。  
2.加入中文汉字的数据，实现输出汉字的图形的功能。
