# APC 批处理程序使用说明

 ### 程序构成

- data文件生成程序 ，程序名：Input_Generate_V1.exe

- APC计算程序 ，程序名：APC_Calculate.exe

- APC auto.json 

- apcdir.txt

  

### 数据计算流

```python
Input_Generate_V1.exe 会读取同目录下的APC auto.json 文件,生成文件夹inputdat，文件夹中包含用于APC计算的的后缀名为dat的文件；
APC_Calculate.exe会调用同目录下的文件夹inputdat中的后缀名为dat的文件，逐个计算；
```



### json文件介绍

```json
{	
	"mode_cal_List":["fullLoad","partLoad"], // 介绍计算的模式，两种 全负荷和部分负荷
	"mode_cal_Select":["fullLoad"],     // 选用的计算模式
	"iter_var":["Tamb","IGV","TT1","GIRI"], //要迭代的变量，该行暂时未用到
	"Tamb" :[0,0.5,0.5],            // 中括号内部的可以有3个或1个数，三个数时[a1,a2,步长]
	"UR":[30],						// 中括号里只有一个值[10],此时不参与迭代
	"Pamb" :[1.01325],
	"IGV" : [95,105,10],
	"TT1" : [1200],
	"TT2" : [550,560,10],
	"GIRI" :[2900,3000,100],
	"PGT" :[71510.0],
	"head" :"[yudengtao][39300135] \n Project:78 MW AE64.3A  ",  //文件的表头，可以修改
	"NAMEMAP":"TGS_943A_71,",   //计算的机组对应的map图；
	"end1" :"\nICOMB=1,HC=27.28,PC=50032,WC=75.9094,WH=23.8551,WO=0,WS=0,WAR=0,WHE=0,\nINOX=0,",

	"end2" :"\nTEST=0,MTR=19,MIWS=0,TIWS=25,PIWS=30,IWS=2,MICE=0,\nIPMAX=0,\nEtaGEN=100,PAUX=0,\n&FINE"	
        // end1 、end2中的数据可以按需修改
}

```

``` php
注意：
    01.除了最后一行，每一行结尾都以逗号结尾；
    02.每一行用 ： 分开，组成键值对，前面是键，后面是值；
    03.注意非数字必须用双冒号包裹起来；
    04. // 后是注释内容，不可以放在文件中。
    05.经测试，PC上不需要安装python环境，就可以运行。
    06.win10系统暂时不支持；
    07.文件路径中不能有中文，因为APC计算不支持中文路径。
```



### apcdir.txt文件介绍

``` txt
C:\Program Files (x86)\AnsaldoEnergia\APC3\APC3.exe

```

``` 注
注：此路径是电脑中APC安装的路径，如果APC安装时是默认安装的，则无需修改。
```


## Python数据后处理程序
[叶轮径向力计算](Fr_cal.py)

