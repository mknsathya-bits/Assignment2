from autoviz.AutoViz_Class import AutoViz_Class
import pandas as pd

# Load your dataset
df = pd.read_csv('Cleaned_Entities.csv')

# Create an instance of AutoViz
AV = AutoViz_Class()

# Visualize the dataset
AV.AutoViz('Cleaned_Entities.csv')
