import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

from pandas.tools.plotting import parallel_coordinates
from pandas.tools.plotting import andrews_curves
# Look pretty...
matplotlib.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
# .. your code here ..

df=pd.read_csv("wheat.Data")
df.drop(['id'], axis=1, inplace=True)


#
# TODO: Drop the 'id', 'area', and 'perimeter' feature
# 
# .. your code here ..



#
# TODO: Plot a parallel coordinates chart grouped by
# the 'wheat_type' feature. Be sure to set the optional
# display parameter alpha to 0.4
# 
# .. your code here ..

plt.figure()
andrews_curves (df, 'wheat_type')
plt.show()


