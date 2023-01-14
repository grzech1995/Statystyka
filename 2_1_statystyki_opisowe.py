import numpy as np
import scipy.stats as scs
import statistics

dane_wzrostu = np.loadtxt("files/Wzrost.csv", delimiter=',')
print(dane_wzrostu)

print("min wzrost", dane_wzrostu.min())
print("min wzrost z numpy", np.min(dane_wzrostu))
print("max wzrost z numpy", np.max(dane_wzrostu))
print("srednia wzrost", dane_wzrostu.mean())
print("srednia wzrostu z numpy", np.mean(dane_wzrostu))
print("stand odchyl", dane_wzrostu.std())
print("stand odchyl z numpy", np.std(dane_wzrostu))

print("mediana wzrostu:", np.median(dane_wzrostu))
print("Mediana Scipy:", scs.scoreatpercentile(dane_wzrostu, 100))
print("Dominanta wzrostu:", statistics.mode(dane_wzrostu))

print("podstawowe statystyki wzrostu:", scs.describe(dane_wzrostu))