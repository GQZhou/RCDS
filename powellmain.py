# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 09:50:44 2017

@author: GQZhou
"""

import numpy as np
from fun_obj import func
from numpy import linalg
from bracketmin import bracketmin
from linescan import linescan
def powellmain(x0,step,Dmat0,tol,maxIt,flag_plot,maxEval,gcnt,\
               g_data,g_noise,Nvar,vrange):
    Nvar=len(x0)
    [f0,gcnt,g_data,g_noise,Nvar,vrange]=\
    func(x0,gcnt,g_data,g_noise,Nvar,vrange)
    nf=1
    xm=x0
    fm=f0
    it=0
    Dmat=np.array(Dmat0)
    """sample number?"""
    Npmin=6
    while it < maxIt:
    #    print Dmat
        it=it+1
        """why ?"""
        step=step/1.2
        k=1
        dell=0
        for ii in range(0,Nvar):
            dv=Dmat[:,ii]
          
            [x1,f1,a1,a2,xflist,ndf,gcnt,g_data,g_noise,Nvar,vrange]=\
            bracketmin(xm,fm,dv,step,flag_plot,gcnt,g_data,g_noise,Nvar,vrange)
            nf=nf+ndf
         #   print it, ii, gcnt
            print("iter %d, dir %d: begin\t%d\t%f" %(it, ii, gcnt,f1))
            [x1,f1,ndf,gcnt,g_data,g_noise,Nvar,vrange]=linescan(x1,f1,dv\
            ,a1,a2,Npmin,xflist,flag_plot,gcnt,g_data,g_noise,Nvar,vrange)
     #       print gcnt,f1
            nf=nf+ndf
            
            if (fm-f1)*(1)>dell:
                dell=(fm-f1)*(1)
                k=ii
                print("iteration %d, var %d: del = %f updated\n" %(it, ii, dell))
            fm=f1
            xm=x1
        xt=2*xm-x0
   # ft=func(xt)
        [ft,gcnt,g_data,g_noise,Nvar,vrange]=\
        func(xt,gcnt,g_data,g_noise,Nvar,vrange)
        nf=nf+1
#    print '*************'
 #   print ' '
 #   print [x0,xt,xm]
 #   print [f0,ft,fm]
  #  print 'ok'
  #  print ' '
  #  print '*************'
    
    
        if f0<ft or 2*(f0-2*fm+ft)*((f0-fm-dell)/(ft-f0))**2>=dell:
#        print k,'not replaced：',f0<ft,\
 #       2*(f0-2*fm+ft)*((f0-fm-dell)/(ft-f0))**2>=dell
            print("   , dir %d not replaced: %d, %d\n" % (k,f0<=ft,\
                    2*(f0-2*fm+ft)*((f0-fm-dell)/(ft-f0))**2 >= dell ))
        else:
            if abs(linalg.norm(xm-x0))!=0:
                ndv=np.array((xm-x0)/linalg.norm(xm-x0))
                dotp=np.zeros([Nvar])
                for jj in range(0,Nvar):
                    dotp[jj]=abs(np.dot(np.transpose(ndv),Dmat[:,jj]))

       #     print 'Max(dotp)=', max(dotp), '\n'
            if max(dotp)<0.9:
                for jj in range(k,Nvar-1):
                    Dmat[:,jj]=Dmat[:,jj+1]
                Dmat[:,-1]=ndv
            
              #  print "{}{}{}{}}{}{}{}{}",ndv
                dv=Dmat[:,-1]
                [x1,f1,a1,a2,xflist,ndf,gcnt,g_data,g_noise,Nvar,vrange]=\
                bracketmin(xm,fm,dv,step,flag_plot,gcnt,g_data,\
                g_noise,Nvar,vrange)
                
                nf=nf+ndf
                print("iter %d, new dir %d: begin\t%d\t%f " %(it,k, gcnt,f1))
                [x1,f1,ndf,gcnt,g_data,g_noise,Nvar,vrange]=linescan(x1,f1,dv,\
                a1,a2,Npmin,xflist,flag_plot,gcnt,g_data,g_noise,Nvar,vrange)
                print("end\t%d : %f\n" %(gcnt,f1))
                nf=nf+ndf
                fm=f1
                xm=x1
            else:
                print("    , skipped new direction %d, max dot product %f\n" \
                     %(k, max(dotp)))
             #   print '    , skipped new direction',k, 'max dot product',\
           #     max(dotp),'\n'
           
        if gcnt>maxEval:
            print 'terminated, reaching function evaluation limit'
            break
        if 2.0*abs(f0-fm) < tol*(abs(f0)+abs(fm)) :
            print 'terminated: f0=',f0,'fm=',fm,'f0-fm=',f0-fm,'\n'
            break
        f0=fm
        x0=xm
    return xm,fm, nf,gcnt,g_data,g_noise,Nvar,vrange
        
                
                
                                          
    







































        
        
            
        
    
    
    