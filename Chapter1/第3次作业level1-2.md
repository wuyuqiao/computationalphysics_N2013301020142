#第三次作业（level 1-2）  
##一、摘要  
###作业要求（摘自老师的Exercise.md文件）  
作业L1 在屏幕上用字符拼出自己姓名的英文  
作业L2 在屏幕上用字符拼出任意次序的姓名  
  
本次作业使用了python语言设计了一份代码，通过该代码可以实现作业上的要求。在下方有附上具体代码，同时在Chapter1文件夹中可以看到代码的源文件，如需查看，[请点击这里。](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter1/Code%20for%20level%201-2)   
  
##二、背景介绍    
如果想打印出来名字，可以使用print函数。但是如果我们想用图形形式打印出来，就要编写程序来执行。我们可以选择5*5的格式来打印，这样能够清晰的辨认出来每个字母，同时又不会占用太大的屏幕空间。  本次作业实际上显示了计算机屏幕显示字符的运行方案。
##三、正文  
###1.问题分析  
1.显然可见，如果实现了作业L2所要求的功能，那么作业L1的功能亦可实现，故本文从一开始就注意在作业L2功能的实现。  
  
2.要拼出任意次序的姓名，要先考察姓名的基本组成。如作者的姓名是YUQIAO WU，其基本的组成元素是英文字母，而字母一共有26个。本文设想当字母显示在屏幕上时，每个字母应该是由#和空格组成的图形。比如字母A应该显示为:  
![A](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter1/%E5%AD%97%E6%AF%8DA.png)  
此图中的A字母是显示在一个5*5的矩阵上。  
  
3.显然这需要用到print函数。而print函数是一行一行打印的，故本文将每一个字母按行数分为五行，每行单独用一个名称表示。比如对于字母A，用a1代表第一行，a2代表第二行，如此类推。比如a1=' '*2+'#'+' '*2。同时还要单独列一个5*5矩阵表示空格矩阵。  
  
4.用#号和空格表示出每一个字母的每一行后，要将每一个字母的五行单独统一起来。于是对于每个字母生成一个列表，列表中的元素就是该字母的五个行的表示名称，这也就是定义每个字母。如aa=[a1,a2,a3,a4,a5]。  

5.当用户输入名字的时候，程序应该能将名字中的单个字母与程序中定义了的字母进行联系，故我们定义一个字典，将string格式的字母与上面定义了的图形的字母对应起来。  

6.把每个字母的图形格式编写好之后，需要按行把名字按行打印出来。由于每个字母都是在5*5的矩阵上编写的，我们需要首先打印出所有字母的第一行，之后打印出所有字母的第二行、第三行、第四行和第五行。这样一共有五行的打印任务，我们编写五个函数来实现。  

7.有了这五个函数之后，再编写一个总函数以执行上一步的五个函数，命名为bigpattern，有一个自变量，取用户输入的字符串为该自变量。函数的作用就是将输入的字符串用图形形式打印出来。  
  
###2.python代码  
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

###3.程序执行情况  
1.作业L1执行情况  
作业L1的要求是在屏幕上拼出自己名字的英文。我的名字是吴雨桥，大写英文就是YUQIAO WU。执行情况如下：  

![作业L1执行情况](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter1/%E4%BD%9C%E4%B8%9AL1%E6%89%A7%E8%A1%8C%E6%83%85%E5%86%B5.png)  
  
2.作业L2执行情况  
作业L2的要求是在屏幕用字母拼出任意次序的姓名，为此我选取了我名字的倒写UW OAIQUY、 HAOCAI、WUHAN UNI三个名字显示。执行情况如下：
![作业L2执行情况第一张](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter1/%E4%BD%9C%E4%B8%9AL2%E7%AC%AC%E4%B8%80%E5%BC%A0.png)  
  
![作业L2执行情况第二张](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter1/%E4%BD%9C%E4%B8%9AL2%E7%AC%AC%E4%BA%8C%E5%BC%A0.png)  
  
![作业L2执行情况第三张](https://raw.githubusercontent.com/wuyuqiao/computationalphysics_N2013301020142/master/Chapter1/%E4%BD%9C%E4%B8%9AL2%E7%AC%AC%E4%B8%89%E5%BC%A0.png)  

##4.结论  
本文中使用了python语言，定义了几个简单的函数，同时运用了列表和字典的知识，实现了将用户输入的任意字符串以大写字母的图形形式表现出来的功能。该程序还有许多可以改进的地方，最重要的是两点：  
1.加入小写字母的数据，实现输出小写字母的图形的功能。  
2.加入中文汉字的数据，实现输出汉字的图形的功能。
