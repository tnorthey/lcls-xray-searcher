from psana import *
from global_vars import *

# Experiment and run number
run = 43
Nevents = 100000 #Number of detector events to process

smldata = ds.small_data('%sxint_binning_run%d.h5' %(scratch_dir, run), gather_interval=100)  #This creates a 'small-data file' in your scratch folder


