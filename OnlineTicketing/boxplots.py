import numpy as np
import matplotlib.pyplot as plt

data = [1.49492, 3.66265, 2.85902, 1.85234, 2.85404, 3.25728, 3.46318, 0.75151, 1.04772, 0.74756,
        0.37638, 4.36083, 3.25326, 4.36191, 1.05304, 3.06593, 3.04858, 0.14795, 0.82941, 1.35065,
        3.53038, 1.54825, 4.54474, 4.55102, 2.33507, 2.34540, 4.12416, 4.75065, 1.24891, 3.75053,
        0.75030, 3.75585, 5.05404, 0.26528, 3.75451, 4.95535, 0.15843, 0.19216, 3.65155, 2.46147,
        5.07228, 1.34821, 3.71493, 1.44762, 4.25472, 0.35370, 3.75472,2.96774, 4.64964, 4.05474]

print(data)

fig1, ax1 = plt.subplots()
ax1.set_title('Response times')
ax1.boxplot(data)
plt.show()
