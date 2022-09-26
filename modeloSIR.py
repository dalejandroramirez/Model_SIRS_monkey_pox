#!/usr/bin/env python
# coding: utf-8



import matplotlib.pyplot as plt
import numpy as np
import sdeint


  ## Parametros ##
[ah,b1,b2,b3,a1,a2,fi,t,g,mh,mr,dh,dr,ar,a3] = [0.029,0.00025,0.00006,0.027,0.2,2,2,0.52,0.83,1.5,0.002,0.2,0.5,0.2,4]

#0 tasa de reclutamiento en humanos  : ah
#1 tasa de contacto de roedor a humano : b1
#2 tasa de contacto humano a humano : b2
#3 tasa de contacto roedor a roedor : b3
#4 Proporcion de humanos expuestos a la enfermedad : a1
#5 proporcion identificada con casos sospechosos : a2
#6 proporcion de casos descartados despues de diagnostico enviados a susceptibles :fi
#7 proporcion de casos sospechosos  y trasladados a recuperados : t
#8 tasa de humanos recuparados : g
#9 tasa de muerte natural humanos : mh
#10 tasa de muerte natural roedor : mr
#11 tasa de muerte inducida humanos : dh
#12 tasa de muerte inducida roedor : dr
#13 tasa de reclutamiento en roedores : ar
#14 Proporcion de roedores expuestos a la enfermedad : a3
############################################################

sig1=0.07
sig2=0.08
sig3=0.05
sig4=0.07
sig5=0.08
sig6=0.05
sig7=0.07
sig8=0.07

tspan = np.linspace(0,200,5001)

y0 = np.array([25, 12, 8,12,3,4,3,5])


def f(y, t):

    p = [0.029,0.00025,0.00006,0.027,0.2,2,2,0.52,0.83,1.5,0.002,0.2,0.5,0.2,4]
    Sh = y[0]
    Eh = y[1]
    Ih = y[2]
    Qh = y[3]
    Rh = y[4]
    Sr = y[5]
    Er = y[6]
    Ir = y[7]

    Nh = Sh + Eh + Ih + Qh + Rh
    Nr = Sr + Er + Ir

    f0 = p[0] - (((p[1]*Ir + p[2]*Ih)*Sh) / Nh ) -p[9]*Sh + p[6]*Qh 

    f1 = (((p[1]* Ir + p[2]*Ih )*Sh) / Nh) - (p[4] + p[5] + p[9])*Eh

    f2 = p[4]*Eh -(p[9]+p[11]+p[8])*Ih

    f3 = p[5]*Eh -(p[6]+p[7]+p[11]+p[9])* Qh

    f4 = p[8]*Ih + p[7]*Qh -p[9]*Rh

    f5 = p[13] - ((p[3]*Sr*Ir)/Nr) - p[10]*Sr

    f6 = ((p[3]*Sr*Ir)/Nr) - (p[10] + p[14])*Er

    f7 = p[14]*Er - (p[10]+p[12])*Ir
    
    return np.array([f0, f1, f2 ,f3 ,f4, f5, f6, f7])


def GG(y,t):
    return np.array([[sig1*y[0]],[sig2*y[1]],[sig3*y[2]],[sig4*y[3]],[sig5*y[4]],[sig6*y[5]],[sig7*y[6]],[sig8*y[7]]])

result = sdeint.itoint(f, GG, y0, tspan)


plt.plot(tspan,result,label=["Sh","Eh","Ih","Qh","Rh","Sr","Er","Ir"])
plt.legend()
plt.show()




