import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from apriori_source import apriori

data = pd.DataFrame(pd.read_csv("apriori.csv"))

main_list = []

s = 0
while s < 161:
    fow = list(data.iloc[s,:])
    k = 0
    while k < 5:
        fow.pop(0)
        k += 1
    main_list.append(fow)
    s += 1

result = apriori(main_list, min_support=0.01, min_confidence=0.2, min_lift=3, min_length=2)

for i in list(result):
    print("\n", i,"\n")