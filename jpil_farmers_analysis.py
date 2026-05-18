#importing the libraries

import pandas as pd
import matplotlib.pyplot as plt
 
#importing the excel file
df= pd.read_excel("farmers_analysis.xlsx", header=1)
print(df.columns)

#which village had the highest average crop yield after training?
#avg_crop_yield=df.groupby("Village")["Yield After kg per hec"].mean()
#print(avg_crop_yield)

#i will be drawing my average crop yield using bar chart
#avg_crop_yield.plot(kind="bar", color=["green", "red", "blue"])

#plt.title("Average yield after training")
#plt.xlabel("Village", fontsize=12)
#plt.ylabel("Average yield after training", fontsize=12)
#plt.xticks(rotation=45)
#plt.tight_layout()
#plt.savefig("Average_Crop_Yield_After_Training.png")
#plt.show()



#which village used most fertilizers on average?
#most_fertilizer_used=df.groupby("Village")["Fertilizer Used kg"].mean()
#print(most_fertilizer_used)

#using bar chart
#most_fertilizer_used.plot(kind="bar", color=["coral", "purple", "green"])
#plt.title("Most fertilizer used")
#plt.xlabel("Village", fontsize=12)
#plt.ylabel("Most fertilizer used", fontsize=12)
#plt.xticks(rotation=45)
#plt.tight_layout()
#plt.savefig("Most_fertilizer_used.png")
#plt.show()


#which crop type had the highest average farm size-cassava or yam?
#crop_type_avg_farm_size=df.groupby("Crop Type")["Farm Size ha"].mean()
#print(crop_type_avg_farm_size)

#crop_type_avg_farm_size.plot(kind="bar", color=["coral", "purple", "green"])
#plt.title("average crop type")
#plt.xlabel("Crop Type", fontsize=12)
#plt.ylabel("Farm Size", fontsize=12)
#plt.xticks(rotation=45)
#plt.tight_layout()
#plt.savefig("crop_type_farm_size.png")
#plt.show()


#on average how much did yield improve per village before and after training
#avg_yield_per_village = df.groupby("Village")[["Yield Before kg per hec", "Yield After kg per hec"]].mean()
#print(avg_yield_per_village)

#avg_yield_per_village.plot(kind="bar", color=["brown","blue", "indigo"])
#plt.title("average yield before and after training")
#plt.xlabel("Village", fontsize=14)
#plt.ylabel("Yield kg per hec")
#plt.xticks(rotation=45)
#plt.legend(["Before training", "After training"])
#plt.savefig("Average_yield_per_village.png")
#plt.tight_layout()
#plt.show()

#what is the typical yield change for cassava farmers compared to yam farmers?
#typical_yield_change=df.groupby("Crop Type")["Yield Change"].mean()
#print(typical_yield_change)

#typical_yield_change.plot(kind="bar", color=["orange", "green"])
#plt.title("Typical yield change")
#plt.xlabel("Crop type", fontsize=14)
#plt.ylabel("Yield change")
#plt.xticks(rotation=45)
#plt.tight_layout()
#plt.savefig("Typical_yield_change.png")
#plt.show()


#what is the typical amount of fertilizer used by farmers who used it correctly and incorrectly?
#amount_of_fertilizer_used=df.groupby("Fertilizer Type")["Fertilizer Used kg"].count()
#print(amount_of_fertilizer_used)

#amount_of_fertilizer_used.plot(kind="bar", color=["blue","green"])
#plt.title("Amount of fertilizer used")
#plt.xlabel("Fertilizer type")
#plt.ylabel("Fertilizer used")
#plt.xticks(rotation=45)
#plt.tight_layout()
#plt.savefig("Amount_of_fertilizer_used.png")
#plt.show()

#what is the median farm size for farmers who had pest problems versus those who did not?
#median_farm_size=df.groupby("Pest Incidence")["Farm Size ha"].median()
#print(median_farm_size)

#median_farm_size.plot(kind="bar", color=["orange","blue"])
#plt.title("Median_farm_size", fontsize=12)
#plt.xlabel("Pest incidence", fontsize=14)
#plt.ylabel("Farm size ha")
#plt.xticks(rotation=45)
#plt.savefig("Median_farm_size.png")
#plt.tight_layout()
#plt.show()


#what is the most common crop grown by farmers in this dataset?
#most_common_crop=df["Crop Type"].value_counts()
#print(most_common_crop)

#most_common_crop.plot(kind="bar", color=["coral","blue"])
#plt.title("Most Common Crop")
#plt.xlabel("Crop Type")
#plt.ylabel("Number of farmers")
#plt.xticks(rotation=45)
#plt.savefig("Most_common_crop.png")
#plt.tight_layout()
#plt.show()


#which village appears most frequently in the dataset?
#most_frequent_appearing_village=df["Village"].value_counts()
#print(most_frequent_appearing_village)

#most_frequent_appearing_village.plot(kind="bar", color=["coral","brown","blue"])
#plt.title("Most Frequent Appearing Village")
#plt.xlabel("Village")
#plt.ylabel("Number of farmers")
#plt.xticks(rotation=45)
#plt.savefig("Most_frequent_appearing_village.png")
#plt.tight_layout()
#plt.show()


#is pest incidence more common than not among these farmers?
#pest_incidence=df["Pest Incidence"].value_counts()
#print(pest_incidence)

#i will be plotting a pie chart
#plt.figure(figsize=(7,7))
#pest_incidence.plot(
    #kind="pie",
    #color=["coral", "seagreen"],
    #autopct="%1.1f%%",
    #startangle=90,
    
