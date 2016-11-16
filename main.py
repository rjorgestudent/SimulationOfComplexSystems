import numpy as np
import matplotlib.pyplot as plt
import geometries

pts = geometries.box_with_hole()

plt.scatter(pts[:, 0], pts[:, 1])
# plt.xlim([-1, 11])
# plt.ylim([-1, 11])
plt.show()
