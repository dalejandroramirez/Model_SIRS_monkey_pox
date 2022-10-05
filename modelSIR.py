import pandas as pd
import matplotlib.pyplot as plt


# 'eones' (número de puntos de tiempo para modelar, predeterminado 1000)
# 'Susceptible' (número de individuos susceptibles en el momento 0, predeterminado 950)
# 'Infectado' (número de personas infectadas en el momento 0, predeterminado 50)
# 'Resistente' (número de individuos resistentes en el momento 0, predeterminado 0)
# 'rateSI' (tasa base 'beta' de S a I, por defecto 0.05)
# 'rateIR' (tasa base 'gamma' de I a R, por defecto 0.01)

class SIR:

    def __init__(self, eons=1000, Susceptible=950, Infected=50, Resistant=0, rateSI=0.05, rateIR=0.01):
        self.eons = eons
        self.Susceptible = Susceptible
        self.Infected = Infected
        self.Resistant = Resistant
        self.rateSI = rateSI
        self.rateIR = rateIR
        self.numIndividuals = Susceptible + Infected + Resistant
        self.results = None
        self.modelRun = False

    def run(self):
        Susceptible = [self.Susceptible]
        Infected = [self.Infected]
        Resistant = [self.Resistant]

        for step in range(1, self.eons):
            S_to_I = (self.rateSI * Susceptible[-1] * Infected[-1]) / self.numIndividuals  #dS/dt
            I_to_R = Infected[-1] * self.rateIR

            Susceptible.append(Susceptible[-1] - S_to_I)
            Infected.append(Infected[-1] + S_to_I - I_to_R)
            Resistant.append(Resistant[-1] + I_to_R)

        self.results = pd.DataFrame.from_dict({'Time':list(range(len(Susceptible))),
            'Susceptible':Susceptible, 'Infected':Infected, 'Resistant':Resistant},
            orient='index').transpose()
        self.modelRun = True

    def plot(self):
        if self.modelRun == False:
            print('Error: Model has not run. Please call SIR.run()')
            return
        plt.plot(self.results['Time'], self.results['Susceptible'], color='blue',label="S")
        plt.plot(self.results['Time'], self.results['Infected'], color='red',label="I")
        plt.plot(self.results['Time'], self.results['Resistant'], color='green',label="R")
        plt.xlabel('Time')
        plt.ylabel('Population')
        plt.legend(['Susceptible','Infected','Resistant'], prop={'size': 10}, loc='upper center', bbox_to_anchor=(0.5, 1.02), ncol=3, fancybox=True, shadow=True)
        plt.title(r'$\beta = {0}, \gamma = {1}$'.format(self.rateSI, self.rateIR))
        plt.savefig('test.png')
        plt.legend()
        plt.show()
        plt.close()
        

