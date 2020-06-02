## pyinstaller 打包总结

 打包命令：

打开anaconda下的anaconda prompt，进入py文件所在目录

``` python 
pyinstaller -F -i gt256.ico Inputdata_generate.py
```

其中 gt256.ico 、Inputdata_generate.py必须在工作同一个目录下；

gt256.ico要求较高，采用下面网站生成的ico,可用

``` http
http://www.ico51.cn/
```

### 程序代码

``` python 
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 15:57:15 2020
@author: 39300135
"""
import time
import json
import os
#import win32api

def iandfrange(start,*args):
    """
    输入：函数可接收最多三个参数，依次分别是起始值，结束值和步长，可以做任意整数和小数的range功能
    输出：返回值为包含起始值的，以起始值迭代加步长，直到最后一个<=结束值的值为止的一个列表
    约定：
        1.如果只传入2个参数，自动匹配给起始值和结束值，步长默认为1
        2.如果只传入1个参数，自动匹配给结束值，起始值默认为0，步长默认为1
    测试：
        1.参数超过3个
        2.参数传入2个
        3.参数传入1个
        4.步长传入的值非整数和小数的情况
        5.start>=end的情况
        6.用户输入的起始值加步长经过1次计算后即超过结束值的情况
    声明：
        1.程序仅供学习使用，实现并未参考numpy.arange的实现，测试如有不详尽之处，请多多指教
        2.程序中对计算结果如果不四舍五入，可能会得到类似"2.5366600000000004"这样精度有错误的结果，
          此结果由计算机本身的精度误差导致
    """
    #保证传入参数不超过3个，超过则报错提示用户
    try:
        args[2]
    except Exception as e:
        pass
    else:
        raise Exception(ValueError,"The function receive three args!")
    #保证传入的3个参数能正确匹配到start,end和step三个变量上
    try:
        end,step=args[0],args[1]
    except IndexError:
        try:
            end=args[0]
        except IndexError:
            end=start
            start=0
        finally:
            step=1      
    #参数正确性校验，包括对step是否是int或float的校验，提示用户输出数据可能只有start的校验以及start>=end的情况
    try:
        try:
            a,b=str(step).split(".")
            roundstep=len(b)
        except Exception as e:
            if isinstance(step,int):
                roundstep=0
            else:
                raise Exception(TypeError, "Sorry,the function not support the step type except integer or float!")        
        if start+step>=end:
            print("The result list may include the 'start' value only!")
        if start>=end:
            raise Exception(ValueError, "Please check you 'start' and 'end' value,may the 'start' greater or equle the 'end'!")
    except TypeError as e:
        print(e)
    else:
        pass
    #输出range序列
    lista=[]
    while start<end:
        lista.append(start)
        
        start=round(start+step,roundstep)
    return lista

def isList(list):
    Result=[]
    if(type(list).__name__=='list'):
        if (len(list)==3):
            Result=[ i for i in iandfrange(list[0],list[1]+list[2],list[2])]
        elif (len(list)==1):
            Result=[ i for i in iandfrange(list[0],list[0]+list[0],list[0])]       

    else:
        print("please check list or not .please set it as list")
    return Result    

        
        
        
def load(filepath):
    with open(filepath,'r') as f:
        data = json.load(f)
        return data

info=load('APC auto.json')
#print(info['Tamb'])
#print(len(info['Tamb']))
#print(type(info['Tamb']))
Tamb=isList(info['Tamb']) 
#print(Tamb)
Pamb=isList(info['Pamb'])
GIRI=isList(info['GIRI'])
phi=isList(info['UR'])
head=info['head']
end1=info['end1']
end2=info['end2']
NAMEMAP=info['NAMEMAP']

cal_mode=info['mode_cal_Select'][0]
if (cal_mode.lower()=='fullload'):
    TT1=isList(info['TT1'])
    IGV=isList(info['IGV'])
    for a in Tamb:
        for b in Pamb:
            for c in GIRI:
                for d in TT1:
                    for e in IGV:
                        datetime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                        st0='\n'+str(datetime)+'\n'
                        st1=head
                        st20='\n'+"&INPUTDATA"
                        
                        name=['TC1=',',PAMB=',',UR=','DPI=',',DPU=','TT1=',',PIGV=',',PIGVMAX=']
                        
                        
                        st_row1='\n'+'TC1='+str(a) + ',PAMB=' + str(b) + ',UR=' + str(60)+','
                        st_row2='\n'+'DPI='+str(10) + ',DPU=' + str(30) + ',IDP=0,ALT=0,'
                        st_row3='\n'+'TT1='+str(d) + ',PIGV='+str(e)+',PIGVMAX=100,' +'\n' +"GIRI="+ str(c)+','
                        st_row4="\n"+"NAMEMAP="+str(NAMEMAP)
                        
                        str_all= st0 + st1 + st20 +  st_row1+st_row2+st_row3+ st_row4 +end1+end2
                        
                        
                        filename='TC1='+str(a) +'-IGV='+str(e)+'-tiso='+str(d) + '-N='+ str(c)+'.dat'
                        print(filename)
                        isExists=os.path.exists("inputdata")
                        if not isExists:
                            os.mkdir("inputdata")
                            print("file inputdata create successfully")
                        dirpath=os.getcwd()+'\\inputdata\\'
                        
                        with open(dirpath+filename,'w') as f:
                            f.write(str_all)
                        
elif (cal_mode.lower()=='partload'):
    TT2=isList(info['TT2'])
    PGT=isList(info['PGT'])
    for a in Tamb:
        for b in Pamb:
            for c in GIRI:
                for d in TT2:
                    for e in PGT:
                        datetime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                        st0=str(datetime)+'\n'
                        st1=head
                        st20='\n'+"&INPUTDATA"
                        
                        
                        
                        st_row1='\n'+'TC1='+str(a) + ',PAMB=' + str(b) + ',UR=' + str(60)+','
                        st_row2='\n'+'DPI='+str(10) + ',DPU=' + str(30) + ',IDP=0,ALT=0,'
                        st_row3='\n'+'TT2='+str(d) + ',PGT='+str(e)+',PIGVMIN=55,' +'\n' +"GIRI="+ str(c)+','
                        st_row4="\n"+"NAMEMAP="+str(NAMEMAP)
                        
                        str_all=st0 + st1 + st20 +  st_row1+st_row2+st_row3+ st_row4 +end1+end2
                        
                        
                        filename='TC1='+str(a) +'-PGT='+str(e)+'-TT='+str(d) + '-N='+ str(c)+'.dat'
                        print(filename)
                        isExists=os.path.exists("inputdata")
                        if not isExists:
                            os.mkdir("inputdata")
                            print("file inputdata create successfully")
                        dirpath=os.getcwd()+'\\inputdata\\'
                        
                        with open(dirpath+filename,'w') as f:
                            f.write(str_all)

```

