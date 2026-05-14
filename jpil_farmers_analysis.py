#importing the libraries

import pandas as pd
import matplotlib.pyplot as plt

#importing the excel file
df= pd.read_excel("farmers_analysis.xlsx", header=1)
print(df.columns)

#which village had the highest average crop yield after training?
avg_crop_yield=df.groupby("Village")["Yield After kg per hec"].mean()
print(avg_crop_yield)

#i will be drawing my average crop yield using bar chart
avg_crop_yield.plot(kind="bar", color=["green", "red", "blue"])

plt.title("Average yield after training")
plt.xlabel("Village", fontsize=12)
plt.ylabel("Average yield after training", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Average_Crop_Yield_After_Training.png")
#plt.show()

#which village use the most fertilizer on average?
most_fertilizer_used=df.groupby("Village")["Fertilizer Used kg"].mean()
print(most_fertilizer_used)

#using bar chart
most_fertilizer_used.plot(kind="bar", color=["coral", "purple", "green"])
plt.title("Most fertilizer used")
plt.xlabel("Village", fontsize=12)
plt.ylabel("Most fertilizer used", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Most_fertilizer_used.png")
plt.show()