import os
import sys
sys.path.append('../../')
import driver

an = driver.analysis()
an.control = '../yaml/control_modis_l2.yaml'
an.read_control()
an.open_obs()
an.plot_obs()
# an.pair_data()
# an.plotting()
