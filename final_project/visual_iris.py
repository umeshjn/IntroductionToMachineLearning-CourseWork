import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
from pandas import read_csv

df = read_csv('iris.csv')

#Scatter of Petal
x=df['PetalLength']
y=df['PetalWidth']

print df
# Get unique names of species
uniq = list(set(df['Name']))

# Set the color map to match the number of species
z = range(1,len(uniq))
hot = plt.get_cmap('hot')
cNorm  = colors.Normalize(vmin=0, vmax=len(uniq))
scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=hot)

# Plot each species
for i in range(len(uniq)):
    indx = df['Name'] == uniq[i]
    plt.scatter(x[indx], y[indx], s=15, color=scalarMap.to_rgba(i))

plt.xlabel('Petal Width')
plt.ylabel('Petal Length')
plt.title('Petal Width vs Length')
plt.legend()
plt.show()