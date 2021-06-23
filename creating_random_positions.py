import numpy as np
import pandas as pd

RA = np.random.uniform(low=-90.0, high=90.0, size=10000)
DEC = np.random.uniform(low=-0.0, high=360.0, size=10000)

positions = pd.DataFrame(RA,DEC)

positions.to_csv('ob_positions.csv', header='RA,DEC')

