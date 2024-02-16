import numpy as np

x = [1,2,3,4,5]
y = [5.5,43.1,128,290.7,498.4]
p = np.polyfit(x,y,3)
print(p)