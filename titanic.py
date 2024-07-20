import seaborn as sns
import matplotlib.pyplot as plt


titanic = sns.load_dataset("titanic")
# sns.countplot(data=titanic, x='survived')
# plt.title('Count of Survivors')
# plt.show()

# sns.barplot(data=titanic, x='pclass', y='survived')
# plt.title('Survival Rate by Passenger Class')
# plt.show()

# sns.boxplot(data=titanic, x='survived', y='age' , hue="sex")
# plt.title('Age Distribution by Survival Status')
# plt.show()


# sns.violinplot(data=titanic, x='pclass', y='age')
# plt.title('Age Distribution by Passenger Class')
# plt.show()

# g = sns.FacetGrid(titanic, col='survived')
# g.map(sns.histplot, 'age')
# plt.show()

# sns.pairplot(titanic, hue='survived')
# plt.show()


# sns.swarmplot(data=titanic, x='survived', y='fare', hue='sex')
# plt.title('Fare Distribution by Survival Status and Sex')
# plt.show()


# g = sns.FacetGrid(titanic, col='sex', row='pclass', margin_titles=True)
# g.map(sns.histplot, 'survived', bins=2)
# g.add_legend()
# plt.show()


# sns.pointplot(data=titanic, x='pclass', y='fare', hue='survived')
# plt.title('Average Fare by Passenger Class and Survival Status')
# plt.show()


# sns.jointplot(data=titanic, x='age', y='fare', hue='survived')
# plt.show()
