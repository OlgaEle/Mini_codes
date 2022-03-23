import seaborn as sns
import matplotlib.pyplot as plt

#Kernel Density Plot
plt.figure(figsize = (12,6))
sns.kdeplot(data = df[df.stroke == 1],
            x = 'age', shade = True, color = 'purple', alpha = 1)
sns.kdeplot(data = df[df.stroke == 0],
            x = 'age', shade = True, color = 'darkcyan', alpha = 0.7)
plt.xlabel("Age", fontsize = 15,font = 'monospace')
