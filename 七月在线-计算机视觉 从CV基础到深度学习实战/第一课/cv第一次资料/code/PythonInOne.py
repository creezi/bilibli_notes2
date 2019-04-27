#coding: utf-8
# 第一行的作用是用来声明文本的字符集格式，可以识别和输出中文；
#-------------------------------------------------------------------------------
# Name:        PythonInOne.py
# Purpose:     Python快速入门
#-------------------------------------------------------------------------------
import os   #导入模块os.py
import io
import matplotlib   #这种导入方式，调用函数时候使用matplotlib.函数名()
import numpy as np #导入numpy.py，并且用np这个名字来代替numpy，更简洁
import matplotlib.image as mpimg    #调用函数: mpimg.函数名()
import matplotlib.pyplot as plt

from scipy.ndimage import filters #在scipy.ndimage总仅载入filters模块
from IPython.display import Image #函数调用：display.子功能()


def main(): #定义一个函数，名为main，不带输入参数；声明和调用的位置随意放置
    simpleCal() #调用函数，句末没有标点表示结束。声明和实现都在后面
    '''函数内部第一层级的语句这一行要比define缩进4个空格！或者一个Tab。
    python语言特点之一：使用缩进来代表某个功能的作用范围，不像C中用”{}“'''

    #List in Python
    la,lb = [1,2,3], ["苹果", "banana"] #列表类型
    la,lb = lb,la #python 赋值非常灵活，不需要中间变量
    new_lb = [i+2 for i in lb]  #增强型赋值方法 list comprehension
    add = lambda x,y:x+y    #用lamda函数来定义一个新的add函数
    lc = add(la,lb)     #【1,2,3，苹果，banana】
    print("测试add函数",lc)
    ld = lc #我想用ld来保存lc当前的值，但是。。。。
    lf = []
    lf.extend(lc)   #lf能否留住lc呢
    str_tmp1 = "fruit"
    lc.extend(str_tmp1)  #等价于lc[len(lc):] = str_tmp1 把字符串打散添加到list末尾
    lc.append(str_tmp1) #把字符串作为整体添加到最后
    for i in lc:    #i表示列表中每一个元素;注意结尾的冒号！
        print("show me the list:"+str(i))
    print("小心使用赋值语句",lf,ld)

    new_lc = []
    for i in range(len(lc)): #别忘了冒号，冒号，冒号
        new_lc.append((i,lc[i]))
    print("显示list的编号以及内容：",new_lc)

    #class in Python
    id = user("Alvin")
    id.showname()

    #tuple in Python 元组:两个list组队
    t_new_lc = list(enumerate(lc, start = 1))
    print(t_new_lc) #跟上面的new_lc内容一致
    print(type(t_new_lc[2]))
    print(t_new_lc[1])

    #dic in Python 字典：value和属性的组合
    d = {'Lilei': 30, 'Hanmeimei': 29, 'Lily': 28}
    for name, age in d.items():
        print ('%s is %d years old.' % (name, age))

    #numpy
    x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
    v = np.array([1, 0, 1])
    y = x+v   # broadcasting方式相加
    print(y)

#定义一个函数，可以有返回值，也可以没有返回值。
def simpleCal():
    print("首先学习"+"数值型的基本运算+字符串\
    ,bool类型，以及print的用法")   #行末尾的\是“续行符号
    x = 5
    print(type(x)) # Prints "<type 'int'>"
    print("x is %s, x+1 is %d, x*2=%d, x的平方是：%d"%(x,x+1,x*2,x**2))
    if (x <= 5)==True and False: #bool类型不但支持!=, ==,等还支持and or not的表达
        x+=1 #自加 不能用x++或者x--
        x*=2 #自乘
    elif x>5:   #别忘记条件后面的冒号，初学者很容易犯错。
        x/=2
    x-=2
    print ("现在的X值为%s"%x)
    y = 3.0 #ypte is <float>
    print ("x/2 is:%s, y/2 is:%.3f"%(x/2, y/2)) #注意在python2.x中这两个结果不同
    print(type(x/2)) #int类型的x除法之后是float
    str_break = "we will learn something about string!"
    str_tmp1 = "follow me"
    str_tmp2 = '%r %s %d' % (str_tmp1, "in", 2016)  # 格式化字符串
    print(str_break.capitalize()+"\r"+"\r"+str_tmp2.upper()+"---"*20)
    #Python的字符有高级语言的所有常用功能，而且字符可以做乘法！

#定义一个类，名字为user
class user:
    def __init__(self, name):   #构造函数
        self.name = name
        print("用户名设置完毕。")
    def showname(self):         #公有成员函数
        print("Current user's name is:", self.name)

'''一般在脚本最后调用主函数main（）；当我们直接运行当前脚本的时候
__name__相当于__main__。当这个脚本被当作模块import的时候，并不执行main()
'''
if __name__ == '__main__':
    print("Welcome to July's blog!")
    # print('Welcome to July\'s blog!')
    # 上面两句都正确，注意单引号的时候内部的符号要转义.
    main()

    #展示一些库
    img = np.zeros((100, 100))
    img[np.random.randint(0, 100, 500), np.random.randint(0, 100, 500)] = 255
    img2 = filters.gaussian_filter(img, 4, order=2)
    buf = io.BytesIO()
    matplotlib.image.imsave(buf, img2, cmap="gray")
    plt.plot([1,2,3,4])
    plt.ylabel('some numbers')
    plt.show()
    Image(buf.getvalue()) #