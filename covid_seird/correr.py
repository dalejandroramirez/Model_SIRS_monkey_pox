from covid_seird import CountryCovidSeird

# print(CountryCovidSeird.code_search("colombia"))

colombia = CountryCovidSeird("CO")

colombia.fit()

print(colombia.r2)    #Reproduccion de ajuste ??

print(colombia.r0)    #Reproduccion Basica

colombia.plot_fit("colombia_fit_plot")