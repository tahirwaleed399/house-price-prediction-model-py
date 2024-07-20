import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('./house.csv')
sns.set_theme()

# Drop the specified columns
df.drop(columns=["living area", "lot area", "waterfront present", 
                 "number of views", "grade of the house", "living_area_renov", 
                 "lot_area_renov" , "Renovation Year" , "Date" , "id" , "Longitude" , "Number of schools nearby" ,"Lattitude" , "Postal Code"], inplace=True)

# Rename the specified columns
df.rename(columns={"number of bedrooms": "Bedrooms", "number of bathrooms": "Bathrooms"}, inplace=True)
df = df.drop_duplicates()

# Check for duplicate rows
duplicates = df.duplicated()

# Display duplicate rows
duplicate_rows = df[duplicates]


x = df.drop("Price" , axis=1)
y = df['Price']

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y , test_size=20 ,random_state=101)


from sklearn.linear_model import LogisticRegression

lreg = LogisticRegression()

lreg.fit(x_train , y_train)

print(x_test.head())
y_predicted = lreg.predict(x_test)
print(y_predicted)

# Plotting
# sns.boxplot(x=df['Built Year'])

# # Show the plot
# plt.show()
