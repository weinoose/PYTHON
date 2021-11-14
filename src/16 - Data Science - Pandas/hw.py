# Import our resources.
import pandas as pd

# Dataset : 2018 USD/TRY Exchange Rate Dataset.
# Goal : Improve Data Analyzing Skills.

# Gathering the data.
file = pd.read_csv("hw.csv")
df = pd.DataFrame(file)

# Giving a shape.
data = df.groupby("Tarih").min()

# STATISTICAL ANALYZING PART.
# You'll type your code here.