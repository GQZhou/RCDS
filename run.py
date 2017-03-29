# -*- coding: utf-8 -*-
"""
Spyder Editor
This is main function of RCDS.
"""
import numpy as np
from powellmain import powellmain
#from datascan import datascan
#global vrange, Nvar
"""To set the number of variables here"""
Nobj=1
Nvar=3
vrange=np.array([[-1,1],[-1,1],[-1,1]])
p0=np.array([0.1,0.2,0.3])
p0=np.transpose(p0)
x0=np.array(range(0,Nvar))*1.0
for i in range(0,Nvar):
    x0[i]=(p0[i]-vrange[i,0])/(vrange[i,1]-vrange[i,0])
#global g_cnt, g_data
g_data=[]
gcnt=0
#global noise
"""To set the noise here"""
g_noise=0.5
dmat= np.eye(Nvar, dtype=float) 
"""To set the step size here """
step=0.01
tol=0
"""how to change @func_obj plot to python"""
[x1,f1,nf,gcnt,g_data,g_noise,Nvar,vrange]=\
powellmain(x0,step,dmat,tol,50,'plot',5000,gcnt,g_data,g_noise,Nvar,vrange)


pydata=np.array([p0,x0,vrange,g_noise,step,x1,f1])
np.save("result.npy",pydata)
#[result]=datascan(g_data)
gdata=np.array(g_data)
indx=np.argsort(gdata[:,3])
result=gdata[indx[0]]
print 'The result is:',result

#data=open('datagnoise=1.txt','a')
#data.write(str(('%.5f' %result[0]))+'  '+str(('%.5f' %result[1]))+'  '+\
#        str(('%.5f' %result[2]))+'  '+str(('%.5f' %result[3]))+'\n')
#data.close()

#(data_1,xm,fm)=process_scandata(g_data,Nvar,vrange)
#[np.transpose(xm[:]),fm]]
#func_obj(xm)
