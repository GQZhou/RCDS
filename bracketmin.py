# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 15:44:39 2017

@author: GQZhou
"""
import numpy as np
from fun_obj import func
from matplotlib import pyplot
from time import sleep
from math import isnan
def bracketmin(x0,f0,dv,step0,flag_plot,gcnt,g_data,g_noise,Nvar,vrange):
   # print "[][][][][][][][][][][][][][][]",dv
    step=step0
    nf=0
    if np.isnan(f0) or isnan(f0):
        [f0,gcnt,g_data,g_noise,Nvar,vrange]=\
        func(x0,gcnt,g_data,g_noise,Nvar,vrange)
        nf=nf+1
  #  xflist=[]


 #   xflist.append([0.0,f0])
    xflist = np.array([[0,f0]])

    fm=f0
    am=0
    xm=x0
    step_init=step
    x1=x0+dv*step
    [f1,gcnt,g_data,g_noise,Nvar,vrange]=\
    func(x1,gcnt,g_data,g_noise,Nvar,vrange)
   # f1=func(x1)
    nf=nf+1
    xflist = np.concatenate((xflist,np.array([[step,f1]])),axis=0)
   # nxf=float(np.size(xflist,1))+1
  #  xflist.append([step,f1])
    if f1<fm:
        fm=f1
        am=step
        xm=x1
    gold_r=0.618034 
   # step0 = step
    while f1<fm+3*g_noise:
        step = step*(1.0+gold_r)
        x1=x0+dv*step
        [f1,gcnt,g_data,g_noise,Nvar,vrange]=\
        func(x1,gcnt,g_data,g_noise,Nvar,vrange)
        if isnan(f1):
            print 'backetmin: f1=NaN\n'
            break
        else:
            xflist = np.concatenate((xflist,np.array([[step,f1]])),axis=0)
            if f1<fm:
                fm=f1
                am=step
                xm=x1 
    a2=step
    if f0>fm+g_noise*3:
        a1=0

        if flag_plot=='plot' :
            xflist=np.array(xflist)
            pyplot.plot(xflist[:,0],xflist[:,1],'o',xflist[0,0],\
                        xflist[0,1],'r*')
            sleep(0.1)
          
        a1=a1-am
        a2=a2-am
   #     print "&&&&&&&&&&",a1,'%%%%%%',a2 
        return xm,fm,a1,a2,xflist,nf,gcnt,g_data,g_noise,Nvar,vrange

    step=-step_init
    x2=x0+dv*step
    [f2,gcnt,g_data,g_noise,Nvar,vrange]=\
    func(x2,gcnt,g_data,g_noise,Nvar,vrange)
    
    #f2=func(x2)
    nf=nf+1
   # nxf=float(np.size(xflist))+1
   # xflist.append([step,f2])
    xflist = np.concatenate((xflist,np.array([[step,f2]])),axis=0)
    if f2<fm:
        fm=f2
        am=step
        xm=x2

    while f2<fm+g_noise*3:
        step=step*(1.0+gold_r)
        x2=x0+dv*step
        [f2,gcnt,g_data,g_noise,Nvar,vrange]=\
        func(x2,gcnt,g_data,g_noise,Nvar,vrange)
        nf +=1
        if isnan(f2):
            print 'bracketmin: f2=NaN\n'
            break
        else:
            xflist = np.concatenate((xflist,np.array([[step,f2]])),axis=0)
            if f2<fm:
                fm=f2
                am=step
                xm=x2
    a1=step
    if a1>a2:
        tmpa=a2
        a2=a1
        a1=tmpa
    a1=a1-am
    a2=a2-am
    xflist[:,0] -= am
    xflist = xflist[np.argsort(xflist[:,0])]
    if flag_plot=='plot' :
        pyplot.plot(xflist[:,0],xflist[:,1],'o',-am,f0,'r*',0,fm,'gd')
        pyplot.xlabel('alpha')
        pyplot.xlabel('objective')
        sleep(0.1)
        
 #   print "$$$$$$$$$$$",a1,'**********',a2  ,"=======",am  
    return xm,fm,a1,a2,xflist,nf,gcnt,g_data,g_noise,Nvar,vrange
        
















          
                   
        
