from ast import For
import pandas as pd
import matplotlib.pyplot as plt

import modelSIR

m = modelSIR.SIR(rateSI= 1/2,rateIR=1/3,Susceptible= 7900000,Infected=10,Resistant=0)
m.run()
print(m.plot())

