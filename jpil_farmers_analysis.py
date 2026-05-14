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



#which village used most fertilizers on average?
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
#plt.show()


#which crop type had the highest average farm size-cassava or yam?
crop_type_avg_farm_size=df.groupby("Crop Type")["Farm Size ha"].mean()
print(crop_type_avg_farm_size)

#crop_type_avg_farm_size.plot(kind="bar", color=["coral", "purple", "green"])
plt.title("average crop type")
plt.xlabel("Crop Type", fontsize=12)
plt.ylabel("Farm Size", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("crop_type_farm_size.png")
#plt.show()


#on average how much did yield improve per village before and after training
avg_yield_per_village = df.groupby("Village")[["Yield Before kg per hec", "Yield After kg per hec"]].mean()
print(avg_yield_per_village)

avg_yield_per_village.plot(kind="bar", color=["brown","blue", "indigo"])
plt.title("average yield before and after training")
plt.xlabel("Village", fontsize=14)
plt.ylabel("Yield kg per hec")
plt.xticks(rotation=45)
plt.legend(["Before training", "After training"])
plt.savefig("Average_yield_per_village.png")
plt.tight_layout()
#plt.show()

#what is the typical yield change for cassava farmers compared to yam farmers?
typical_yield_change=df.groupby("Crop Type")["Yield Change"].mean()
print(typical_yield_change)

#typical_yield_change.plot(kind="bar", color=["orange", "green"])
plt.title("Typical yield change")
plt.xlabel("Crop type", fontsize=14)
plt.ylabel("Yield change")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Typical_yield_change.png")
#plt.show()


#what is the typical amount of fertilizer used by farmers who used it correctly and incorrectly?
amount_of_fertilizer_used=df.groupby("Fertilizer Type")["Fertilizer Used kg"].count()
print(amount_of_fertilizer_used)

#amount_of_fertilizer_used.plot(kind="bar", color=["blue","green"])
plt.title("Amount of fertilizer used")
plt.xlabel("Fertilizer type")
plt.ylabel("Fertilizer used")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Amount_of_fertilizer_used.png")
#plt.show()

#what is the median farm size for farmers who had pest problems versus those who did not?
median_farm_size=df.groupby("Pest Incidence")["Farm Size ha"].median()
print(median_farm_size)

median_farm_size.plot(kind="bar", color=["orange","blue"])
plt.title("Median_farm_size", fontsize=12)
plt.xlabel("Pest incidence", fontsize=14)
plt.ylabel("Farm size ha")
plt.xticks(rotation=45)
plt.savefig("Median_farm_size.png")
plt.tight_layout()
plt.show()

