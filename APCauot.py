# -*- coding: utf-8 -*-
"""
Created on Thu May  7 16:20:49 2020

@author: 39300135
"""

import numpy as np
import time
import json
import os
import win32api

def load(filepath):
    with open(filepath,'r') as f:
        data = json.load(f)
        return data

info=load('APC auto.json')
Tamb=info['Tamb']
Pamb=info['Pamb']
IGV=info['IGV']
GIRI=info['GIRI']
TT1=info['TT1']
head=info['head']
end=info['end']
phi=info['UR']
NAMEMAP=info['NAMEMAP']


for tamb in np.arange(Tamb[0],Tamb[1],Tamb[2]):
    for igv in np.arange(IGV[0],IGV[1],IGV[2]):
        for tt1 in np.arange(TT1[0],TT1[1],TT1[2]):
            for giri in np.arange(GIRI[0],GIRI[1],GIRI[2]):
                datetime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                st0=str(datetime)+'\n'
                st1=head
                st20='\n'+"&INPUTDATA"
                
                name=['TC1=',',PAMB=',',UR=','DPI=',',DPU=','TT1=',',PIGV=',',PIGVMAX=']
                
                
                st_row1='\n'+name[0]+str(tamb) + name[1] + str(1.01325) + name[2] + str(60)+','
                st_row2='\n'+name[3]+str(10) + name[4] + str(30) + ',IDP=0,ALT=0,'
                st_row3='\n'+name[5]+str(tt1) + name[6]+str(igv)+',PIGVMAX=100,' +'\n' +"GIRI="+ str(giri)+','
                st_row4="\n"+"NAMEMAP="+str(NAMEMAP)
                
                str_all=st0 + st1 + st20 +  st_row1+st_row2+st_row3+ st_row4 +end
                
                
                filename='TC1='+str(tamb) +'-IGV='+str(igv)+'-tiso='+str(tt1) + '-N='+ str(giri)+'.dat'
                dirpath=os.getcwd()+'\\result\\'
                
                with open(dirpath+filename,'w') as f:
                    f.write(str_all)


                    
    



def cal_apc():
    app=r'C:\Program Files (x86)\AnsaldoEnergia\APC3\APC3.exe' 
#    for i in IGV:
#       s12='{:.2f}'.format(i)
#        for j in speed:
#            s23='{:.2f}'.format(j)
    filePath = 'C:\\Users\\39300135\\Desktop\\gengxin\\result\\'
    file=os.listdir(filePath)
#    dir=r'C:/Users/39300135/Desktop/gengxin/78MW/Map_cal/ ' + s12+'IGV'+s23+'N' +'-100%GT-Methane.dat BATCH' 
    for dir in file:
        dir=str(dir)
        
        dir=r'C:/Users/39300135/Desktop/gengxin/result/' + dir +' BATCH' 
        print(dir)
        win32api.ShellExecute(0, 'open', app, dir, '', 0)           # 后台执行  
        time.sleep(6)
        os.system('%s%s' % ("taskkill /F /IM ",'EXCEL.EXE'))



cal_apc()
        
        
        
        
#datetime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
#st0=str(datetime)+'\n'
#st1=head
#st20=('''
#&INPUTDATA
#''')
#name=['TC1=',',PAMB=',',UR=','DPI=',',DPU=','TT1=',',PIGV=',',PIGVMAX=']
#
#
#st_row1=name[0]+str(Tamb[0]) + name[1] + str(Pamb[0]) + name[2] + str(phi[0])+','
#st_row2='\n'+name[3]+str(10) + name[4] + str(30) + ',IDP=0,ALT=0,'
#st_row3='\n'+name[5]+str(TT1[0]) + name[6]+str(IGV[0])+',PIGVMAX=100,' +'\n' +"GIRI="+ str(GIRI[0])+','
#st_row4="\n"+"NAMEMAP="+str(NAMEMAP)
#
#str_all=st0 + st1 + st20 +  st_row1+st_row2+st_row3+ st_row4 +end
#
#
#filename='TC1='+str(Tamb[0]) +' PAMB='+str(Pamb[1])+' PIGV='+str(IGV[0]) +'.dat'
#dirpath=os.getcwd()+'\\result\\'
#
##with open(dirpath+filename,'w') as f:
##    f.write(str_all)
##filePath = os.getcwd()+'\\result\\'
##app=r'C:\Program Files (x86)\AnsaldoEnergia\APC3\APC3.exe' 
##file=os.listdir(filePath)