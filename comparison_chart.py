import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from test_bench import displaying_results


my_images = ["data/J+12_PM_GA.jpg"]
a = [[23],[43],[46],[43]]
b = displaying_results(my_images, 0)
c = np.hstack((a,b))

df=pd.DataFrame({'x_values': range(2), 'bht': c[0], 'multi-otsu 1': c[1], 'multi-otsu 2': c[2], 'otsu': c[3] })
 
# multiple line plots
plt.plot( 'x_values', 'bht', data=df, marker='o', markerfacecolor='blue', markersize=12, color='blue', linewidth=4)
plt.plot( 'x_values', 'multi-otsu 1', data=df, marker='o', markerfacecolor='green', markersize=12, color='green', linewidth=4)
plt.plot( 'x_values', 'multi-otsu 2', data=df, marker='o', markerfacecolor='green', markersize=12, color='green', linewidth=4)
plt.plot( 'x_values', 'otsu', data=df, marker='o', markerfacecolor='red', markersize=12, color='red', linewidth=4)
# show legend
plt.legend()

# show graph
plt.show()