#)
#plt.title("Pest Incidence")
#plt.ylabel("")
#plt.tight_layout()
#plt.savefig("Pest_incidence_piechart.png")
#plt.show()


#what is the most common type of land ownership among the farmers? what type of chart are we using to draw it?
#most_common_type_of_land_ownership=df["Land Tenure"].value_counts()
#print(most_common_type_of_land_ownership)

#most_common_type_of_land_ownership.plot(kind="bar", color=["coral","brown","blue"])
#plt.title("Most Common Type Of Land Ownership")
#plt.xlabel("Land Tenure")
#plt.ylabel("Number of farmers")
#plt.xticks(rotation=45)
#plt.savefig("Most_common_type_of_land_ownership.png")
#plt.tight_layout()
#plt.show()


#Draw a bar chart showing the average yield after training for each village
#avg_yield_after_training = df.groupby("Village")["Yield After kg per hec"].mean()
#print(avg_yield_after_training)

#avg_yield_after_training.plot(kind="bar", color=["brown","blue", "indigo"])
#plt.title("average yield after training")
#plt.xlabel("Village", fontsize=14)
#plt.ylabel("Yield After kg per hec")
#plt.xticks(rotation=45)
#plt.savefig("Average_yield_after_per_village.png")
#plt.show()


#draw a bar chart showing the median fertilizer used by correct vs incorrect fertilizer users
#median_fertilizer_used=df.groupby("Fertilizer Type")["Fertilizer Used kg"].median()
#print(median_fertilizer_used)

#median_fertilizer_used.plot(kind="bar", color=["brown","blue", "indigo"])
#plt.title("Median fertilizer used")
#plt.xlabel("Fertilizer Type", fontsize=14)
#plt.ylabel("Fertilizer Used kg", fontsize=14)
#plt.xticks(rotation=45)
#plt.savefig("Median_Fertilizer_Used.png")
#plt.show()


#draw a bar chart showing how many farmers grow each crop type
number_of_farmers_for_each_crop_type=df["Crop Type"].value_counts()
print(number_of_farmers_for_each_crop_type)

number_of_farmers_for_each_crop_type.plot(kind="bar", color=["brown","blue", "indigo"])
plt.title("Number of farmers for each crop type", fontsize=14, fontweight="bold")
plt.xlabel("Crop Type", fontsize=14)
plt.ylabel("Farmer ID", fontsize=14)
plt.xticks(rotation=45)
plt.savefig("Number_of_farmers_for_each_crop_type.png")
plt.show()


#does using more fertilizer lead to a bigger yield change? scatter plot
#plt.figure(figsize=(7,7))
#plt.scatter(
    #df["Fertilizer Used kg"],
    #df["Yield Change"],
    #color=["red"],
    #edgecolor="black",
    #alpha=0.6
#)
#plt.title("Relationship Between Fertilizer Used and Yield Change", fontsize=14, fontweight="bold")
#plt.xlabel("Fertilizer Used kg")
#plt.ylabel("Yield Change")
#plt.tight_layout()
#plt.savefig("Fertilizer_vs_Yield_Change_Scatter.png")
#plt.show()


#how does avarage yield after training change as farm size increases? line graph
#avg_yield_by_size = df.groupby("Farm Size ha")["Yield After kg per hec"].mean()
#print(avg_yield_by_size)
#plotting the line graph
#plt.close('all')
#plt.figure(figsize=(8, 6))
#avg_yield_by_size.plot(kind="line", marker="o", color="indigo", linewidth=2, markersize=7)

#plt.title("Average Yield After Training by Farm Size", fontsize=14)
#plt.xlabel("Farm Size")
#plt.ylabel("Average Yield After Training")
#plt.tight_layout()
#plt.savefig("Average_Yield_by_Farm_Size_Line.png")
#plt.show()


# does using more fertilizer lead to a bigger yield change?scatter plot
#plt.close('all')
#plt.figure(figsize=(7,7))
#plt.scatter(
    #df["Fertilizer Used kg"],
    #df["Yield Change"],
    #color="teal",
    #alpha=0.7,
    #edgecolors="black"
    
#)
#plt.title("Relationship Between Fertilizer Used and Yield Change", fontsize=14)
#plt.xlabel("Fertilizer Used")
#plt.ylabel("Yield Change")
#plt.tight_layout()
#plt.savefig("Fertilizer_vs_Yield_Change_Scatter.png")
#plt.show()


#is there a relationship between farm size and yield change? scatter plot
#plt.close('all')
#plt.figure(figsize=(7,7))
#plt.scatter(
    #df["Farm Size ha"],
    #df["Yield Change"],
    #color="green",
    #alpha=0.7,
    #edgecolors="black"
    
#)
#plt.title("Relationship Between Farm Size and Yield Change", fontsize=14)
#plt.xlabel("Farm Size")
#plt.ylabel("Yield Change")
#plt.tight_layout()
#plt.savefig("Farm_Size_vs_Yield_Change_Scatter.png")
#plt.show()


#do farmers with higher yield before training also end up with higher yield after training?scatter plot
#plt.close("all")
#plt.scatter(
    #df["Yield Before kg per hec"],
    #df["Yield After kg per hec"],
    #color="coral",
    #alpha=0.7,
    #edgecolors="black"
    
#)
#plt.title("Relationship Between Yield Before And Yield After")
#plt.xlabel("Yield Before kg per hec")
#plt.ylabel("Yield After kg per hec")
#plt.tight_layout()
#plt.savefig("Yield_Before_vs_Yield_After_Scatter.png")
#plt.show()