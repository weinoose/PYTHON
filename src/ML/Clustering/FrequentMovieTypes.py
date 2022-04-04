import pandas as pd
from apriori_source import apriori

data = pd.DataFrame(pd.read_excel("frequentmovietypes.xlsx"))

main_list = []

s = 0
while s < len(list(data['GENRE'])):
    fow = list(data.iloc[s,:])
    main_list.append(fow)
    s += 1

result = apriori(main_list, min_support=0.01, min_confidence=0.2, min_lift=3, min_length=2)

for i in list(result):
    print("\n", i,"\n")